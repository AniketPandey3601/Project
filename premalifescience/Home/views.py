from datetime import datetime
from django.shortcuts import render,HttpResponse
from Home.models import contact,Products,Covid_Solutions
from django.templatetags.static import static


# Create your views here.
def Home(request):
    # return HttpResponse('this is home page')
    return render(request,'Home.html')

def AboutUS(request):
    return render(request,'about.html')
    
 
def Contact(request):
    if request.method=="POST":
      
        name= request.POST.get('name')
        email= request.POST.get('email')
        number= request.POST.get('number')
        desc= request.POST.get('desc')
        ins=contact(name=name,email=email,number=number,desc=desc,date=datetime.today())
        ins.save()
        
    
    return render(request,'contact.html')
   
def PRODUCTSHOME(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request,'productshome.html',context)

def PRODUCTS(request,slug):
    
    return HttpResponse(f"you are viewing {slug}")

    
def COVID19SOLUTIONSHOME(request):
    covids = Covid_Solutions.objects.all()
    context = {'covids': covids}

    return render(request,'covidhome.html',context)
    
def COVID19SOLUTIONS(request,slug):
   return HttpResponse(f"you are viewing {slug}")
    
def MEDIA(request):
    return render(request,'media.html')
    
def CAREER(request):
    return render(request,'career.html')
    