from django.shortcuts import render
from django.http import HttpResponse
from .forms import Uploader, Contactussubmit
from .models import Uploaderform,contactusform


# Create your views here.

def homeview(request,*args,**kwargs):
   # return HttpResponse("<h2>Welcome to the store</h3>")
    form = Uploader(request.POST or None)

    if form.is_valid():
        form.save()

    return render(request,'home.html',{"form":form})

def aboutview(request,*args,**kwargs):
    #return HttpResponse("<h2>About us</h3>")
    return render(request,'aboutus.html',{})



def contactview(request,*args,**kwargs):
    #return HttpResponse("<h2>Contact us</h3>")
    form =  Contactussubmit(request.POST or None)

    if form.is_valid():
        form.save()
    return render(request,'contactus.html',{"form":form})


def serviceview(request,*args,**kwargs):
    #return HttpResponse("<h1> socialpages</h3>")
    return render(request,'services.html',{})


def upload_file(request):
    """
    Uploads the file to the database and renders the status of the upload.
    """
    email = request.POST.get('email', None)
    mobile = request.POST.get('mobile', None)
    fname = request.FILES['file']
    contents = fname.read()
    fname = str(fname)
    ts_as_id = datetime.now().strftime("%Y%m%d%H%M%S%f")
    obj_uploader = Uploader(TIMESTAMP_AS_ID=ts_as_id, EMAIL=email, PHONE=mobile, FILENAME=fname, FILE=contents)
    obj_uploader.save()
    updr = Uploader.objects.filter(TIMESTAMP_AS_ID=ts_as_id)
    status = " Uploaded Successfully" if len(updr) > 0 else " Upload Failed"
    return render(request, 'back_to_upload.html', {'filename': fname, 'status': status} )


