from django.shortcuts import render
from apps.storeApp.models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


# Create your views here.

class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'userApp/userApp_profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update({
            "orders": Order.objects.filter(user=self.request.user, ordered=True)
        })
        return context