from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, ActivityViewSet, TeamViewSet, WorkoutSuggestionViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'suggestions', WorkoutSuggestionViewSet)

urlpatterns = router.urls