from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)  # Ensure this field exists
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name