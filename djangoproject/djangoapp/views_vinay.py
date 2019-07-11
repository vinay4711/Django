from django.shortcuts import render
from .form import StuForm
from .mobile_form import mobForm,Vinay_form
from django.http import HttpResponse
from .functions import handle_uploaded_file



def vinayinfo(request):
    vinay = Vinay_form()

    if request.method == 'POST':
        vinay = Vinay_form(request.POST, request.FILES)
        if vinay.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
        else:
            return HttpResponse("File not uploaded successfuly")

    else:
        student = Vinay_form()
        return render(request, "vinay.html", {'form': vinay})

