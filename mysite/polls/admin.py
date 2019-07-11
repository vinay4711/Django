from django.contrib import admin

from .models import Choice, Question
from .model_many_one import Article
from .model_many_many import Publication,Article2
from .model_many_many1 import Entry,Blog,Author
#from .model_aggr import Store,Book_Author,Book_Publisher,Book
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id','question','choice_text']

admin.site.register(Choice,ChoiceAdmin)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_text', 'quest_Type', 'pub_date']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date','quest_Type'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Article)
admin.site.register(Publication)
#admin.site.register(Article2)
#admin.site.register(Blog)
#admin.site.register(Author)
#admin.site.register(Entry)
#admin.site.register(Store)
#admin.site.register(Book_Author)
#admin.site.register(Book_Publisher)
#admin.site.register(Book)