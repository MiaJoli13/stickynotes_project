"""View functions for the notes application."""

from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note


def note_list(request):
	"""Render the main sticky notes list page."""

	notes = Note.objects.order_by("-created_at")
	return render(request, "notes/note_list.html", {"notes": notes})


def note_detail(request, pk):
	"""Show the details for a single note."""

	note = get_object_or_404(Note, pk=pk)
	return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
	"""Create a new sticky note."""

	if request.method == "POST":
		form = NoteForm(request.POST)
		if form.is_valid():
			note = form.save()
			return redirect("notes:note_detail", pk=note.pk)
	else:
		form = NoteForm()
	return render(request, "notes/note_form.html", {"form": form, "page_title": "Create note"})


def note_update(request, pk):
	"""Edit an existing sticky note."""

	note = get_object_or_404(Note, pk=pk)
	if request.method == "POST":
		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			note = form.save()
			return redirect("notes:note_detail", pk=note.pk)
	else:
		form = NoteForm(instance=note)
	return render(request, "notes/note_form.html", {"form": form, "note": note, "page_title": "Edit note"})


def note_delete(request, pk):
	"""Confirm and delete a sticky note."""

	note = get_object_or_404(Note, pk=pk)
	if request.method == "POST":
		note.delete()
		return redirect("notes:note_list")
	return render(request, "notes/note_confirm_delete.html", {"note": note})
