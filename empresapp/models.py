from django.db import models

# Create your models here.
class Employee(models.Model):
    def __str__(self):
        if self.SecondSurname is None:
            return self.Name + " " + self.FirstSurname
        else:
            return self.Name + " "+ self.FirstSurname + " " + self.SecondSurname
    DNI = models.CharField(primary_key=True,max_length=9)
    Name = models.CharField(max_length=50)
    FirstSurname = models.CharField(max_length=100)
    SecondSurname = models.CharField(max_length=100,blank=True,null=True)
    BirthDate = models.DateField() # Fecha nacimiento
    StartedDate = models.DateField() # Fecha alta
    DismissalDate = models.DateField(blank=True,null=True) # Fecha Despido
    RetirementDate = models.DateField(blank=True,null=True) # Fecha Jubilacion


