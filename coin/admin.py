from django.contrib import admin

# Register your models here.

from core.models import Blockchain, Task, Notification, FollowerProfile, ScopeUser, Airdrop

admin.site.register(Airdrop)
admin.site.register(Blockchain)
admin.site.register(ScopeUser)
admin.site.register(Task)