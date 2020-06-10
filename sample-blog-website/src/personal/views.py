from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
	context = {}
	context['some_string'] = "this is some string I am passing to view"
	context['some_number'] = 12345

	# other way to use ocntext to pass the data to template from views class
	#context = {
	#		"some_string" : "this is some string I am passing to view",
	#		"some_number" : 12345,
	#}

	list_of_values = []
	list_of_values.append("first entry")
	list_of_values.append("second entry")
	list_of_values.append("third entry")
	list_of_values.append("fourth entry")

	context['list_of_values'] = list_of_values


	return render(request, "personal/home.html", context)