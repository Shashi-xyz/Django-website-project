from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages 
# Create your views here.



def index(request):
    context = {
     "variable1": "this is varriable value1 ram",
     "variable2": "this is varriable value2 shayam"
}
    return render(request, 'index.html', context)
   #return HttpResponse("this is home page")
    

def about(request):
    #return HttpResponse('this is about page')
    return render(request, 'about.html')
 
def services(request):
    #return HttpResponse('this is service page')
    return render(request, 'services.html')
 
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        if name and email:  # Ensure no empty entries
            contact_entry = Contact(name=name, email=email, date=datetime.today())
            contact_entry.save()
            messages.success(request, "Profile details updated.")
            return render(request, 'contact.html', {'message': "Contact saved!"})
            
    return render(request, 'contact.html')  


