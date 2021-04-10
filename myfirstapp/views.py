from django.shortcuts import render, HttpResponseRedirect
# from django.http import HttpResponse
from .models import Stock
from django.contrib import messages

# Create your views here.
def render_index(request):
    stocks = Stock.objects.all()
    print(stocks)
    params = {
        "stocks": stocks
    }
    return render(request, "index.html", params)

def render_delete(request, main_id):
    stocks = Stock.objects.get(main_id = main_id)
    params = {"stock": stocks,"stock_id": main_id}
    return render(request, "delete.html", params)

def insert_portfolio(request):
    ticker = request.POST.get("ticker")
    price = request.POST.get("price")
    quantity = request.POST.get("quantity")
    date = request.POST.get("date")
    stock_obj = Stock.objects.create(ticker = ticker, price = price, quantity = quantity, date = date)
    stock_obj.save()
    messages.success(request, "Stock Portfolio was Saved Successfully !")
    return HttpResponseRedirect("/")

def remove_portfolio(request, main_id):
    stock_obj = Stock.objects.get(main_id=main_id)
    if request.method =="POST":
        stock_obj.delete()
        messages.success(request, "Stock Portfolio was Removed Successfully !")
        return HttpResponseRedirect("/")

def edit_portfolio(request,main_id):
    stock_obj = Stock.objects.get(main_id=main_id)
    if request.method =="POST":
        messages.success(request, "Stock Portfolio was Edited Successfully !")
        return HttpResponseRedirect("/")

# def delete_departments(request):
#     if request.method!="POST":
#         return HttpResponse("<h2>Method Not Allowed</h2>")
#     else:
#         main_id = request.POST.get('main_id')
#         try:
#             stocks = Stock.objects.get(main_id=main_id)
#             stocks.delete()
#             messages.success(request,"Successfully Deleted Department !")
#             return HttpResponseRedirect(reverse("/"))
#         except:
#             messages.error(request,"Failed to Delete Department !")
#             return HttpResponseRedirect(reverse("departments"))