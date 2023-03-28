from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    #change the representation of the object
    def __str__(self):
        #return string 
        return self.name + ': ' + self.description