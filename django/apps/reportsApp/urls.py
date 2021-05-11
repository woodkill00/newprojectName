from django.urls import path
from .views import (
    create_report_view,
    ReportDetailView,
    ReportListView,
    render_pdf_view,
    ReportUploadTemplateView,
    report_csv_upload_view,
)

app_name = 'reportsApp'

urlpatterns = [
    path('', ReportListView.as_view(), name='report-main'),
    path('save/', create_report_view, name='report-create'),
    path('upload/', report_csv_upload_view, name='report-upload'),
    path('from_file/', ReportUploadTemplateView.as_view(), name='report-from-file'),
    path('<pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('<pk>/pdf/', render_pdf_view, name='report-pdf'),
]