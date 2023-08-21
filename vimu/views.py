from django.shortcuts import render,HttpResponse,redirect
from vimu.models import contact1
import time

def index(request):

    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['no']
        subject=request.POST['sub']
        message=request.POST['msg']

        my_form=contact1(first_name=fname,last_name=lname,email_id=email,phone_No=phone,Subject=subject,Message=message)
        my_form.save()

        # return HttpResponse("thank you contacting us")
        data={
            'msg':'thank for contacting us'
        }
        return render(request,'index.html',data)
        sleep(2)
        return redirect('index')

        
    return render(request,'index.html')
# Create your views here.
