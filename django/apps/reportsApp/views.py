import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.shortcuts import render, get_object_or_404
from apps.userApp.models import UserProfile
from apps.salesApp.models import Sale, Position, CSV
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import get_report_image
from .models import Report
from .forms import ReportForm
from django.views import generic
import csv
from django.utils.dateparse import parse_date
from apps.productApp.models import Product
from apps.customerApp.models import Customer

# Create your views here.

class ReportListView(LoginRequiredMixin, generic.ListView):
    model = Report
    template_name = 'reportsApp/reports_app_main.html'


class ReportDetailView(LoginRequiredMixin, generic.DetailView):
    model = Report
    template_name = 'reportsApp/reports_app_detail.html'

class ReportUploadTemplateView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'reportsApp/reports_app_from_file.html'

def report_csv_upload_view(request):
    print('file is being sent')

    if request.method == 'POST':
        csv_file_name = request.FILES.get('file').name
        csv_file = request.FILES.get('file')
        obj, created = CSV.objects.get_or_create(file_name=csv_file_name)

        if created:
            obj.csv_file = csv_file
            obj.save()
            with open(obj.csv_file.path, 'r') as f:
                reader = csv.reader(f)
                reader.__next__()
                for row in reader:
                    print(row, type(row))
                    # print(row)
                    data = row
                    print(data)
                    # if you need to edit the uploaded file to process
                    # data = "".join(row)
                    # print(data, type(data))
                    # data = data.split(',')
                    # print(data, type(data))
                    # if the list has a ' ' blank value at end
                    # data.pop()
                    # print(data)

                    transaction_id = data[1]
                    product = data[2]
                    quantity = int(data[3])
                    customer = data[4]
                    date = parse_date(data[5])

                    try:
                        product_obj = Product.objects.get(title__iexact=product)
                    except Product.DoesNotExist:
                        product_obj = None

                    if product_obj is not None:
                        # print(transaction_id)
                        # print(product)
                        # print(quantity)
                        # print(customer)
                        # print(date)
                        # print(Customer.objects.get(user__username=customer))
                        # Customer.user.id
                        customer_obj, _ = Customer.objects.get_or_create(user__username=customer)
                        salesman_obj = UserProfile.objects.get(user=request.user)
                        position_obj = Position.objects.create(product=product_obj, quantity=quantity, created=date)

                        sale_obj, _ = Sale.objects.get_or_create(transaction_id=transaction_id, customer=customer_obj, salesman=salesman_obj, created=date)
                        sale_obj.positions.add(position_obj)
                        sale_obj.save()
                return JsonResponse({'ex': False})
        else:
            return JsonResponse({'ex': True})

    return HttpResponse()

@login_required
def create_report_view(request):
    form = ReportForm(request.POST or None)
    if request.is_ajax():
        # name = request.POST.get('name')
        # remarks = request.POST.get('remarks')

        image = request.POST.get('image')
        img = get_report_image(image)
        author = UserProfile.objects.get(user=request.user)

        # Report.objects.create(name=name, remarks=remarks, image=img, author=author)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.image = img
            instance.author = author
            instance.save()

        return JsonResponse({'msg': 'send'})
    return JsonResponse({})



@login_required
def render_pdf_view(request, pk):
    template_path = 'reportsApp/reports_app_pdf.html'
    # context = {'myvar': 'this is your template context'}

    obj = get_object_or_404(Report, pk=pk)
    context = {'obj': obj}

    response = HttpResponse(content_type='application/pdf')

    # if download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display
    response['Content-Disposition'] = 'filename="report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    # pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response