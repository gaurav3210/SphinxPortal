from django.contrib import admin

# Register your models here.
from User.models import user, past_contest
from Contest.models import contest, question

admin.site.register(user)
admin.site.register(past_contest)
admin.site.register(contest)
admin.site.register(question)