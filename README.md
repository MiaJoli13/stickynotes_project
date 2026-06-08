# Sticky Notes Project

This is a Django sticky notes application that lets users create, view, update, and delete notes.

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run database migrations with `python manage.py migrate`.
4. Start the development server with `python manage.py runserver`.

## Implementation Steps

1. Defined the `Note` model with `title`, `content`, and `created_at` fields.
2. Added a `NoteForm` for creating and editing notes.
3. Built list, detail, create, update, and delete views.
4. Added navigation buttons so users can move between all CRUD actions.
5. Created reusable templates for listing, editing, and deleting notes.
6. Added tests for the model and core note views.

## Features

- Home page that lists all notes.
- Note detail page for reading a single note.
- Create, update, and delete note actions.
- Clean responsive styling for the note pages.
