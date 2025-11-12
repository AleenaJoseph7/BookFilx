from django.contrib import admin
from Myapp.models import bookdb,catergorydb
from webapp.models import contactdb
# Register your models here.
admin.site.register(catergorydb)
admin.site.register(bookdb)
admin.site.register(contactdb)