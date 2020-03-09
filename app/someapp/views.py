from django.shortcuts import render

# Create your views here.
from .models import Huuser
from .forms import PostHuuserForm

def index(request):
    huusers = Huuser.objects.all()
    if request.method == "POST":
        form = PostHuuserForm(request.POST)
        if form.is_valid():
            huuser = form.save(commit=False)
            print("HERE'S HUUSER OBJECT FROM THE FORM:", huuser)
            print(huuser.first_name, huuser.goal_in_life) # do whatever you want
            huuser.save()
    else: 
        form = PostHuuserForm()
    return render(request, 'index.html', {"huusers": huusers, "form": form})