# from apps.cart.models import Product
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic
from apps.inventoryManagementApp.models import Stock
from apps.inventoryManagementApp.forms import StockCreateForm, StockSearchForm
from django.db.models import Q
from .filters import StockFilter
from apps.userApp.models import CustomUser


# Create your views here.

# class StockListView(generic.TemplateView):
#     template_name = 'inventoryManagementApp/stock_list.html'
    # def get_queryset(self):
    #     return super().get_queryset()



class StockListView(generic.ListView):
    template_name = 'inventoryManagementApp/stock_list.html'
    queryset = Stock.objects.all()
    context_object_name = "stocks"
    form_class = StockSearchForm
    form = StockSearchForm

    # def search(request, pk):
    #     searchstock = Stock.objects.get(id=pk)
    #     newstock = searchstock.order_set.all()
    #     myFilter = StockFilter(request.GET, queryset=newstock)
    #     newstock = myFilter.qs

    #     context = {
    #         'searchstock': searchstock, 'newstock': newstock,'myFilter': myFilter
    #     }
    #     return render(request, 'inventoryManagementApp/stock_list.html', context)


    # def get_queryset(self):
        # form = StockSearchForm
        # return super().get_queryset()
        # query = self.request.GET.get('q')
        # object_list = Stock.objects.filter(
        #     Q(category__icontains=query)
        # )
        # return Stock.objects.filter(
        #     category__icontains=form['category'].value(),
        #     item_name__icontains=form['item_name'].value()
        #     )
        # return object_list

    def get_success_url(self):
        return reverse("inventoryManagementApp:stock-list")

    # def stock_search(request):
    #     form = StockSearchForm(request.POST or None)
    #     if request.method == 'POST':
    #         print('Receiving Search Request')
    #         queryset = Stock.objects.filter(
    #             category__icontains=form['category'].value(),
    #             item_name__icontains=form['item_name'].value()
    #         )
    #         context = {
    #             "form": form,
    #             # "header": header,
    #             "queryset": queryset,
    #         }
    #         return render(request, "inventoryManagementApp/stock_list.html", context)



def stocks_list(request):
    stocks = Stock.objects.all()
    context = {
        "stocks": stocks
        }
    return render(request, "inventoryManagementApp/stock_list.html", context)

# def stock_search(request, pk):
#     # product = Product.objects.get(id=pk)
#     product = get_object_or_404(Product, pk=pk)
#     # stocks = Stock.objects.get(id=pk)
#     stocks = product.stock_set.all()
#     stock_count = stocks.count()

#     myFilter = StockFilter(request.GET, queryset=stocks)
#     stocks = myFilter.qs
#     # stockItem = myFilter.qs

#     context = {
#         "product": product,
#         "stocks": stocks,
#         "stock_count": stock_count,
#         # "stockItem": stockItem

#     }
#     return render(request, 'inventoryManagementApp/stock_list2.html', context)


class StockItemCreateView(generic.CreateView):
    template_name = 'inventoryManagementApp/stock_add_item.html'
    form_class = StockCreateForm

    def get_success_url(self):
        return reverse("inventoryManagementApp:stock-list")

    def form_valid(self, form):
        # # TODO send email
        # send_mail(
        #     subject="A Company has been created",
        #     message="Go to the site to see the new Company", from_email="test@test.com",
        #     recipient_list=["test2@test.com"]
        # )

        return super(StockItemCreateView, self).form_valid(form)


def stockItem_create(request):
    form = StockCreateForm()
    if request.method == "POST":
        print('Receiving a post request')
        form = StockCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inventoryManagementApp:stock-list")
    context = {
        "form": form
    }
    return render(request, "inventoryManagementApp/stock_add_item.html", context)

class StockItemUpdateView(generic.UpdateView):
    template_name = 'inventoryManagementApp/stock_update_item.html'
    queryset = Stock.objects.all()
    form_class = StockCreateForm

    def get_success_url(self):
        return reverse("inventoryManagementApp:stock-list")

def stockItem_update(request, pk):
    stocks = Stock.objects.get(id=pk)
    form = StockCreateForm(instance=stocks)
    if request.method == "POST":
        print('Receiving a post request')
        form = StockCreateForm(request.POST, instance=stocks)
        if form.is_valid():
            form.save()
            return redirect("inventoryManagementApp:stock-list")
    context = {
        "form": form,
        "ingredients": stocks
    }
    return render(request, "inventoryManagementApp/stock_update_item.html", context)

class StockItemDeleteView(generic.DeleteView):
    template_name = 'inventoryManagementApp/stock_delete_item.html'
    queryset = Stock.objects.all()
    form_class = StockCreateForm

    def get_success_url(self):
        return reverse("inventoryManagementApp:stock-list")


def stockItem_delete(request, pk):
    stock = Stock.objects.get(id=pk)
    stock.delete()
    return redirect("/inventoryManagementApp:stock-list")