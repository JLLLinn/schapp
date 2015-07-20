from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice


# add inline to the question view
# admin.TabularInline takes less space (each as one line)
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


# this is choosing how the admin form want to display
# could either just have a list of fields or fieldsets with
#   categorized fields
# collapse is to collapse that fieldset for now
class QuestionAdmin(admin.ModelAdmin):
    # this is for displaying in a table manner, each is a horizontal list
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # add a filter
    list_filter = ['pub_date']
    # add a search field
    search_fields = ['question_text']


# to register for the model so that admin can add records
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
