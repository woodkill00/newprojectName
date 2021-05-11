from enum import auto
from django.db import models
# from django.db.models.fields import CharField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from company_app.models import Company

# Create your models here.

# def get_profile_image_filepath(self, filename):
#     return f'profile_images/{self.pk}/{"profile_image.png"}'

# def get_default_profile_image():
#     return "{IMAGE FILE PATH}"




class CustomUserManager(BaseUserManager):

    def create_superuser(self, email, username, password, **other_fields):

        # other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          **other_fields)
        user.set_password(password)
        user.save()
        # user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    id = models.AutoField(primary_key=True)

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    # date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    # about = models.TextField(_('about'), max_length=500, blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_organizer = models.BooleanField(default=False)
    # profile_image = models.ImageField(max_length=255, upLoad_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)
    # hide_email = models.BooleanField(default=True)
    # *** ADD ONS ***
    # *** AGENT_APP ***
    is_agent = models.BooleanField(default=False)
    # *** COMPANY_APP ***
    # company_name = models.ForeignKey(Company, max_length=150, unique=True, blank=True)
    # company_name = models.ManyToManyField(Company, max_length=150, unique=True, blank=True)
    # *** STORE_APP ***
    # customer = str(username)
    is_customer = models.BooleanField(default=True)


    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    # def get_profile_image_filename(self):
    #     return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}'):]

    # def has_perm(self, perm, obj=None):
    #     return self.is_admin

    # def has_module_perms(self, app_label):
    #     return True

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...", blank=True)
    # user_folder = CustomUser.username
    # avatar = models.ImageField(upload_to=f'user/{user_folder}/avatars', default='no_picture.png', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        # return self.user.username + ' profile'
        return self.user.username
        # return _('[Profile] ') + self.user.username
        # return _('Profile of ') + "{self.user.username}"