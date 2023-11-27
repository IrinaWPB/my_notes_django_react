from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def get_routes(request):
  api_routes = [
    {
      'endopoint': '/notes/',
      'method': 'GET',
      'body': None,
      'description': 'Returns an array of notes'
    },
    {
      'endopoint': '/notes/id',
      'method': 'GET',
      'body': None,
      'description': 'Returns a single not object'
    },
    {
      'endopoint': '/notes/create',
      'method': 'POST',
      'body': {'body': ""},
      'description': 'Creates a new note'
    },
    {
      'endopoint': '/notes/id/update/',
      'method': 'PUT',
      'body': {'body': ""},
      'description': 'Updates an existing note'
    },
    {
      'endopoint': '/notes/id/delete/',
      'method': 'DELETE',
      'body': None,
      'description': 'Deletes a note'
    },
  ]
  return Response(api_routes)

@api_view(['GET'])
def get_notes(request):
  notes = Note.objects.all()
  serializer = NoteSerializer(notes, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def get_note(request, pk):
  note = Note.objects.get(id=pk)
  serializer = NoteSerializer(note, many=False)
  return Response(serializer.data)