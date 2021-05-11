"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.i18n import i18n_patterns
import debug_toolbar
from django.conf import settings
# from config.settings import base
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    # path('accounts/', include('allauth.urls')),
    # (Note that this example makes the view available at /i18n/setlang/.)
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('apps.updateServerApp.urls', namespace="updateServer_app")),
]

urlpatterns += i18n_patterns(
    # path('', views.HomeView.as_view(), name="home")),
    path('', include('apps.mainApp.urls', namespace="main_app")),
    path('polls/', include('apps.pollsApp.urls', namespace="polls_app")),
    # path('feed_app/', include('feed_app.urls', namespace="feed_app")),
    # path('about/', about_views.main, name='about'),
    # path('news/', include(news_patterns, namespace='news')),
    # path('newsReaderApp', include("apps.newsReaderApp.urls", namespace="newsReader_app")),
    path('inventoryManagementApp/', include('apps.inventoryManagementApp.urls', namespace='inventoryManagement_app')),
    # path('profile/', views.ProfileView.as_view(), name='profile'),
    # path('user/', include('user_app.urls', namespace='user_app')),
    path('sales/', include('apps.salesApp.urls', namespace='sales_app')),
    path('reports/', include('apps.reportsApp.urls', namespace='reports_app')),
)


if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
