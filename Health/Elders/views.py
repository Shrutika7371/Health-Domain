from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import Healthdata
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here'


def index(request):
    obj=Healthdata.objects.all() # it passes the all diseses from data base 
    dict1={'obj':obj}
    return render(request,'index.html',dict1)



#this view checks if person have any disease ,if any then provide do's and dont's for the person in daily life
#if he/she doesn't have any disease then do's and dont's for the  age > 65
def diseasecheck(request):
    name = request.POST.get('namef')
    email = request.POST.get('email')
    var = request.POST.get('disease')
    obj= Healthdata.objects.get(disease = var)
    dict1={'obj':obj,name:'name'}
    subject="Detailed Report"
    msg="Hello sir/madam ," + name + " \nAcording to Your age and Health issuues ,\n Here are some instructions for u\n"
    message= render_to_string('mail.html',{
                    'obj':obj,})
    from_email = settings.EMAIL_HOST_USER
    to_list = [email]
    send_mail(subject,msg,from_email, to_list,html_message=message, fail_silently=True)
    return render(request,'report.html',dict1)

    

