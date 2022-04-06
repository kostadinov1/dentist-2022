from django.contrib.auth import get_user_model
from django.db import models

from dentist_3_project.services.models import Service

UserModel = get_user_model()




class Appointment(models.Model):
    VENUES = (('Balchik', 'Balchik'), ('Kavarna', 'Kavarna'), ('Varna', 'Varna'),)

    venue = models.CharField(max_length=20, choices=VENUES,)
    time = models.TimeField()
    date = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING,)

    # @property
    # def number_of_reviews(self):
    #     return Appointment.objects.filter(reviews__user=self.user).count()


    def __str__(self):
        return f'Appointment at {self.venue} on {self.date} at {self.time}'

class Review(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, blank=True)



