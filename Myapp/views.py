from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def four(request):
    return render(request,'404.html')
def about(request):
    return render(request,'about.html')
def appointment(request):
    return render(request,'appointment.html')
def call(request):
    return render(request,'call-to-action.html')
def classes(request):
    return render(request,'classes.html')
def contact(request):
    return render(request,'contact.html')
def facility(request):
    return render(request,'facility.html')
def team(request):
    return render(request,'team.html')
def testimonials(request):
    return render(request,'testimonial.html')

# Create your views here.
