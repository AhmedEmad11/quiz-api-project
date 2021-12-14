from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view

from .serializers import QuestionSerializer
from .models import Question


@api_view(['GET'])
def index(request):
    api_urls = {
        'GET for one test': '/test/',
        'GET for all questions': '/questionList/',
    }
    
    return Response(api_urls)

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class GetTest(generics.ListCreateAPIView):
    queryset = Question.objects.order_by('?')[:2]
    
    serializer_class = QuestionSerializer

