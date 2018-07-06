from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    search_fields = ['ip', 'name', 'form_name', 'email', 'phone_number']
    list_per_page = 10
    list_display = ('name', 'email', 'phone_number')

    readonly_fields = ('created', )


admin.site.register(Feedback, FeedbackAdmin)
