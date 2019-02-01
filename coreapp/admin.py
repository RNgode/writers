from django.contrib import admin
from .models import Order
from .models import Comment
from .models import Status
from .models import Bid
from .models import Client
from .models import Admin
from .models import Writer

# we register our objects here(these are the tables)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Status)
admin.site.register(Bid)
admin.site.register(Client)
admin.site.register(Admin)
admin.site.register(Writer)
