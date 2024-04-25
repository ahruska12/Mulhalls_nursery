from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from .views import RegisterView, login, get_customer_account, RegisterEmpView, getDepartments, elogin, \
    get_employee_account, QuestionAsked, getAllQuestions, getQuestionsByCust, getQuestionsByPlant, \
    getQuestionsByID, AnswerQuestion

app_name = "user"

urlpatterns = [
    # Url that directs to the register view
    # commented out methods aren't needed (right now)
    path('register/customer', RegisterView.as_view(), name='auth_register'),
    path('register/employee', RegisterEmpView.as_view(), name='emp_register'),
    path('auth/<str:username>', login),
    path('auth/employee/<str:username>', elogin),
    path('find-account/customer/<str:email>', get_customer_account),
    path('find-account/employee/<str:email>', get_employee_account),
    path('departments', getDepartments),
    path('ask/question', QuestionAsked.as_view(), name='ask-question'),
    path('list/questions', getAllQuestions, name='list-questions'),
    path('list/questions/<int:var>', getAllQuestions, name='list-unanswered-questions'),
    # path('find/questions-cust/<int:cust_id>', getQuestionsByCust, name='question-by-cust'),
    # path('find/questions-plant/<int:plant_id>', getQuestionsByPlant, name='question-by-plant'),
    path('find/questions-id/<int:question_id>', getQuestionsByID, name='question-by-id'),
    path('answer/question', AnswerQuestion.as_view(), name='answer-question'),
]
