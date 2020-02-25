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
