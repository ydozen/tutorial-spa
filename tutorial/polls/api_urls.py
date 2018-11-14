from rest_framework.routers import DefaultRouter
from . import api_views

question_router = DefaultRouter()
question_router.reqister(r'', api_views.QuestionViewSet)
