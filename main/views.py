from django.shortcuts import render
from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Harjuno Abdullah',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)