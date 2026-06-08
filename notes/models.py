from django.db import models


class Note(models.Model):
	"""Store a single sticky note item."""

	title = models.CharField(max_length=100)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Return the note title for admin and debugging views."""

		return self.title
