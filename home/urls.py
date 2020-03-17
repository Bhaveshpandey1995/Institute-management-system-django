from django.urls import path,include
from .views import AboutView, ContactView , CoursePhdView , CourseUgView , CoursePgView , AdmissionPhdView , AdmissionPgView , AdmissionUgView , CivilView
from .views import MechanicalView , ElectricalView , ElectronicsView , ComputerView , PhysicsView , HumanView , ChemicalView
from .views import ItcaView , EnvironmentView , MathView , ItrcView , LibraryView , HospitalView , HostelView
from .views import GuestView , PrimaryView , PostView , SbiView , CanteenView , TransportView , FeeView , SyllabusView
from .views import FacPhyView , FacCivilView , FacCompView , FacElecView , FacElectroView , FacMechView , FacHumanView , FacChemView
from .views import FacItcaView , FacChemistView , FacMathView , MissionView , VisionView

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
    path('itrc/', ItrcView, name='itrc'),
    path('library/', LibraryView, name='library'),
    path('hospital/', HospitalView, name='hospital'),
    path('hostel/', HostelView, name='hostel'),
    path('guest/', GuestView, name='guest'),
    path('primary/', PrimaryView, name='primary'),
    path('post/', PostView, name='post'),
    path('sbi/', SbiView, name='sbi'),
    path('canteen/', CanteenView, name='canteen'),
    path('transport/', TransportView, name='transport'),
    path('fee/', FeeView, name='fee'),
    path('syllabus/', SyllabusView, name='syllabus'),
    path('facphy/', FacPhyView, name='facphy'),
    path('faccivil/', FacCivilView, name='faccivil'),
    path('faccomp/', FacCompView, name='faccomp'),    
    path('facelec/', FacElecView, name='facelec'),    
    path('facelectro/', FacElectroView, name='facelectro'),    
    path('facmech/', FacMechView, name='facmech'),    
    path('fachuman/', FacHumanView, name='fachuman'),    
    path('facchem/', FacChemView, name='facchem'),    
    path('facitca/', FacItcaView, name='facitca'),    
    path('facchemist/', FacChemistView, name='facchemist'),    
    path('facmath/', FacMathView, name='facmath'),    
    path('mission/', MissionView, name='mission'),    
    path('vission/', VisionView, name='vision'),    
]