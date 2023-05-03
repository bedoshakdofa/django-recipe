from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import recipe
from .forms import registertion,recipeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
def login_view(request):
    if request.method=="POST":
        username=request.POST.get('email')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            context={"error":"invaild username or password"}
            return render(request,'recipe/login.html',context=context)
    return render(request,'recipe/login.html')

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect('home')
    return render(request,'recipe/logout.html')

def sign_views(request):
    if request.method=="POST":
        form=registertion(request.POST or None)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
    else:
        form =registertion()
    return render(request,'recipe/signup.html',{"form":form})

def search_view(request):
    query=request.GET.get("q")
    obj=recipe.objects.filter(recipe_name__icontains=query)
    return render(request,'recipe/search.html',{"obj":obj})

def recipe_detial(request,id):
    object=recipe.objects.get(id=id)
    return render (request,'recipe/detial_view.html',{"object":object})

@login_required(login_url='login')
def recipe_record(request):
    admin=get_user(request)
    if request.method=="POST":
        form=recipeForm(request.POST , request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.auther=admin
            myform.save()
            form=recipeForm()
    else:
        form=recipeForm()
    context={"form":form,"obj":recipe}
    return render(request,'recipe/recipe_record.html',context=context)

