from django.contrib import admin
from .models import Question, Category


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
