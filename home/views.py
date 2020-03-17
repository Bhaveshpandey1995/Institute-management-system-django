from django.shortcuts import render

# Create your views here.

def IndexView(request):

    return render(request, 'index.html')

def AboutView(request):

    return render(request, 'newtemplate/about.html')

def ContactView(request):

    return render(request, 'newtemplate/contact.html')

def CoursePhdView(request):

    return render(request, 'newtemplate/courses/phd.html')

def CourseUgView(request):

    return render(request, 'newtemplate/courses/ug.html')

def CoursePgView(request):

    return render(request, 'newtemplate/courses/pg.html')

def AdmissionUgView(request):

    return render(request, 'newtemplate/admission/adug.html')

def AdmissionPgView(request):

    return render(request, 'newtemplate/admission/adpg.html')

def AdmissionPhdView(request):

    return render(request, 'newtemplate/admission/adphd.html')

def CivilView(request):

    return render(request, 'newtemplate/department/civil.html')

def MechanicalView(request):

    return render(request, 'newtemplate/department/mechanical.html')

def ElectricalView(request):

    return render(request, 'newtemplate/department/Electrical.html')

def ElectronicsView(request):

    return render(request, 'newtemplate/department/Electronics.html')

def ComputerView(request):

    return render(request, 'newtemplate/department/computer.html')

def PhysicsView(request):

    return render(request, 'newtemplate/department/physics.html')

def HumanView(request):

    return render(request, 'newtemplate/department/humanities.html')

def ChemicalView(request):

    return render(request, 'newtemplate/department/Chemical.html')

def ItcaView(request):

    return render(request, 'newtemplate/department/itca.html')

def EnvironmentView(request):

    return render(request, 'newtemplate/department/environment.html')

def MathView(request):

    return render(request, 'newtemplate/department/math.html')

def ItrcView(request):

    return render(request, 'newtemplate/facilities/itrc.html')

def LibraryView(request):

    return render(request, 'newtemplate/facilities/Library.html')

def HospitalView(request):

    return render(request, 'newtemplate/facilities/hospital.html')

def HostelView(request):

    return render(request, 'newtemplate/facilities/hostel.html')

def GuestView(request):

    return render(request, 'newtemplate/facilities/guest.html')

def PrimaryView(request):

    return render(request, 'newtemplate/facilities/primary.html')

def PostView(request):

    return render(request, 'newtemplate/facilities/post.html')

def SbiView(request):

    return render(request, 'newtemplate/facilities/sbi.html')

def CanteenView(request):

    return render(request, 'newtemplate/facilities/canteen.html')

def TransportView(request):

    return render(request, 'newtemplate/facilities/transport.html')

def FeeView(request):

    return render(request, 'newtemplate/feestruc.html')

def SyllabusView(request):

    return render(request, 'newtemplate/syllabus.html')

def FacPhyView(request):

    return render(request, 'newtemplate/faculty/physics.html')

def FacCivilView(request):

    return render(request, 'newtemplate/faculty/civil.html')

def FacCompView(request):

    return render(request, 'newtemplate/faculty/computer.html')

def FacElecView(request):

    return render(request, 'newtemplate/faculty/electrical.html')

def FacElectroView(request):

    return render(request, 'newtemplate/faculty/electronics.html')

def FacMechView(request):

    return render(request, 'newtemplate/faculty/mechanical.html')

def FacHumanView(request):

    return render(request, 'newtemplate/faculty/human.html')

def FacChemView(request):

    return render(request, 'newtemplate/faculty/chemical.html')

def FacItcaView(request):

    return render(request, 'newtemplate/faculty/itca.html')

def FacChemistView(request):

    return render(request, 'newtemplate/faculty/chemistry.html')

def FacMathView(request):

    return render(request, 'newtemplate/faculty/math.html')

def MissionView(request):

    return render(request, 'newtemplate/mission.html')

def VisionView(request):

    return render(request, 'newtemplate/vision.html')


