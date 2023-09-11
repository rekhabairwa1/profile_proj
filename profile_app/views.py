from django.shortcuts import render,HttpResponse
from .models import my_profile
from .forms import my_form


def profile(request):
     if request.method =="POST":
          name = request.POST['name']
          father_name = request.POST['father_name']
          mother_name = request.POST['mother_name']
          mail = request.POST['email']
          roll_no = request.POST['roll_no']
          stream = request.POST['stream']
          address = request.POST['address']
          state = request.POST['state']
          city = request.POST['city']
          pin_code = request.POST['pin_code']
          gender = request.POST['gender']
          mobile_no = request.POST['mobile_no']
          image = request.POST['image']
          description = request.POST['description']
          my_profile(name=name,father_name=father_name,mother_name=mother_name,email=mail,roll_no=roll_no,stream=stream,address=address,state=state,city=city,pin_code=pin_code,gender=gender,mobile_no=mobile_no,image=image,description=description ,).save()

          print(name,father_name,mother_name,roll_no,stream,address,state,city,gender,pin_code,mobile_no,image,description)

          return HttpResponse('Data Saved R!!')
           
     return render(request,'profile.html')


def myforms(request):
     if request.method == "POST":
      a=my_form(request.POST,request.FILES)
      print(a)
      if a.is_valid():
         
         print('i am in')
         n = a.cleaned_data['name']
         f = a.cleaned_data['father_name']
         m = a.cleaned_data['mother_name']
         e = a.cleaned_data['email']
         r = a.cleaned_data['roll_no']
         s = a.cleaned_data['stream']
         m = a.cleaned_data['mobile_no']
         i = a.cleaned_data['image'] 
         d = a.cleaned_data['description'] 
         st = a.cleaned_data['state']  
         c = a.cleaned_data['city']
         p = a.cleaned_data['pin_code'] 
         g = a.cleaned_data['gender']
         a = a.cleaned_data['address']

         my_profile(name=n,father_name=f,mother_name=m,email=e,roll_no=r,stream=s,address=a,state=st,city=c,pin_code=p,gender=g,mobile_no=m,image=i,description=d).save()    
         return HttpResponse('data saved !!!')


     a=my_form()
     context={
            'a':a
     }
     return render(request,'form.html',context)

def get_data(request):
    data = my_profile.objects.all()
    print(data)
    
           
           
