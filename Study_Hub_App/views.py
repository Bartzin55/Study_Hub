from django.shortcuts import render


# Create your views here.
def index(request):  # type: ignore
    return render(request, "Study_Hub_App/index.html")  # type: ignore


def mainPage(request):  # type: ignore
    return render(request, "Study_Hub_App/mainPage.html")  # type: ignore


def overallPage(request):  # type: ignore
    return render(request, "Study_Hub_App/overallPage.html")  # type: ignore


def schedulePage(request):  # type: ignore
    return render(request, "Study_Hub_App/schedulePage.html")  # type: ignore


def signUp(request):  # type: ignore
    return render(request, "Study_Hub_App/signUp.html")  # type: ignore
