from django.shortcuts import render
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

class CreateNoteView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class RetrieveNoteView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class QueryNotesView(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title', '')
        return Note.objects.filter(title__icontains=title)

class UpdateNoteView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    # No need to override the put method unless adding custom logic
