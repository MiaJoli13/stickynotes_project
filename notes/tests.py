from django.test import TestCase
from django.urls import reverse

from .models import Note


class NoteModelTest(TestCase):
	"""Unit tests for the `Note` model."""

	def setUp(self):
		"""Create a sample note instance for model tests."""

		self.note = Note.objects.create(title="Test Title", content="Test Content")

	def test_create_note(self):
		"""Verify a `Note` stores title and content correctly."""

		self.assertEqual(self.note.title, "Test Title")
		self.assertEqual(self.note.content, "Test Content")

	def test_note_string_representation(self):
		"""Verify `Note.__str__()` returns the note title."""

		self.assertEqual(str(self.note), "Test Title")


class NoteViewTest(TestCase):
	"""Unit tests for note CRUD views using Django's test client."""

	def setUp(self):
		"""Create a sample note instance for view tests."""

		self.note = Note.objects.create(title="Test Title", content="Test Content")

	def test_note_list_view(self):
		"""Verify the list page loads and displays note data."""

		response = self.client.get(reverse("notes:note_list"))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Sticky Notes")
		self.assertContains(response, "Test Title")

	def test_note_list_view_empty_state(self):
		"""Verify empty-state text is shown when there are no notes."""

		Note.objects.all().delete()
		response = self.client.get(reverse("notes:note_list"))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No notes yet")

	def test_note_detail_view(self):
		"""Verify the detail page loads and displays note content."""

		response = self.client.get(reverse("notes:note_detail", args=[self.note.pk]))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Test Title")
		self.assertContains(response, "Test Content")

	def test_note_detail_view_404_for_missing_note(self):
		"""Verify requesting an invalid note id returns 404."""

		response = self.client.get(reverse("notes:note_detail", args=[9999]))
		self.assertEqual(response.status_code, 404)

	def test_note_create_view(self):
		"""Verify posting valid data creates a note and redirects."""

		response = self.client.post(
			reverse("notes:note_create"),
			{"title": "New Note", "content": "New Content"},
		)
		self.assertEqual(response.status_code, 302)
		self.assertTrue(Note.objects.filter(title="New Note").exists())

	def test_note_update_view(self):
		"""Verify posting valid data updates a note and redirects."""

		response = self.client.post(
			reverse("notes:note_update", args=[self.note.pk]),
			{"title": "Updated Title", "content": "Updated Content"},
		)
		self.assertEqual(response.status_code, 302)
		self.note.refresh_from_db()
		self.assertEqual(self.note.title, "Updated Title")
		self.assertEqual(self.note.content, "Updated Content")

	def test_note_delete_view(self):
		"""Verify posting to delete removes a note and redirects."""

		response = self.client.post(reverse("notes:note_delete", args=[self.note.pk]))
		self.assertEqual(response.status_code, 302)
		self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
