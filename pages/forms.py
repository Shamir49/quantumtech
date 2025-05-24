from django.forms import ModelForm
from pages.models import *

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

