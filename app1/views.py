from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from app1.forms import AddnewclassForm,StudentForm
from app1.models import AddNewClasses,StudentModel,EnrollSubjects

def home(request):
    return render(request,'home.html')

def adlogin(request):       #RETURN TO SAME PLACE AFTER ADMIN LOGIN
    uname=request.POST.get('a1')
    passw=request.POST.get('a2')

    if uname == 'bapu' and passw == 'bapu':
        return render(request,'adhome.html')
    else:
        return render(request,'adlogin.html')

def newclass(request):
    form=AddnewclassForm()
    return render(request,'newclass.html',{'form':form})

def savenew(request):
    res=AddnewclassForm(request.POST)
    if res.is_valid():
        res.save()
        messages.success(request, 'Saved Successfully')
        return redirect('newclass')
    else:
        return render(request, 'newclass.html', { 'error': res.errors,'form':res})



def viewallclass(request):
    res=AddNewClasses.objects.all()
    return render(request,'viewallclass.html',{'res':res})

def subupdate(request):
    no=request.GET.get('no')
    res=AddNewClasses.objects.get(no=no)
    form=AddnewclassForm(instance=res)
    if request.method =='POST':
        form=AddnewclassForm(request.POST,instance=res)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated successfully')
            return redirect('viewallclass')
        else:
            return render(request,'subupdate.html',{'error':form.errors,"form":form})
    return render(request,'subupdate.html',{'form':form})

def delete(request):
    no=request.GET.get('no')
    AddNewClasses.objects.get(no=no).delete()
    return redirect('viewallclass')

def studenthome(request):
    return render(request,'studenthome.html')

def st_register(request):
    form1=StudentForm()
    return render(request,'st_register.html',{'form1':form1})

def st_save(request):
    stu=StudentForm(request.POST)
    if stu.is_valid():
        stu.save()
        return render(request, 'st_register.html', {'success':'Saved successfully'})
    else:
        return render(request,'st_register.html',{'error':stu.errors,'form1':stu})


def st_login(request):
    return render(request,'st_login.html')


def logins_stu(request):
    con= request.POST.get("s1")
    passw = request.POST.get("s2")
    try:
        log = StudentModel.objects.get(contact=con, passw=passw)
        return render(request,'stu_profile_home.html', {'cont': con})

    except StudentModel.DoesNotExist:
        messages.error(request,'Contact No Or Password in Invalid')
        return redirect('st_login')


def enroll(request):
    cont = request.GET.get('con')
    all_clases=AddNewClasses.objects.all()
    return render(request,'enroll.html',{'classes':all_clases,'cno':cont})

def e_roll(request):
    id=request.GET.get('no')
    cno=request.GET.get('cno')
    EnrollSubjects(no=id,contact=cno).save()
    return redirect('enroll')

def view_enrollclass(request):
    cont = request.GET.get('con')
    return render(request,'view_enrollclass.html',{'cno':cont})