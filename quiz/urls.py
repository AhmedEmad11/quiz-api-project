from django.urls import path

from .views import GetTest, QuestionList, index

urlpatterns = [
    path('', index, name="index"),
    path('test/', GetTest.as_view(), name="test"),
    path('questionList/', QuestionList.as_view(), name="questionList"),
]