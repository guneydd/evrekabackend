from django.contrib import admin

from .models import NavigationRecord
from .models import Vehicle
from .models import Bin
from .models import Collection
from .models import Operation



admin.site.register(NavigationRecord)
admin.site.register(Vehicle)
admin.site.register(Bin)
admin.site.register(Collection)
admin.site.register(Operation)