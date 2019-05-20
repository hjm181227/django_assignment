from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Board, Resume

from .serializer import BoardSerializer, ResumeSerializer


class BoardListCreateAPIView(ListCreateAPIView):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ResumeListCreateAPIView(ListCreateAPIView):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
