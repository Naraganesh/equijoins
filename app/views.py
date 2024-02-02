from django.shortcuts import render 
from django.db.models import Q

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




def selfjoins(request): 
    empmgrobjects=Emp.objects.select_related('mgr').all() 
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='KING')  
    empmgrobjects=Emp.objects.select_related('mgr').filter(deptno=20)

    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__gt=2500) 
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__lt=2000) 
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='BLAKE')  

    empmgrobjects=Emp.objects.select_related('mgr').filter(hiredate__year=2024) 

    empmgrobjects=Emp.objects.select_related('mgr').filter(hiredate__year=2024,sal__lt=2500) 
    empmgrobjects=Emp.objects.select_related('mgr').filter(hiredate__year=2024,sal__gt=2500) 

    empmgrobjects=Emp.objects.select_related('mgr').filter(deptno=20)
    empmgrobjects=Emp.objects.select_related('mgr').filter(deptno=30) 

    empmgrobjects=Emp.objects.select_related('mgr').filter(deptno__dname='ACCOUNTING')
    empmgrobjects=Emp.objects.select_related('mgr').filter(deptno__dname='SALES') 
    empmgrobjects=Emp.objects.select_related('mgr').filter(deptno__dname='RESEARCH')  


    empmgrobjects=Emp.objects.select_related('mgr').filter(comm__isnull=True)  
    empmgrobjects=Emp.objects.select_related('mgr').filter(comm__isnull=False)  

    empmgrobjects=Emp.objects.select_related('mgr').all()[2:5:]  
    empmgrobjects=Emp.objects.select_related('mgr').all()[::] 
    empmgrobjects=Emp.objects.select_related('mgr').all()[::-1]
    empmgrobjects=Emp.objects.select_related('mgr').all()[0::-2] 
    




   

    d={'empmgrobjects':empmgrobjects}
    return render(request,'selfjoins.html',d) 




def emp_mgr_dept(request): 
    emd=Emp.objects.select_related('deptno','mgr').all()  
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH') 
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES') 
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation='DALLAS') 
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE') 
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING') 
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__year=2024) 
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='BLAKE') 
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='MARTIN')  
    emd=Emp.objects.select_related('deptno','mgr').all()  
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='RESEARCH')|Q( mgr__ename='JOHNS')) 
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__deptno=20)   
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dlocation='DALLAS') |Q(mgr__ename='JOHNS') ) 
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__deptno=20)  
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__deptno=20)  
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__hiredate__year=2024)  
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__hiredate__year=2024,sal__gt=2000)  
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__hiredate__year=2024,sal__lt=3000)   
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__comm__isnull=True)  
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__comm__isnull=False)  
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__isnull=True)   
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(mgr__hiredate__year=2024) |Q(deptno__dname='SALES') ) 
    emd=Emp.objects.select_related('deptno','mgr').all()  
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='SMITH')  
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__hiredate__year=2024)   
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__deptno=30) 
    


    
    
    
      



    d={'emd':emd}

    return render(request,'emp_mgr_dept.html',d)
