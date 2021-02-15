
from django.contrib import admin
from .models import NIKKEI,SP500,USDJPY,BITCOIN,COMMON

admin.site.register(NIKKEI)
admin.site.register(SP500)
admin.site.register(USDJPY)
admin.site.register(BITCOIN)
admin.site.register(COMMON)
