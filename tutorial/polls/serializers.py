from rest_framework import serializers
from .models import Question,Choice

class QuestionSerializer(serializers.modelSerializer):
    class Meta:
        model = Question
        fields = (
                'id',
                'question_text',
                'pub_date',
        )

class ChoiceSerializer(serializers.modelSerializer):
    class Meta:
        model = (
            fields = (
                'id',
                'question',
                'choice_text',
                'votes',
            )
        )