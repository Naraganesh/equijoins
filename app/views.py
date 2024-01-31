from django.shortcuts import render

# Create your views here.
from app.models import *
def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all() 
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024) 
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__gt=2500) 
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__lt=2500) 
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=20) 
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=40) 

    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING') 
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='SALES')   
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='MANAGER')   


    EMPOBJECTS=Emp.objects.select_related('deptno').all() 
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='DALLAS') 
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='NEW YORK')  

    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True) 
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False) 

    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True) 
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False) 
  
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[2:5:] 
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[2:8:] 
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[:5:] 
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[2:8:-1] 
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[0:5:-2]

    

    
    
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)
