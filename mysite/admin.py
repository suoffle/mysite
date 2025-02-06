from django.contrib import admin
from .models import Question
#admin.site.register(Question)
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)