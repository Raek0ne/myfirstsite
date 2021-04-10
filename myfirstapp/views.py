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

def insert_portfolio(request):
    ticker = request.POST.get("ticker")
    price = request.POST.get("price")
    quantity = request.POST.get("quantity")
    date = request.POST.get("date")
    stock_obj = Stock.objects.create(ticker = ticker, price = price, quantity = quantity, date = date)
    stock_obj.save()
    messages.success(request, "Stock Portfolio was Saved Successfully !")
    return HttpResponseRedirect("/")

def remove_portfolio(request, pk):
    stock_obj = Stock.objects.get(pk=pk)
    if request.method =="POST":
        stock_obj.delete()
        messages.success(request, "Stock Portfolio was Removed Successfully !")
        return HttpResponseRedirect("/")

def edit_portfolio(request,pk):
    stock_obj = Stock.objects.get(pk=pk)
    if request.method =="POST":
        messages.success(request, "Stock Portfolio was Edited Successfully !")
        return HttpResponseRedirect("/")
