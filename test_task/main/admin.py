from django.contrib import admin
from .models import Question, Answer, QuizTaker, Student, Quiz


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('order', 'text')
    list_filter = ('quiz', )


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_correct')
    list_filter = ('question', 'question__quiz')


admin.site.register(Student)
admin.site.register(Quiz)
admin.site.register(QuizTaker)
