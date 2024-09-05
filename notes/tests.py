from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Note

class NoteTests(APITestCase):
    def test_create_note(self):
        url = reverse('create-note')
        data = {'title': 'Test Note', 'body': 'This is a test note.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_note_by_id(self):
        note = Note.objects.create(title='Test Note', body='This is a test note.')
        url = reverse('retrieve-note', args=[note.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_query_notes_by_title(self):
        Note.objects.create(title='Test Note', body='This is a test note.')
        url = reverse('query-notes')
        response = self.client.get(f'{url}?title=Test', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_note(self):
        note = Note.objects.create(title='Old Title', body='This is a test note.')
        url = reverse('update-note', args=[note.id])
        data = {'title': 'New Title', 'body': 'Updated body.'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        note.refresh_from_db()
        self.assertEqual(note.title, 'New Title')
        self.assertEqual(note.body, 'Updated body.')
