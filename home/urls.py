from django.urls import path,include
from .views import AboutView, ContactView , CoursePhdView , CourseUgView , CoursePgView , AdmissionPhdView , AdmissionPgView , AdmissionUgView , CivilView
from .views import MechanicalView , ElectricalView , ElectronicsView , ComputerView , PhysicsView , HumanView , ChemicalView
from .views import ItcaView , EnvironmentView , MathView

app_name = 'home'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('about/', AboutView, name='about'),
    path('contact/', ContactView, name='contact'),
    path('coursephd/', CoursePhdView, name='phd'),
    path('courseug/', CourseUgView, name='ug'),
    path('coursepg/', CoursePgView, name='pg'),
    path('admissionug/', AdmissionUgView, name='adug'),
    path('admissionpg/', AdmissionPgView, name='adpg'),
    path('admissionphd/', AdmissionPhdView, name='adphd'),
    path('civil/', CivilView, name='civil'),
    path('mechanical/', MechanicalView, name='mechanical'),
    path('electrical/', ElectricalView, name='electrical'),
    path('electronics/', ElectronicsView, name='electronics'),
    path('computer/', ComputerView, name='computer'),
    path('physics/', PhysicsView, name='physics'),
    path('human/', HumanView, name='human'),
    path('chemical/', ChemicalView, name='chemical'),
    path('itca/', ItcaView, name='itca'),
    path('environment/', EnvironmentView, name='environment'),
    path('math/', MathView, name='math'),
]