from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
	context	= {
	"title":"this is being rendered out through context",
	"content": "this is an awesome content",
	#"premium_content":"Even if there be one good which is universally predictable or is capable of independent existence, it could not be attained by man."
	}
	if request.user.is_authenticated:
		context['premium_content'] = "Even if there be one good which is universally predictable or is capable of independent existence, it could not be attained by man."
	return render(request, "home_page.html", context)


def about_page(request):
	context	= {
	"title" : " this is being rendered out from about",
	"policy": "here is the policy"
	}
	return render(request, "home_page.html", context)


def contact_page(request):

	contact_form = ContactForm(request.POST or None)
	context = {

		"title":"New Contact Page",
		"form": contact_form

	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# print(request.POST)
	# print(request.POST.get('fullname'))
	# print(request.POST.get('email'))
	# print(request.POST.get('content'))

	return render(request, "contact/view.html", context)

def service_page(request):
	
	return render(request, "service_page.html")

def call_page(request):
	return render(request, "home_page.html", context)

def login_page(request):
	form = LoginForm(request.POST or None)
	context	= {
		"form": form
	}
	print("user logged in")
	#print(request.user.is_authenticated)
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		#copy from here context['form'] = LoginForm()
		user = authenticate(request, username=username, password=password)
		print(user)
		#print(request.user.is_authenticated)
		if user is not None:
			#print(request.user.is_authenticated)
			login(request, user)
			#context['form'] = LoginForm()
			return redirect("/")
		else:
				print("error")

	
	return render(request, "auth/login.html", context)


user = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		"form": form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		newuser = user.objects.create_user(username, email, password)
		print(username)
	return render(request, "auth/register.html", context)



def home_page_old(request):
	html_ = """

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, how are you doing ?</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>

"""

	return HttpResponse(html_)