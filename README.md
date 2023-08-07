# Code Judge

Code Judge is a Django-based web application designed to provide a platform for executing and evaluating code submissions in three popular programming languages: C++, Java, and Python. Whether you're a learner looking to practice coding problems or an educator aiming to automate assessments, Code Judge simplifies the process of running and grading code submissions.

## Features

- **Multi-Language Support**: Code Judge supports code submissions in C++, Java, and Python, making it versatile for various programming challenges.
- **User-Friendly Interface**: The intuitive web interface allows users to submit their code, choose the desired programming language, and receive prompt feedback on their submissions.
- **Automated Evaluation**: Code Judge evaluates user submissions based on predefined test cases, providing instant verdicts such as successful execution, compilation errors, incorrect answers, runtime issues, and more.
- **Scalable and Customizable**: Easily extend the platform by adding new programming languages, problem sets, or custom test cases to tailor the application to your needs.
- **Admin Dashboard**: An admin dashboard is provided to manage problems, view user submissions, and review evaluations.
- **User Authentication**: User registration and authentication system ensure secure access and maintain personalized profiles.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/har3927/Code-Judge.git
    cd Code-Judge
    ```

2. **Install Dependencies**:
    Create a virtual environment (optional but recommended) and install the project dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Run Migrations**:
    Apply the initial database migrations:
    ```bash
    python manage.py migrate
    ```

4. **Create a Superuser**:
    Create an admin superuser to access the admin dashboard:
    ```bash
    python manage.py createsuperuser
    ```

5. **Run the Development Server**:
    Start the development server:
    ```bash
    python manage.py runserver
    ```

6. **Access the Application**:
    Open your web browser and navigate to `http://127.0.0.1:8000/` to access the Code Judge application.
