from django.contrib import admin
from testapp.models import Hydjobs
from testapp.models import Apjobs
from testapp.models import Kajobs
# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','number']
admin.site.register(Hydjobs,HydjobsAdmin)

class ApjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','number']
admin.site.register(Apjobs,ApjobsAdmin)

class KajobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','number']
admin.site.register(Kajobs,KajobsAdmin)