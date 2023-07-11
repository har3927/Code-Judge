import subprocess
from datetime import datetime
import random
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Problem, Solution, TestCase
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import platform
from django.http import HttpResponse

# COMPILE = ["g++", "temp.cpp"]
COMPILE='g++ C:/djangoproject/djangoproj/temp.cpp'
# RUN = ["./a.out"]
RUN = './a.exe'

def index(request):
    return render(request, 'judge/index.html')

def list_problems(request):
    problemset = Problem.objects.all()
    context = {'problemset' : problemset}
    return render(request, 'judge/problems_list.html', context)

def detail(request, question_id):
    pro = Problem.objects.get(pk=question_id)
    io=TestCase.objects.filter(problem=pro)[0]
    if request.method == 'GET':
        problem = get_object_or_404(Problem, pk = question_id)
        context = {'problem' : problem,'io':io,'problem':pro}
        return render(request, 'judge/problem.html', context)
    else:
        return submit(request, question_id)
@login_required(login_url='users:login')
def submit(request, question_id):
    submitted_by=request.user
    if request.method == 'POST':
        code = request.POST['code']
        language = request.POST['language']

        if language == 'cpp':
            file_extension = 'cpp'
            compile_command = f'g++ temp.{file_extension} -o temp.exe'
            if platform.system() == 'Windows':
                execute_command = 'temp.exe'
            else:
                execute_command = './a.out'
        elif language == 'python':
            file_extension = 'py'
            compile_command = None
            execute_command = 'python temp.py'
        elif language == 'java':
            file_extension = 'java'
            compile_command = f'javac Main.{file_extension}'
            execute_command = 'java Main'

        with open(f'temp.{file_extension}', 'w') as file:
            file.write(code)

        if compile_command:
            _compile = subprocess.run(compile_command, shell=True, stdout=subprocess.PIPE)

            if _compile.returncode != 0:
                verdict = Solution.Verdict.COMPILATION_ERROR
            else:
                verdict = Solution.Verdict.Success
        else:
            verdict = Solution.Verdict.Success

        problem = get_object_or_404(Problem, pk=question_id)
        tests = TestCase.objects.filter(problem=problem)

        for test in tests:
            input_data = test.input
            expected_output = test.output
            expected_output = expected_output.replace("\r\n", "\n").replace("\r", "\n")

            try:
                _run = subprocess.run(execute_command, shell=True, stdout=subprocess.PIPE, input=input_data, encoding='ascii', timeout=1, check=True)
                actual_output = _run.stdout.strip().rstrip("/n").strip()

                if expected_output != actual_output:
                    verdict = Solution.Verdict.Wrong_Output
                    break
            except subprocess.TimeoutExpired:
                verdict = Solution.Verdict.Time_Limit_Exceeded
                break
            except Exception as e:
                verdict = Solution.Verdict.Runtime_Error
                print("Runtime Error:", e)  # Print the exception message
                break

        sol = Solution(
            problem=problem,
            verdict=verdict,
            submittedAt=datetime.now(),
            language=language,
            code=code,
            submittedBy=submitted_by
        )
        sol.save()

        return HttpResponseRedirect(reverse('leaderboard'))



@login_required(login_url='users:login')
def leaderboard(request):
    recent_submissions = Solution.objects.all().order_by('-submittedAt')[:10]
    return render(request, 'judge/leaderboard.html', {"result": recent_submissions})
