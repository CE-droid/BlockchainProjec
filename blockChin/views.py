from django.shortcuts import render
import requests
from subprocess import check_output, run , PIPE, CalledProcessError, Popen
import sys
import tempfile
import io

def button(request):
    return render(request,'home.html')
def external(request):
   if request.method == "POST":
        inp=request.POST.get('message')
     #    if inp :
     #    l=[inp,respon]
        process = run([sys.executable,'BlockchainProjec\\blockChin\\test.py',inp],stdout=PIPE,text=True).stdout.strip(" ") 
        process2 = run([sys.executable,'BlockchainProjec\\blockChin\\test2.py',inp,'yes'],stdout=PIPE,text=True).stdout.strip(" ") 
         
     #    data={ 
     #      "data1":process,
     #      "data2":process2,

     #     }
     #    print(data)
      
        return render(request,'home.html',{'data1':process,'data2':process2}) 
     #    respon=request.POST.get('response')
     #    else:
     #     process2 = run([sys.executable,'C:\\Users\\HP\\Downloads\\BlockchainProject\\django\\blockChin\\blockChin\\test2.py',inp,'yes'],stdout=PIPE,text=True).stdout.strip(" ") 
     #     return render(request,'home.html',{'data2':process2}) 


    
        

   else: 
        return render(request,'home.html')
def output(request):
     data=requests.get("https//reqres.in/api/sers")
     print(data.text)
     data=data.text 
     return render (request,'home.html',{'data':data}) 
