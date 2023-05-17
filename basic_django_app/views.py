from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    my_name = "Ben Peterson"
    from basic_django_app.namer import learn_django
    return render(request, 'about.html', {"my_name": my_name, "namer": learn_django})