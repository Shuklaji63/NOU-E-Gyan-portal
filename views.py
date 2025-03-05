from django.shortcuts import render,redirect,HttpResponse
from datetime import date
from .models import registration
from django.contrib import messages
from .models import Login
from .models import Usm
from .models import Complaints
from .models import Feedbacks
from .models import lecture
from .models import assignment
from .models import Enquiry
from .models import noti
from django.core.mail import send_mail
from django.utils import timezone
from django.views.decorators.cache import cache_control
# Create your views here.
#================================All Method For templates===============================
def layout(request):
    return render(request,'layout.html')

def home(request):
    return render(request,'home.html')

def courses(request):
    return render(request,'courses.html')

def study(request):
    return render(request,'study.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'homelogin.html')

def Regi(request):
    return render(request,'rigistration.html')

def about(request):
    return render(request,'about.html')

def studentlayout(request):
    return render(request,'studentlayout.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studenthome(request):
    if 'userid' in request.session:
        return render(request,'studenthome.html')
    else:
        return redirect('homelogin')

def adminlogin(request):
    allstudent=registration.objects.count()
    return render(request,'adminlogin.html',{'allstudent':allstudent})

def adminlayout(request):

    return render(request,'adminlayout.html')   

def usersdata(request):
    show=registration.objects.all()
    return render(request,'usersdata.html',{'Show':show})

def manageuser(request):
    ab=registration.objects.all()
    bs=registration.objects.count()
    return render(request,'showdata.html',{'show':ab,'bs':bs})

def delete(request,enrollment):
    a=registration.objects.get(id=enrollment)
    a.delete()
    return redirect('usersdata')

def updateprofile(request):
        user_email = request.session.get('userid')
        user1=registration.objects.filter(email=user_email).first()
     
       
        co = {
            'uee': user1
          }
        return render(request,'updateprofile.html',co)

def viewstudy(request):
    papa=Usm.objects.all()
    return render(request,'viewstudy.html',{'papa':papa})

def viewlecture(request):
    lect=lecture.objects.all()
    return render(request,'viewlecture.html',{'lect':lect})

def viewassignment(request):
    assi=assignment.objects.all()
    return render(request,'viewassignment.html',{'assi':assi})

def complaint(request):
    sh=registration.objects.all()
    return render(request,'complaint.html',{'S':sh})

def feedback(request):
    fd=Feedbacks.objects.all()
    return render(request,'feedback.html',{'fd':fd})

def uploadstudy(request):
    uploadstudy=Usm.objects.all()
    return render(request,'uploadstudy.html',{'uppapa':uploadstudy})

def uploadassignments(request):
    return render(request,'uploadassignments.html')

def uploadlecture(request):
    return render(request,'uploadlecture.html')

def enquiry(request):
    return render(request,'enquiry.html')

def viewfeedback(request):
    feedsh=Feedbacks.objects.all()
    
    return render(request,'viewfeedback.html',{'F':feedsh})

def notification(request):
    return render(request,'notification.html')

def viewcomplaint(request):
    viewcom=Complaints.objects.all()
    return render(request,'viewcomplaint.html',{'vc':viewcom})


#================================All Method For templates===============================
#================================All save Method ===============================
def save(request):
    enrollment=request.POST['enrollment']
    name=request.POST['name']
    fname=request.POST['fname']
    mname=request.POST['mname']
    gender=request.POST['gender']
    address=request.POST['address']
    course=request.POST['course']
    branch=request.POST['branch']
    year=request.POST['year']
    mobile=request.POST['mobile']
    email=request.POST['email']
    password=request.POST['password']
    usertype='student'
    status='N'
    a=registration(enrollment=enrollment,name=name,fname=fname,mname=mname,gender=gender,address=address,course=course,branch=branch,year=year,mobile=mobile,email=email,password=password)
    b=Login(userid=email,password=password,usertype=usertype,status=status)
    a.save()
    b.save()
    messages.success(request,'Your data is successfully stored')
    return render(request,'rigistration.html')

def save_view(request):
    if request.method == 'POST':
        # Extract form data
        enrollment = request.POST.get('enrollment')
        name = request.POST.get('name')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        usertype='student'
        status='N'
        a=registration(enrollment=enrollment,name=name,fname=fname,mname=mname,gender=gender,address=address,course=course,branch=branch,year=year,mobile=mobile,email=email,password=password)
        b=Login(userid=email,password=password,usertype=usertype,status=status)
        a.save()
        b.save()
    
        # Prepare email content
        subject = 'Registration Confirmation'
        message = f'''
        Thank you Your Are Successfuly Register Nou Egyan Protal
        Your Userid And Password This 
        Userid: {email}
        Password: {password}
        '''
        from_email = 'ashishshukla0866@gamil.com'
        recipient_list = [email]

        # Send email
        send_mail(subject, message, from_email, recipient_list)

        # Add success message and redirect
        messages.success(request, 'Registration successful! Please check your email for confirmation.')
    #    messages.success(request,'Your data is successfully stored')
        return render(request,'rigistration.html') # Replace with your success URL

 
    return render(request,'rigistration.html')


def logcode(request):   
    if request.method=="POST":
       userid=request.POST['userid']
       password=request.POST['password']
       usertype=request.POST['usertype']
       ad=Login.objects.filter(userid=userid,password=password).first()
       if ad:
           if ad.usertype=="student" and usertype=="student":
               request.session['userid']=userid
               return redirect('studenthome')
           elif ad.usertype=="admin" and usertype=="admin":
               return redirect('adminlayout')  
           else:
               messages.success(request,'Invalid User')
               return redirect('homelogin')
       else:
           messages.success(request,'Invalid User')
           return render(request,'homelogin.html')
       


def usmsave(request):
    program = request.POST['program']
    Branch = request.POST['Branch']
    Year = request.POST['Year']
    subject = request.POST['subject']
    file_name = request.POST['file_name']
    new_file = request.FILES['new_file']
    sv = Usm(program=program,Branch=Branch,Year=Year,subject=subject,file_name=file_name,new_file=new_file)
    sv.save()
    messages.success(request,'Study Material Successfully Save')
    return redirect('uploadstudy')

def Complaintsave(request,id):

    sg=registration.objects.get(pk=id)
    Subject=request.POST['Subject']
    comp=request.POST['comp']
    status='Pending'
    reqdate=date.today()
    v=Complaints(name=sg.name,program=sg.course,branch=sg.branch,contactno=sg.mobile,email=sg.email,Subject=Subject,comp=comp,status=status,reqdate=reqdate)
    v.save()
    return redirect('viewcomplaint')


def feedsave(request):
    if request.method == 'POST':
        
        subject = request.POST.get('Subject')
        feedback = request.POST.get('feed')

        user_email = request.session.get('userid')
        
        
        user = registration.objects.filter(email=user_email).first()

        if user:
            # Save feedback
            Feedbacks.objects.create(
                name=user.name,
                program=user.course,
                branch=user.branch,
                contactno=user.mobile,
                email=user.email,
                Subject=subject,
                feed=feedback,
                status='Pending',
                reqdate=timezone.now()  # Use timezone.now() for current time
            )
            messages.success(request, 'Feedback submitted successfully.')
        else:
            messages.error(request, 'User registration not found.')

        return redirect('feedback')
    
  
    return redirect('feedback')
def lecturesave(request):
    program = request.POST['program']
    Branch = request.POST['Branch']
    Year = request.POST['Year']
    subject = request.POST['subject']
    file_name = request.POST['file_name']
    link = request.POST['link']
    pt = lecture(program=program,Branch=Branch,Year=Year,subject=subject,file_name=file_name,link=link)
    pt.save()
    messages.success(request,'Links Uploaded Successfully')
    return redirect('uploadlecture')

def assisave(request):
    program = request.POST['program']
    Branch = request.POST['Branch']
    Year = request.POST['Year']
    subject = request.POST['subject']
    file_name = request.POST['file_name']
    new_file = request.FILES['new_file']
    sv = assignment(program=program,Branch=Branch,Year=Year,subject=subject,file_name=file_name,new_file=new_file)
    sv.save()
    messages.success(request,'Assignments uploaded')
    return redirect('uploadassignments')


def enqsave(request):
    name=request.POST['name']
    contactno=request.POST['contactno']
    email=request.POST['email']
    enq=request.POST['enq']
    enqdate=date.today()
    ens=Enquiry(name=name,contactno=contactno,email=email,enq=enq,enqdate=enqdate)
    ens.save()
    messages.success(request,'Enqury is Save ')
    return redirect('contact')
 
def notisave(request):
    notim=request.POST['notim']
    notidate=date.today ()
    ns=noti(notim=notim,notidate=notidate)
    ns.save()
    return redirect('notification')

def updateform(request):
    if request.method=='POST':
        enrollment=request.POST['enrollment']
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        gender=request.POST['gender']
        address=request.POST['address']
        course=request.POST['course']
        branch=request.POST['branch']
        year=request.POST['year']
        mobile=request.POST['mobile']
        email=request.POST['email']
        password=request.POST['password']
   
    a=registration(enrollment=enrollment,name=name,fname=fname,mname=mname,gender=gender,address=address,course=course,branch=branch,year=year,mobile=mobile,email=email,password=password)
    a.save()
    return redirect('showdata')


#================================All save Method ===============================
#================================All delete Method===============================

def deleteUsm(request,id):
    usd=Usm.objects.get(pk=id)
    usd.delete()
    return redirect('uploadstudy')
def deleteuser(request,id):
    duser=registration.objects.get(pk=id)
    duser.delete()
    return redirect('showdata')
#================================All delete Method===============================
#================================All UpdateMethod===============================

def updateuser(request,id):
    qw=registration.objects.get(pk=id)
    return render(request, 'updateuser.html',{'qw':qw})
#================================All UpdateMethod===============================

       
def logout(request):
    request.session.flush()
    return redirect('home')

def updatepro(request):
        user_email = request.session.get('userid')
        user=registration.objects.filter(email=user_email).first()
     
       
        con = {
            'ue': user
          }
       

        return render(request,'updatepro.html',con)
      
def upsave(request):
    if request.method == 'POST':
        user_email = request.session.get('userid')
        user = registration.objects.filter(email=user_email).first()

        if user:
            user.enrollment = request.POST['enrollment']
            user.name = request.POST['name']
            user.fname = request.POST['fname']
            user.mname = request.POST['mname']
            user.gender = request.POST['gender']
            user.address = request.POST['address']
            user.course = request.POST['course']
            user.branch = request.POST['branch']
            user.year = request.POST['year']
            user.mobile = request.POST['mobile']
            user.email = request.POST['email']
            user.password = request.POST['password']

            if 'New_file' in request.FILES:
                user.New_file = request.FILES['New_file']

            user.save()
            return redirect('updateprofile')
        else:
           
             return redirect('updateprofile')