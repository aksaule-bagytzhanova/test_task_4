from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Student(User):
    phone = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.username


class Quiz(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.questions.all()


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)
    order = models.IntegerField()

    def __str__(self):
        return self.text

    def get_answers(self):
        return self.answers.all()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class QuizTaker(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempts')
    correct_answers = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{str(self.student)}-{str(self.quiz)}-{str(self.correct_answers)}"
