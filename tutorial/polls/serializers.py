from rest_framework import serializers
from .models import Question,Choice

class QuestionSerializer(serializers.modelSerializer)