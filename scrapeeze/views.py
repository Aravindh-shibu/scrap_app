from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,UpdateView,TemplateView,DetailView
from scrapeeze.forms import SignupForm,SigninForm,ProfileUpdateForm,AddForm
from django.contrib.auth import authenticate,login,logout
from scrapeeze.models import UserProfile,Scrap,Wishlist
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

def signin_required(fn):
   def wrapper(request,*args,**kwargs):
      if not request.user.is_authenticated:
         messages.error(request,"invalid session")
         return redirect("signin")
      else:
         return fn(request,*args,**kwargs)
   return wrapper 





# Create your views here.

class RegisterView(CreateView):
      template_name="register.html"
      form_class=SignupForm
            
      def get_success_url(self):
            return reverse("sign_in")
            
class Sign_inView(View):
      def get(self,request,*args,**kwargs):
            form=SigninForm()
            return render (request,"signin.html",{"form":form})
      def post(self,request,*args,**kwargs):
            form=SigninForm(request.POST)
            if form.is_valid():
                  uname=form.cleaned_data.get("username")
                  pwd=form.cleaned_data.get("password")
                  user_obj=authenticate(request,username=uname,password=pwd)
                  if user_obj:
                        login(request,user_obj)
                        return redirect("product_list")
            return render(request,"signin.html",{"form":form})
      

class ProfileUpdateview(UpdateView):
      template_name="profile_update.html"
      form_class=ProfileUpdateForm
      model=UserProfile   

      def get_success_url(self):
            return reverse("product_list")
      
class ProfileListView(View):
      def get(self,request,*args,**kwargs):
            data=UserProfile.objects.get(user=request.user)
            scrap_obj=Scrap.objects.filter(user=request.user)
            return render(request,"profile_detail.html",{"data":data,"scraps":scrap_obj})
      
class SignOutView(View):
      def get(self,request,*args,**kwargs):
             logout(request)
             return redirect("sign_in")

class ProductAddView(View):
      def get(self,request,*args,**kwargs):
            form=AddForm()
            return render(request,"add.html",{"form":form})
      def post(self,request,*args,**kwargs):
            form=AddForm(request.POST,files=request.FILES)
            if form.is_valid():
                  form.instance.user=request.user
                  form.save()
                  return redirect("product_list")
            else:
                  return reverse("sign_in")
      
class ProductListView(View):
      def get(self,request,*args,**kwargs):
            data=Scrap.objects.all()
            return render(request,"ProductList.html",{"data":data})
            
class ProductUpdateView(UpdateView):
      template_name="ProductUpdate.html"
      form_class=AddForm

      def get_succeess_url(self):
            return reverse("sign_up")


class ProductDetailView(DetailView):
      model=Scrap
      template_name="product_detail.html"
      context_object_name="data"

@method_decorator(signin_required,name="dispatch")
class ScrapDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Scrap.objects.get(id=id).delete()
        messages.success(request,"mobile has been removed")
        return redirect("list")


@method_decorator(signin_required,name="dispatch")
class WishListView(View):
     def post(self,request,*args,**kwargs):
          id=kwargs.get("pk")
          scrap_obj=Scrap.objects.get(id=id)
          action=request.POST.get("action")
          wishlist,created=Wishlist.objects.get_or_create(user=request.user)
          if action =="add":
            wishlist.scrap.add(scrap_obj)
          elif action == "remove":
            wishlist.scrap.remove(scrap_obj)
          return redirect("product_list")
     
class WishListdetailView(View):
      def get(self,request,*args,**kwargs):
            data=Wishlist.objects.get(user=request.user)
            return render(request,"wishlist.html",{"data":data})
    