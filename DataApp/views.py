from django.shortcuts import render
from DataApp import models
from DataApp.models import faq
from DataApp.models import contactus
from DataApp.models import userregister
from DataApp.models import review

# Create your views here.
def login(request):
	if request.method=="POST":
		e=request.POST.get('em')
		p=request.POST.get('pw')
		res=userregister.objects.filter(email=e, password=p)

		if len(res)>0:
			request.session['email']=e
			return render(request,'sidebar.html')
		else:
			msg="Invalid Login"
			return render(request,'login.html')
	else:
		return render(request,'login.html')

def base(request):
	return render(request,'base.html')

def nav(request):
	return render(request,'NAV.html')

def footer(request):
	return render(request,'footer.html')

def allfaq(request):
	res=faq.objects.all()
	return render(request,'allfaq.html',{'data':res})	

def contact(request):
	if request.method=="POST":
		ho=contactus()
		ho.Name=request.POST.get('name')
		ho.email_id=request.POST.get('email')
		ho.message=request.POST.get('comment')
		ho.save()
		return render(request,'contactus.html',{'msg':"data successfully added"})
	else:
		return render(request,'contactus.html')

def register(request):
	if request.method=="POST":
		n=request.POST.get('nm')
		e=request.POST.get('em')
		p=request.POST.get('pw')
		c=request.POST.get('cpw')
		if userregister.objects.filter(email=e).exists():
			msg="Email Id is already registered"
			return render(request,'register.html',{'msg':msg})
		else:
			if p==c:
				x=userregister()
				x.name=n
				x.email=e
				x.password=p
				x.save()
				msg="user successfully registered "
				return render(request,'register.html',{'msg':msg})
			else:
				msg="password and c-pass doesnot match"
				return render(request,'register.html',{'msg':msg})

	else:
		return render(request,'register.html')	

def change(request):

	if request.method=="POST":
		re=userregister.objects.get(email=request.session['email'])
		opassword=request.POST.get('old')
		npassword=request.POST.get('new')
		cpassword=request.POST.get('cpass')

		if(npassword==cpassword):	
			pa=re.cpassword
			print(pa)
			if(opassword==pa):
				re.password=npassword
				re.save()
				rest="Password Changed"
				return render(request,'changepassword.html',{'rest':rest})
			else:
				res="Invalid current Password"
				return render(request,'changepassword.html',{'res':res})
		else:
			res="Confirm password and new password don't match"
			return render(request,'changepassword.html',{'res':res})
	else:
		return render(request,'changepassword.html')

def reviews(request):

	if request.method=="POST":
		re=review()
		re.name=request.POST.get('nm')
		re.message=request.POST.get('msg')
		re.save()

	else:
		return render(request,'review.html')

def forget(request):
	return render(request,'forgetpassword.html')