
from django.shortcuts import render , HttpResponseRedirect
from .forms import ProductDetails
from .models import User
# display all the products and will add items.
def home(request):
    if request.method == 'POST':
        fm = ProductDetails(request.POST)
        if fm.is_valid():
            prod_name = fm.cleaned_data['Product_Name']
            pri = fm.cleaned_data['Price']
            quant = fm.cleaned_data['Quantity']
            reg = User(Product_Name=prod_name,Price=pri,Quantity=quant)
            reg.save()
            fm = ProductDetails()
    else:
        fm = ProductDetails() 
    stud = User.objects.all()       
    return render(request,"enroll/home_page.html",{'forms':fm,'stu':stud})


def delete_product(request , id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')    

def update_product(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = ProductDetails(request.POST,instance=pi) 
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = ProductDetails(instance=pi) 

    return render(request, 'enroll/update_product.html',{'id':id,'form':fm})
def search(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = ProductDetails(request.POST,instance=pi) 
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = ProductDetails(instance=pi) 

    return render(request, 'enroll/search.html',{'id':id,'form':fm})
