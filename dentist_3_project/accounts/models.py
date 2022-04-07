from cloudinary import models as cloudinary_models
from django.contrib.auth import models as auth_models
from django.db import models
from dentist_3_project.accounts.managers import AppUsersManager
from dentist_3_project.common.validators import validate_only_letters


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False,)
    date_joined = models.DateTimeField(auto_now_add=True,)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False,)
    is_active = models.BooleanField(default=True)

    objects = AppUsersManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    GENDERS = (('Male', 'Male'), ('Female', 'Female'), ('LGBT+', 'LGBT+'), ('Prefer Not to Tell', 'Prefer Not to Tell'),)

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH,
                                  validators=(validate_only_letters,))
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH,
                                 validators=(validate_only_letters,))
    dob = models.DateField(null=True, blank=True,)
    gender = models.CharField(max_length=30, choices=GENDERS, null=True, blank=True)
    phone = models.CharField(max_length=10, unique=True)
    image = cloudinary_models.CloudinaryField('image')
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True,)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'





'''
1 - create the model extending abstract user and permissions mixin
2 - define fields desired - 'email', 'is_staff', 'is_superuser', 'date_joined', 'objects'
3 - define AUTH_USER_MODEL = '$appname.$classname' in settings.py
4 - create user manager (add objects field = class in manager.py and invoke it) - create managers.py in the app desired
5 - manager inherits BaseUserManager then go to UserManager copy paste the first 3 methods (create_user methods) and
    modify 'username' to become 'email' variable and delete some stuff -> check managers.py folder
'''
