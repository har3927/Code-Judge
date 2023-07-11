from django.contrib import admin
from . import models

myModels = [models.Problem, models.Solution, models.TestCase]
admin.site.register(myModels)
