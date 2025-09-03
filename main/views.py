from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406434090',
        'name': 'Daffa Ismail',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)