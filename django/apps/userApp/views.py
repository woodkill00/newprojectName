from apps.storeApp.models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, reverse
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, login, authenticate
from django.conf import settings
# from .forms import CustomUserCreationForm, RegistrationFrom, UserProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.

class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'userApp/userApp_profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update({
            "orders": Order.objects.filter(user=self.request.user, ordered=True)
        })
        return context

# class SignupView(generic.CreateView):
#     template_name = "user_app/registration/signup.html"
#     form_class = CustomUserCreationForm

#     # model = User
#     # fields = ("email","username","password1","password2")

#     def get_success_url(self):
#         return reverse("user_app_login")

# class LogoutView(generic.CreateView):
#     template_name = "user_app/registration/logout.html"
#     form_class = CustomUserCreationForm

#     # model = User
#     # fields = ("email","username","name","age","password1","password2")

#     def get_success_url(self):
#         return reverse(" ")

# class RegistrationView(generic.CreateView):
#     template_name = "user_app/registration/signup.html"

#     def register_view(request, *args, **kwargs):
#         user = request.user
#         if user.is_authenticated:
#             return HttpResponse(f"You are already authenticated as {user.email}.")

#         context = {}

#         if request.POST:

#             form = RegistrationFrom(request.POST)

#             if form.is_valid():
#                 form.save()
#                 email = form.cleaned_data.get('email').lower()
#                 raw_password = form.cleaned_data.get('password1').lower()
#                 user = authenticate(email=email, password=raw_password)
#                 login(request, user)
#                 destination = kwargs.get("next")
#                 if destination:
#                     return redirect(destination)
#                 return redirect("lead_list")

#             else:
#                 context['registration_form'] = form


#         return render(request, 'user_app/registration/signup.html', context)

# @login_required
# def my_profile_view(request):
#     profile = UserProfile.objects.get(user=request.user)
#     form = UserProfileForm(request.POST or None, request.FILES or None, instance=profile)
#     confirm = False

#     if form.is_valid():
#         form.save()
#         confirm = True

#     context = {
#         'profile': profile,
#         'form': form,
#         'confirm': confirm,

#     }
#     return render(request, 'user_app/profile/user_profile2.html', context)