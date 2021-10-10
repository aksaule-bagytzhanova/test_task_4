from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, widgets
from .models import Question, Answer, Student


class StudentRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Student
        fields = ("username", "email", "phone", "password1", "password2")

    def save(self, commit=True):
        user = super(StudentRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['question', 'text', 'is_correct']
        widgets = {
            'text': widgets.Select(attrs={'class':'form-control select2', 'style':'width: 100%;'})
        }
