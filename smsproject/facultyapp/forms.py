from django import forms

from .models import CourseContent


class AddCourseContentForm(forms.ModelForm):
    class Meta:
        model = CourseContent
        fields ="__all__"
        labels={"faculty":"Select Faculty id","course":"Select Course","description":"Enter Description ","link":"Link","contentimage":"Choose contentimage"}

