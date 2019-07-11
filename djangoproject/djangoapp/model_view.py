from django.shortcuts import render
from .form import StuForm,EmployeeForm
from .mobile_form import mobForm
from django.shortcuts import render
from django.shortcuts import redirect

def student_index(request):
    stu = StuForm()
    return render(request, "studentinfo.html", {'form': stu})

def mobile_index(request):
    mbu=mobForm()
    return render(request, "mobileinfo.html", {'form': mbu})


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/djangoapp/vinayinfo')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'emp.html',{'form':form})