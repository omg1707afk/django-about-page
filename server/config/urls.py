from django.contrib import admin
from django.urls import path

from .login_view import login_user, logout_user, register_user
from .dealers import get_dealers
from .dealer_reviews import get_dealer_reviews
from .dealer_by_id import get_dealer_by_id
from .dealers_by_state import get_dealers_by_state
from .car_makes import get_all_car_makes
from .analyze_review import analyze_review
from .home import home
from .post_review import post_review

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", register_user, name="register"),
    path("signup/", register_user, name="signup"),
    path("dealers/", get_dealers, name="all-dealers"),
    path("get_dealers/", get_dealers, name="get-dealers"),
    path("dealers/<int:dealer_id>/reviews/", get_dealer_reviews, name="dealer-reviews"),
    path("dealers/<int:dealer_id>/", get_dealer_by_id, name="dealer-by-id"),
    path("dealers/by-state/", get_dealers_by_state, name="dealers-by-state"),
    path("car-makes/", get_all_car_makes, name="car-makes"),
    path("analyze-review/", analyze_review, name="analyze-review"),
    path("dealers/<int:dealer_id>/post-review/", post_review, name="post-review"),
]
