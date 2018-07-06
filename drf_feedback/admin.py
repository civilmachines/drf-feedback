from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    search_fields = ['name', 'email', 'mobile']
    list_per_page = 10
    list_display = ('name', 'email', 'mobile')

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return ()
        return 'created_by', 'create_date'


admin.site.register(Feedback, FeedbackAdmin)
