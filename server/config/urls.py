from django.contrib import admin
from django.urls import path

from .login_view import login_user, logout_user, register_user
from .dealers import (
    get_all_dealers,
    get_dealers_by_state_param,
    get_dealers_by_state_path,
    get_dealer_by_id,
)
from .dealer_reviews import get_dealer_reviews
from .car_makes import get_cars
from .analyze_review import analyze_sentiment_get, analyze_review_post
from .home import home
from .post_review import post_review

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),

    # Authentication endpoints (Rubric: /djangoapp/login and /djangoapp/logout)
    path("djangoapp/login", login_user, name="djangoapp-login"),
    path("djangoapp/login/", login_user, name="djangoapp-login-slash"),
    path("login/", login_user, name="login"),
    path("djangoapp/logout", logout_user, name="djangoapp-logout"),
    path("djangoapp/logout/", logout_user, name="djangoapp-logout-slash"),
    path("logout/", logout_user, name="logout"),
    path("djangoapp/registration", register_user, name="djangoapp-register"),
    path("register/", register_user, name="register"),
    path("signup/", register_user, name="signup"),

    # Dealership endpoints (Rubric: /fetchDealers, /fetchDealers/<state>, /fetchDealer/<id>)
    path("fetchDealers", get_all_dealers, name="fetch-dealers"),
    path("fetchDealers/", get_all_dealers, name="fetch-dealers-slash"),
    path("fetchDealers/<str:state>", get_dealers_by_state_path, name="fetch-dealers-state"),
    path("fetchDealer/<int:dealer_id>", get_dealer_by_id, name="fetch-dealer-id"),
    path("djangoapp/get_dealers", get_all_dealers, name="djangoapp-get-dealers"),
    path("djangoapp/get_dealers/", get_all_dealers, name="djangoapp-get-dealers-slash"),
    path("djangoapp/get_dealers/<str:state>", get_dealers_by_state_path, name="djangoapp-get-dealers-state"),
    path("dealers/", get_dealers_by_state_param, name="dealers-param"),
    path("dealers/by-state/", get_dealers_by_state_param, name="dealers-by-state"),
    path("dealers/<int:dealer_id>/", get_dealer_by_id, name="dealer-by-id"),

    # Reviews endpoints (Rubric: /fetchReviews/dealer/<id>)
    path("fetchReviews/dealer/<int:dealer_id>", get_dealer_reviews, name="fetch-reviews-dealer"),
    path("fetchReviews/dealer/<int:dealer_id>/", get_dealer_reviews, name="fetch-reviews-dealer-slash"),
    path("djangoapp/get_reviews/dealer/<int:dealer_id>", get_dealer_reviews, name="djangoapp-get-reviews"),
    path("dealers/<int:dealer_id>/reviews/", get_dealer_reviews, name="dealer-reviews"),

    # Car Models (Rubric: /djangoapp/get_cars)
    path("djangoapp/get_cars", get_cars, name="djangoapp-get-cars"),
    path("djangoapp/get_cars/", get_cars, name="djangoapp-get-cars-slash"),
    path("get_cars/", get_cars, name="get-cars"),
    path("car-makes/", get_cars, name="car-makes"),

    # Sentiment Analyzer (Rubric: /analyze/<text>)
    path("analyze/<path:input_txt>", analyze_sentiment_get, name="analyze-sentiment-get"),
    path("analyze-review/", analyze_review_post, name="analyze-review-post"),

    path("dealers/<int:dealer_id>/post-review/", post_review, name="post-review"),
]
