from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from app.registration_form import registration_form,todolist_form
from django.core.mail import EmailMultiAlternatives
from app.models import user_registration,todolist_info
import random
from django.urls import reverse
import datetime
from django.core.mail import EmailMultiAlternatives
from threading import Timer
# Create your views here.
def homepage(request):
    request.session['log']=False
    return render(request,'homepage.html')

def registration_page(request):
    request.session['log']=False
    registration_form_obj= registration_form()
    if request.method=='POST':
        registration_form_obj=registration_form(request.POST)
        if registration_form_obj.is_valid():
            registration_form_obj.save()
            return HttpResponseRedirect(reverse('app:login_page'))
            #return redirect('login_page')

    return render(request,'registration_page.html',context={'registration_form':registration_form_obj})


def login_page(request):
    request.session['log']=False
    if request.method=='POST':
        name=request.POST.get('name')
        passes=request.POST.get('pass')
        print(name)

        try:
            obj=user_registration.objects.get(user_name=name,user_password=passes)
            request.session['user_name']=name
            request.session['log']=True
            return render(request,'todo_page.html',{'name':name})

            print(obj.user_email)
        except:
            print('exception')
            return render(request,'except.html')
    return render(request,'login_page.html',{'type':0})

def todo_page(request):
    name=request.session['user_name']
    form_obj=todolist_form()
    if request.method=='POST':
        form_obj=todolist_form(request.POST)
        print('success')
        x=form_obj.save(commit=False)
        print(x.event_name+" "+x.event_description)
        obj=user_registration.objects.get(user_name=name)
        x.user_obj=obj
        x.date_event=str(request.POST.get('date'))
        print(x.date_event)
        x.save()
        return render(request,'todo_page.html')

    return render(request,'create_list.html',{'obj':form_obj})


def see(request):
    name=request.session['user_name']
    #obj_main=user_registration.objects.filter(user_name=name)
    obj_main=todolist_info.objects.filter(user_obj=user_registration.objects.get(user_name=name))
    return render(request,'see.html',{'obj':obj_main})
    # mail=obj_main[0].user_email
    # obj=todolist_info.objects.all()
    # #return render(request,'see.html',{obj:obj,mail:mail})
    # for i in obj:
    #     if i.user_obj.user_email == mail:
    #         print(str(i.date_event)+" "+i.event_name+" "+i.event_description)
    #return render(request,'todo_page.html')
    # return render(request,'see.html',{'obj':obj,'mail':mail})


def mail_scheduler():
    print('come')
    x = str(datetime.datetime.now())[:10]
    todolist_obj=todolist_info.objects.all()
    for obj in todolist_obj:
        print(obj.date_event)
        print(x)
        if str(obj.date_event) == x:
             print('1')
             event_reminder(user_email=obj.user_obj.user_email,user_name=obj.user_obj.user_name,event_name=obj.event_name,event_description=obj.event_description)
             obj.delete()
    #Timer(60*60*24.0, mail_scheduler).start() enable these 2 for sechuled mails
#Timer(10.0,mail_scheduler).start()
#---------------------------------------------------------------------------------

def  event_reminder(user_email,user_name,event_name,event_description):
    print('2')
    subject, from_email, to = 'Remainder Email', 'umgkrishna00.com',user_email
    text_content = ''
    html_content = '<p>You have an upcomming event {}, {}</p>'.format(event_name,event_description)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    print(msg.send())
