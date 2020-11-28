from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
import datetime

from facebookapp.models import user
from facebookapp.models import bussinesspage

from django.contrib import messages


def businesspage(request):
    return render(request,'businesspage.html')

def home(request):
    return render(request,'index.html')
def register(request):
 try:

    if request.method == 'POST':
        name1 = request.POST['name']
        lastname1 = request.POST['lastname']

        email1 = request.POST['email']
        password1 = request.POST['password']
        confirmpassword1 = request.POST['confirmpassword']
        c = request.POST['date']
        g = request.POST['gender']

        if password1==confirmpassword1:
            if user.objects.filter(email=email1).exists():
                messages.info(request, 'email taken')
                return redirect('register')

            else:
                print("hello4")

                register1 = user(name=name1, lastname=lastname1, email=email1, password=password1, date=c, gender=g)
                register1.save();


                return redirect('register')


        else:

            messages.info(request, 'Password not matching')
            return redirect('register')


    else:

        return render(request,'index.html')

 except:

             return render(request, 'index.html', {'error': "Please Fill The Form"})


def login(request):
    try:

         if request.method=="POST":
            m=user.objects.get(email=request.POST['email'])


            if m.password==request.POST['passw']:
                request.session['updateuser']=m.name


                return render(request,'businesspage.html',{'name':m.name})

            else:
                return render(request, 'index.html',{'error':"please check the password"})

         else:
             return render(request, 'index.html')
    except:

             return render(request, 'index.html', {'error': "Please Fill The Form"})



def logout(request):
    try:
        del request.session['users_name']
    except KeyError:
        pass
    return  render(request,'index.html')

def business(request):
  try:
    if request.method == 'POST':

        source1 = request.POST['source']
        companyname1= request.POST['companyname']
        name1 = request.POST['name']
        address1 = request.POST['address']
        contactno1 = request.POST['contactno']
        rating1 = request.POST['rating']
        p = request.FILES["picture"]


        register1 = bussinesspage( companyname=companyname1,source=source1,name=name1,address=address1,contactno=contactno1,rating=rating1,data=p)
        register1.save();

        return render(request, 'businesspage.html')
    else:
        return render(request, 'businessregister.html')
  except:

      return render(request, 'businessregister.html', {'error': "Please Fill The Form"})
def businessdetailsupdate(request):
 try:
    a = request.session['updateuser']

    userlist = bussinesspage.objects.filter(name=a)

    if request.method == "POST":


        source1 = request.POST['source']
        name1=request.POST['name']
        companyname1 = request.POST['companyname']
        address1 = request.POST['address']
        contactno1 = request.POST['contactno']
        rating1 = request.POST['rating']


        bussinesspage.objects.filter(name=a).update(name=name1,source=source1,companyname=companyname1, address=address1,contactno=contactno1,rating=rating1)



        return render(request, 'businesspage.html')
    else:
        return render(request, 'profileupdate.html',{'user': userlist})
 except:

      return render(request, 'profileupdate.html', {'error': "Please Fill The Form"})
def updatestatus(request):
 try:
    a=request.session['updateuser']

    userlist = bussinesspage.objects.filter(name=a)

    if request.method == "POST":


        source1 = request.POST['source']
        name1 = request.POST['name']
        address1 = request.POST['address']
        contactno1 = request.POST['contactno']
        rating1 = request.POST['rating']


        bussinesspage.objects.filter(name=a).update(source=source1,name=name1, address=address1,contactno=contactno1,rating=rating1)



        return render(request, 'businesspage.html')
    else:
        return render(request, 'updatestatus.html',{'user': userlist})
 except:

      return render(request, 'updatestatus.html', {'error': "Please Fill The Form"})
def update(request):
    bussinesspage.objects.filter(bid=request.POST['btn']).update(status=1)
    a = request.session['updateuser']
    userlist = bussinesspage.objects.filter(name=a)

    return render(request, 'updatestatus.html', {'user': userlist})

