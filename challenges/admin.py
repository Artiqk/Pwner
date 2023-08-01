from django.contrib import admin

from .models import *

admin.site.register(ChallengeCategory)

admin.site.register(Challenge)