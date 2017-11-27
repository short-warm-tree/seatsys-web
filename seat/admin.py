from django.contrib import admin
from seat.models import seat
from seat.models import orderrecord
from seat.models import auto_token
from seat.models import polling
admin.site.register(seat)
admin.site.register(orderrecord)
admin.site.register(auto_token)
admin.site.register(polling)
# Register your models here.
