from django.test import TestCase

from .models import Note


class NoteModelTest(TestCase):
	def test_create_note(self):
		note = Note.objects.create(
			title="Test Title",
			content="Test Content"
		)
		self.assertEqual(note.title, "Test Title")
		self.assertEqual(note.content, "Test Content")
