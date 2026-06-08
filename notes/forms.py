"""Forms for the notes application."""

from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
	"""Provide a form for creating and updating notes."""

	class Meta:
		"""Configure note form fields and widgets."""

		model = Note
		fields = ["title", "content"]
		widgets = {
			"title": forms.TextInput(attrs={"placeholder": "Note title"}),
			"content": forms.Textarea(
				attrs={"rows": 10, "placeholder": "Write your note here..."}
			),
		}