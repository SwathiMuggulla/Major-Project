from django.shortcuts import render,redirect
from usersapp.models import *
from mainapp.models import *
from django.contrib import messages
import socket
import pathlib
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator


# Create your views here.
def workstation_index(request):
    return render(request,'workstation/index.html')

def workstation_analysisreport(request):

    files=AttackerModel.objects.filter(att_status="attacked")

    fPosts=AttackerModel.objects.all().order_by("-file_enc_id")
    paginator = Paginator(fPosts,4)

    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    # data=FileModel.objects.all()


    return render(request,'workstation/workstation-analysisreport.html',{'file':files,'post':post})

def workstation_dashboard(request):
    users=UserModel.objects.all().count()
    files=FileModel.objects.all().count()
    attackers=AttackerModel.objects.all().count()
    return render(request,'workstation/workstation-dashboard.html',{'x':files,'i':users,'o':attackers})

def workstation_dynamicanalysis(request):
    # user_id=request.session['user_id']
    # user=UserModel.objects.get(user_id=user_id)
    hostname=socket.gethostname()
    IPadress=socket.gethostbyname(hostname)
    print(IPadress)
    # user_ip=IPadress
    fPosts=FileModel.objects.filter(file_status='marked as ransomware').order_by("-file_id")
    paginator = Paginator(fPosts, 4)

    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
   
    # userimage=UserModel.objects.get(user_image=userimage)
    # userfile=FileModel.objects.filter(user=userimage)
    # print(userfile)


    return render(request,'workstation/workstation-dynamicanalysis.html',{'post':post})

def workstation_staticanalysis(request):
    
    
    hostname=socket.gethostname()
    IPadress=socket.gethostbyname(hostname)
    print(IPadress)
    # IPadress=x
    fPosts=FileModel.objects.filter(file_status='verification in process').order_by("-file_id")
    paginator = Paginator(fPosts, 4)

    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
  
    # if request.method=="POST":
    #     ip=request.POST.get(user_ip)
    

    return render(request,'workstation/workstation-staticanalysis.html',{'post':post})

def markedassafe(request,id):
    file= FileModel.objects.get(file_id=id)
    file.file_status = "marked as safe"
    file.save()
        # messages.success(request, 'Alloted Successfully')
    return redirect ('workstation_safefile')

def markedasransomware(request,id):
    file= FileModel.objects.get(file_id=id)
    file.file_status = "marked as ransomware"
    file.save()
        # messages.success(request, 'Alloted Successfully')
    return redirect ('workstation_dynamicanalysis')


def workstation_ransomwarefile(request):
    fPosts=FileModel.objects.filter(file_status='ransomware').order_by("-file_id")
    paginator = Paginator(fPosts, 4)

    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    return render(request,'workstation/workstation-ransomwarefile.html',{'post':post})


def workstation_safefile(request):
    
    fPosts=FileModel.objects.filter(file_status='marked as safe').order_by("-file_id")
    paginator = Paginator(fPosts, 4)

    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
   
    return render(request,'workstation/workstation-safefile.html',{'post':post})


def execute(request,id):
    file=FileModel.objects.get(file_id=id)
    filename = file.file_type
    filepath=file.file_path

    if "C:" in filepath or '.exe' in filename or '.dll' in filename :
        # print('workinggggggggggggggggggggg')
        file.file_status='ransomware'
        file.save()
        messages.success(request,'file found ransomware')
        return redirect('workstation_ransomwarefile')
    else:
        file.file_status='marked as safe'
        file.save()
        messages.error(request,'File is safe')
        return redirect('workstation_safefile')

       

    return redirect('workstation_ransomwarefile')

# def execute(request):


