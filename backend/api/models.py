from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    symptoms = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.name
    

    


    