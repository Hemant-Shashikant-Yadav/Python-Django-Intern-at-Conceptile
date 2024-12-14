from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('start/', views.start_quiz, name='start_quiz'),
    path('start/session/<uuid:session_id>/question/', views.quiz_question, name='quiz_question'),
    path('start/session/<uuid:session_id>/submit/', views.submit_answer, name='submit_answer'),
    path('start/session/<uuid:session_id>/summary/', views.quiz_summary, name='quiz_summary')
]