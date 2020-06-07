from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Board
from .serializers import BoardSerializer

# Create your views here.
@api_view(['GET'])
def board_list(request):
    if request.method == 'GET':
        queryset = Board.objects.all()
        serializer = BoardSerializer(queryset, many=True)
        return Response({'data':serializer.data})
