from django.shortcuts import render

# Create your views here.
def edu(request):
    context={'edu':'active'}
    return render(request,'edu/edu.html',context)