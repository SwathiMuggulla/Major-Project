from django.shortcuts import render,redirect
from usersapp.models import *
from django.contrib import messages
import pathlib
from django.core.files.storage import FileSystemStorage
import socket
from django.core.paginator import Paginator

def main_userregistration(request):
   

    if request.method=="POST" and request.FILES['image']:
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        dob=request.POST.get('dob')
        contact=request.POST.get('contact')
        city=request.POST.get('city')
        image=request.FILES['image']
        hostname=socket.gethostname()
        IPadress=socket.gethostbyname(hostname)
        print(IPadress,'hhhh')
        print(name,email,password,contact,image,city,dob)

        userregistration=UserModel.objects.create(user_name=name,user_dob=dob,user_email=email,user_password=password,user_contact=contact,user_city=city,user_image=image,user_ip=IPadress)
        # userregistration = UserModel.objects.create(user_name=name,user_city=city,user_email=email,user_password=password,user_dob=dob,user_contact=contact,user_image=image)
        userregistration.save()
        if userregistration:
            messages.success(request,'successfully login')
            return redirect('main_user_login')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('main_userregistration')


    return render(request,'main/main-userregistration.html')


     
def main_user_login(request):
    if request.method == "POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        print(email,password)
        try:
            check = UserModel.objects.get(user_email=email,user_password=password)
            request.session['user_id']=check.user_id
            print(check)
            messages.success(request,'user login successfully')
            return redirect('users_dashboard')
        except:
            messages.info(request,'invalid Credentials')
            return redirect('main_user_login')

    # if main_user_login:
    #     messages.success(request,'successfully login')
    #     return redirect('users/users_dashboard')
    # else:
    #     messages.error(request,'Invalid Credentials')
    #     return redirect('main_user_login')
        

    return render(request,"main/main-user-login.html")
    
# Create your views here.

def users_about(request):
    return render(request,'users/user-about-us.html')


def users_contact(request):
    return render(request,'users/user-contact.html')

def users_features(request):
    return render(request,'users/user-features.html')

def users_index(request):
    return render(request,'users/user-index.html')

def users_portfolio(request):
    return render(request,'users/user-portfolio.html')

def users_services(request):
    return render(request,'users/user-services.html')

def users_testimonials(request):
    return render(request,'users/user-testimonials.html')

def users_dashboard(request):
    users=UserModel.objects.all().count()
    files=FileModel.objects.all().count()

    return render(request,'users/user-dashboard.html',{'i':users,'x':files})

def users_myfile(request):
    user_id=request.session['user_id']
    user=UserModel.objects.get(user_id=user_id)
    userfile=FileModel.objects.filter(user=user_id)
    print(userfile,'data')
    fPosts=FileModel.objects.filter(user=user_id).order_by("file_id")
    paginator = Paginator(fPosts, 4)

    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)


  
    return render(request,'users/user-myfile.html',{'userfile':userfile,'post':post})

def users_myprofile(request):
    user_id=request.session['user_id']
    userprofile=UserModel.objects.get(user_id=user_id)
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        dob=request.POST.get('dob')
        contact=request.POST.get('contact')
        city=request.POST.get('city')
        if len(request.FILES)!=0:
            image=request.FILES['image']
            userprofile.user_name=name
            userprofile.user_email=email
            userprofile.user_password=password
            userprofile.user_dob=dob
            userprofile.user_contact=contact
            userprofile.user_city=city
            userprofile.user_image=image
            userprofile.save()
        
        else:
             userprofile.user_name=name
             userprofile.user_email=email
             userprofile.user_password=password
             userprofile.user_dob=dob
             userprofile.user_contact=contact
             userprofile.user_city=city
             userprofile.save()

        messages.success(request,'Updated Successfully')

        return redirect('users_myprofile')


    return render(request,'users/user-myprofile.html',{'userprofile':userprofile})

def users_uploaddata(request):
    context={}
    if request.method == "POST" and request.FILES['file']:
        name=request.POST.get("name")
        filetype=request.POST.get("filetype")
        file=request.FILES["file"]
        f_type=file.name
        a=pathlib.Path(f'{f_type}').suffix
        fs=FileSystemStorage()
        fname=fs.save('media/'+name,file)
        url=fs.url(fname)
        context['url'] =fs.url(name)
        uploaded_file_path=fs.path(fname)
        
        print(url,uploaded_file_path)

        
        user_id=request.session['user_id']
        user1=UserModel.objects.get(user_id=user_id)
        useruploaddata=FileModel.objects.create(file_name=name,file_type=a,file_upload=file,user=user1,file_path=uploaded_file_path)
        # userregistration = UserModel.objects.create(user_name=name,user_city=city,user_email=email,user_password=password,user_dob=dob,user_contact=contact,user_image=image)
        useruploaddata.save()
        if useruploaddata:
            messages.success(request,'successfully uploaded data')
            return redirect('users_uploaddata')
        else:
            messages.error(request,'Invalid datatype')
            return redirect('users_uploaddata')

    return render(request,'users/user-uploaddata.html',context)

def users_pricing(request):
    return render(request,'users/user-pricing.html')




