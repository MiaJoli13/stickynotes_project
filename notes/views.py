from django.http import HttpResponse


def home(request):
	return HttpResponse("Sticky Notes App")

# Create your views here.
