from django.contrib import admin
from ekratia.threads.models import Comment

# Register Thread models in the admin
admin.site.register(Comment)
