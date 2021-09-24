from django.shortcuts import render
# from Bright_demo_app.models import People
from .models import People,Daycare
from django.http import HttpResponse

def hello(request,daycare_id):


    people= People.objects.filter(Daycare_info=daycare_id)

    daycare_name=Daycare.objects.get(id=daycare_id)

    context={
        'NAME':people,'daycare_name':daycare_name,'daycare_id':daycare_id
     }


    return render(request, 'test111.html',context=context)

def hello1(request):
    BBB= Daycare.objects.all()
    context1={
        'NAME':BBB
    }
    return render(request,"test112.html",context=context1)

def hello2(request,student_id):

    EEEE=People.objects.filter(id=student_id)

    context2={
        'NAME2':EEEE
    }
    return render(request,"test113.html",context=context2)

def hello3(request,student_id):
    kid=People.objects.get(id=student_id)
    Q=kid.Daycare_info
    daycare_id=Q.id
 #   kid.daycare_info
 #   print(kid.name)
    kid.delete()
    people=People.objects.filter(Daycare_info=Q)

    daycare_name = Daycare.objects.get(id=Q.id)
    context = {
        'NAME': people,'daycare_name':daycare_name,'daycare_id':daycare_id
    }

    return render(request, 'test111.html', context=context)

def hello4(request):
    student_id=request.POST.get('id')
    student_name=request.POST.get('name')
    student_age=request.POST.get('age')
    FF=request.POST.get('gender')
    if FF=="True":
        student_gender=True
    else:
        student_gender=False
    student_parent_name=request.POST.get('parent_name')
    student_tel=request.POST.get('tel')
    student_address=request.POST.get('address')
    student_payment_info=request.POST.get('payment_info')
    student_teacher=request.POST.get('teacher')
    student_memo=request.POST.get('memo')
    student_daycare=request.POST.get('daycare_id')
    new_student=People(student_id,student_name,student_gender,student_age,student_parent_name,student_tel,
                   student_address,student_payment_info,student_teacher,student_memo,student_daycare)
    new_student.save()
    return HttpResponse('Create / Modify student successfully.')

def hello5(request):
    return render(request,'creat_student.html')