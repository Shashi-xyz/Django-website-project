from django.contrib import admin
from myapp.models import Contact  # Ensure the correct model name is used

# Register your model
admin.site.register(Contact)  # Use "Contact" with an uppercase "C"
