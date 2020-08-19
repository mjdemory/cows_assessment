from django.shortcuts import render
import subprocess

from homepage.models import CowText

from homepage.forms import InputForm

# Create your views here.


def index(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowText.objects.create(
                body=data.get('body')
            )

            cow_run = subprocess.run(['cowsay', data.get('body')], capture_output=True, text=True)
            return render(request, "index.html", {"form": InputForm(), "cow_run": cow_run.stdout})

    form = InputForm()
    return render(request, "index.html", {"form": form})


def history(request):
    cow_history = CowText.objects.filter().order_by('-id')[:10]
    return render(request, "history.html", {"cow_history": cow_history})

