from django.shortcuts import render,redirect,HttpResponse
from usersapp.models import*
from mainapp.models import*
import pathlib
from django.core.files.storage import FileSystemStorage
import socket
import platform
import os
from django.contrib import messages
# from django_user_agents.utils import get_user_agent
from django.core.paginator import Paginator

# Create your views here.
def main_home(request):
    return render(request,'main/main-home.html')

def main_about(request):
    return render(request,'main/main-about.html')

def main_contact(request):
    return render(request,'main/main-contact.html')

def main_features(request):
    return render(request,'main/main-features.html')

def main_portfolio(request):
    return render(request,'main/main-portfolio.html')

def main_pricing(request):
    return render(request,'main/main-pricing.html')

def main_services(request):
    return render(request,'main/main-services.html')

def main_testimonials(request):
    return render(request,'main/main-testimonials.html')

def attacker(request):

    
    file=FileModel.objects.exclude(attack_status='Attacked')
    #  file=AttackerModel.objects.create(username='user_name',filetype='file_type',filename='file_name')

    fPosts=AttackerModel.objects.order_by("file_enc_id")
    paginator = Paginator(fPosts, 4)

    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
  

    return render(request,'main/attacker.html',{'file': file,'post':post})


    
def main_workstationlogin(request):
   
    if request.method=='POST':
        
        name=request.POST.get('name')
        password=request.POST.get('password')
        print(name,password)

        if name =="workstation" and password == "workstation":
            # print('suceeeee')
            messages.success(request,"workstation successfully login")
            return redirect('workstation_dashboard')
        else:
            messages.error(request,"invalid credentials")
            return redirect('main_workstationlogin')
       


    return render(request,'main/main-workstationlogin.html')




def enyc(request,id):

    # user_agent=get_user_agent(request)
    # if user_agent.is_mobile:
    #     # return HttpResponse('user using mobile')
    #     print('mobile')
    # elif user_agent.is_pc:
    #     vi=request.META['HTTP_USER_AGENT']
    #     print(vi,'ggggg')
    #     # return HttpResponse('user using pc')
    
    #     # f_type=file.name
    #     # ab=pathlib.Path(f'{f_type}').suffix
    #     # fss=FileSystemStorage()
    #     # fname=fss.save('media/'+name,file)
    #     # url=fss.url(fname)
    
  
    hostname=socket.gethostname()
    IPadress=socket.gethostbyname(hostname)
    pc = socket.gethostname()
    print(pc,IPadress)
    filed = FileModel.objects.get(pk=id)
    filed.attack_status = 'Attacked'
    filed.save()
    platform.node()
    x=os.environ['COMPUTERNAME']
    att=AttackerModel.objects.create(file_enc_id=id,att_status="attacked",att_ip=IPadress,att_pc=x)
    
    messages.success(request,"File got encrypted")
    # print(url,IPadress)
       
    
    return redirect('attacker')