from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import User, Doctor, Patient,Appointment
# from .models import Doctor,Patient,
# Create your views here.

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def welcome(request):
    return render(request,'welcome.html')
def waitinglist(request):
    return render(request,'waitinglist.html')
def loging(request):
    if request.method == "POST":
       username = request.POST['username']
       password = request.POST['pwd']
       userpass = authenticate(request,username=username, password=password)
       if userpass is not None and userpass.is_superuser==1:
           return redirect('admin_home')
       elif userpass is not None and userpass.is_staff==1:
           login(request, userpass)
           request.session['doctor_id']=userpass.id
           return redirect('doctor_home')
       elif userpass is not None and userpass.is_active==1:
           login(request, userpass)
           request.session['patient_id']=userpass.id
           return redirect('patient_home')
       else:
            return render(request,'waitinglist.html')
    else:
        return render(request,'login.html')
        
    
def Logout(request):
    logout(request)
    return redirect('home')

# admin module functions

def admin_home(request):
    #for both table in admin dashboard
    doctors=Doctor.objects.all().order_by('-id')
    patients=Patient.objects.all().order_by('-id')

    #for three cards
    doctorcount=Doctor.objects.all().filter(status=True).count()
    pendingdoctorcount=Doctor.objects.all().filter(status=False).count()
    
    patientcount=Patient.objects.all().filter(status=True).count()
    pendingpatientcount=Patient.objects.all().filter(status=False).count()

    appointmentcount=Appointment.objects.all().filter(status=True).count()
    pendingappointmentcount=Appointment.objects.all().filter(status=False).count()

    
    return render(request,'admin_home.html',{'doctorcount':doctorcount,'patientcount':patientcount,'doctors':doctors,
                                             'patients':patients, 'appointmentcount':appointmentcount, 'pendingappointmentcount':pendingappointmentcount,
                                             'pendingdoctorcount': pendingdoctorcount, 'pendingpatientcount':pendingpatientcount})

def admin_doctor(request):
    return render(request,'admin_doctor.html')

def admin_view_doctor(request):
    doctors=Doctor.objects.all().filter(status=True)
    return render(request,'admin_view_doctor.html',{'doctors':doctors})

def admin_add_doctor(request):
    if request.method =='POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        un = request.POST['username']
        pwd = request.POST['password']
        dept = request.POST['dept']
        address = request.POST['address']
        phn = request.POST['phone']
        images=request.FILES['pic']

        a = User.objects.create_user(first_name=fn, last_name=ln, username=un, password=pwd, usertype='doctor',is_staff=True,is_active=True)
        a.save()
        z = Doctor.objects.create(doctor_id=a, address=address, phone=phn, department=dept, image=images, 
                                  status='True')
        z.save()
        return HttpResponseRedirect('admin_view_doctor')
    else:
        return render(request,'admin_add_doctor.html')
    
def admin_edit_doctor(request,id):
    doc_info = Doctor.objects.get(id=id)
    return render(request,'admin_update_doctor.html',{'edit':doc_info})

def admin_update_doctor(request,id):
    if request.method =='POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        un = request.POST['username']
        address = request.POST['address']
        phn = request.POST['phone']
        

        y = Doctor.objects.get(id=id)
        y.address=address
        y.phone=phn
        y.save()

        user_obj =y.doctor_id
        user_obj.first_name = fn
        user_obj.last_name = ln
        user_obj.username = un
        user_obj.save()
        return redirect('admin_view_doctor')
    else:
        return render(request,'admin_update_doctor.html')

def admin_delete_doctor(request,id):
    doc = Doctor.objects.get(id=id)
    doc.doctor_id.delete()
    return redirect('admin_view_doctor')
  
def admin_view_doctor_Specialisation(request):
    doctors=Doctor.objects.all().filter(status=True)
    return render(request,'admin_view_doctor_Specialisation.html',{'doctors':doctors})

def admin_patient(request):
    return render(request,'admin_patient.html')

def admin_add_patient(request):
    doctors=Doctor.objects.all().filter(status=True)
    if request.method =='POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        un = request.POST['username']
        pwd = request.POST['password']
        symptom= request.POST['symptom']
        address = request.POST['address']
        assignedDoctor = request.POST['assignedDoctor']
        phn = request.POST['phone']
        images=request.FILES['pic']
       

        a = User.objects.create_user(first_name=fn, last_name=ln, username=un, password=pwd, usertype='patient',is_staff=False,is_active=True)
        a.save()
        z = Patient.objects.create(patient_id=a, address=address, phone=phn, symptoms=symptom, image=images, 
                                   status='True',assignedDoctorID=assignedDoctor)
        z.save()
        return HttpResponseRedirect('admin_view_patient')
   
    else:
        return render(request,'admin_add_patient.html',{'doctors':doctors})

def admin_view_patient(request):
    patients=Patient.objects.all().filter(status=True)
    doc=Doctor.objects.all().filter(status=True)
    return render(request,'admin_view_patient.html',{'patients':patients,'doc':doc})

def admin_delete_patient(request,id):
    pat = Patient.objects.get(id=id)
    pat.patient_id.delete()
    return redirect('admin_view_patient')

def admin_edit_patient(request,id):
    pat_info = Patient.objects.get(id=id)
    return render(request,'admin_update_patient.html',{'edit':pat_info})

def admin_update_patient(request,id):
    if request.method =='POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        un = request.POST['username']
        address = request.POST['address']
        phn = request.POST['phone']
        symptoms = request.POST['symptom']
        
        y = Patient.objects.get(id=id)
        y.address=address
        y.phone=phn
        y.symptoms=symptoms
        y.save()

        user_obj =y.patient_id
        user_obj.first_name = fn
        user_obj.last_name = ln
        user_obj.username = un
        user_obj.save()
        return redirect('admin_view_patient')
    else:
        return render(request,'admin_update_patient.html')
    
def admin_appointment(request):
    return render(request,'admin_appointment.html')

def admin_add_appointment(request):
    patients=Patient.objects.all().filter(status=True)
    doctors=Doctor.objects.all().filter(status=True)

    if request.method=='POST':
        Description=request.POST['Description']
        assignedDoctor=request.POST['assignedDoctor']
        assignedpatient=request.POST['assignedpatient']
        b=Appointment.objects.create(description=Description, patientID=assignedpatient, doctorID=assignedDoctor,status=True)
        b.save()
        return HttpResponseRedirect('admin_view_appointment')
    else:
        return render(request,'admin_add_appointment.html',{'patients':patients,'doctors':doctors })

def admin_view_appointment(request):
    appointments=Appointment.objects.all().filter(status=True)
    patients=Patient.objects.all().filter(status=True)
    doc=Doctor.objects.all().filter(status=True)
    return render(request,'admin_view_appointment.html', {'appointments':appointments,'patients':patients,'doc':doc})


# doctor module functions

def doctor_home(request):
    doctor_id =request.session.get('doctor_id', None)
    if doctor_id is not None:
        patientcount=Patient.objects.all().filter(status=True,assignedDoctorID=request.user.id).count()
        appointmentcount=Appointment.objects.all().filter(status=True,doctorID=request.user.id).count()
        patientslist=Patient.objects.filter(assignedDoctorID=doctor_id)
        appointmentlist=Appointment.objects.filter(doctorID=doctor_id)
        z=zip(patientslist,appointmentlist)
        # doctor=Doctor.objects.get(doctor_id=request.user.id) #for profile picture of doctor in sidebar
        return render(request,'doctor_home.html',{'z':z, 'patientcount':patientcount,'appointmentcount':appointmentcount})
    else:
        return HttpResponse("Invalid session data. Please log in again.")

def doctor_patient(request):
    doctor_id =request.session.get('doctor_id', None)
    if doctor_id is not None:
        return render(request,'doctor_patient.html')

def doctor_view_patient(request):
    doctor_id =request.session.get('doctor_id', None)
    if doctor_id is not None:
        patientslist=Patient.objects.filter(assignedDoctorID=doctor_id)
        doc=Doctor.objects.all().filter(status=True)
        return render(request,'doctor_view_patient.html', {'patientslist':patientslist, 'doc':doc})

def doctor_appointment(request):
    doctor_id =request.session.get('doctor_id', None)
    if doctor_id is not None:
        return render(request,'doctor_appointment.html')

def doctor_view_appointment(request):
    doctor_id =request.session.get('doctor_id', None)
    if doctor_id is not None:
        patientslist=Patient.objects.filter(assignedDoctorID=doctor_id)
        appointmentlist=Appointment.objects.filter(doctorID=doctor_id)
        z=zip(patientslist,appointmentlist)
        return render(request,'doctor_view_appointment.html',{'z':z})

def doctor_delete_appointment(request):
    doctor_id =request.session.get('doctor_id', None)
    if doctor_id is not None:
        patientslist=Patient.objects.filter(assignedDoctorID=doctor_id)
        appointmentlist=Appointment.objects.filter(doctorID=doctor_id)
        z=zip(patientslist,appointmentlist)
        return render(request,'doctor_delete_appointment.html',{'z':z})
    
def delete_appointment(request,id):
    d=Appointment.objects.get(id=id)
    d.delete()
    return redirect('doctor_delete_appointment')

def doctor_signup(request):
    if request.method =='POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        un = request.POST['username']
        pwd = request.POST['password']
        dept = request.POST['dept']
        address = request.POST['address']
        phn = request.POST['phone']
        images=request.FILES['pic']

        a = User.objects.create_user(first_name=fn, last_name=ln, username=un, password=pwd, usertype='doctor',is_staff=False,is_active=False)
        a.save()
        z = Doctor.objects.create(doctor_id=a, address=address, phone=phn, department=dept, image=images, 
                                  status='False')
        z.save()
        return HttpResponseRedirect('welcome')
    else:
        return render(request,'doctor_signup.html')
    
# patient module functions

def patient_home(request):
    return render(request,'patient_home.html')
