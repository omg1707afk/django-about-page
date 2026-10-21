from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .dealers import DEALERS

DEALER_REVIEWS = {
    1: [
        {
            "id": 1,
            "name": "Demo Dealer",
            "dealership": 1,
            "review": "Excellent service.",
            "purchase": True,
            "purchase_date": "02/15/2026",
            "car_make": "Toyota",
            "car_model": "Camry",
            "car_year": 2023,
            "sentiment": "positive",
            "rating": 5,
            "username": "demo",
        },
        {
            "id": 2,
            "name": "Demo Dealer",
            "dealership": 1,
            "review": "Good experience.",
            "purchase": False,
            "sentiment": "positive",
            "rating": 4,
            "username": "customer2",
        },
    ],
    2: [
        {
            "id": 3,
            "name": "Sample Dealer",
            "dealership": 2,
            "review": "Helpful dealer.",
            "purchase": True,
            "purchase_date": "01/10/2026",
            "car_make": "Honda",
            "car_model": "Civic",
            "car_year": 2022,
            "sentiment": "positive",
            "rating": 4,
            "username": "customer3",
        },
    ],
}

@require_GET
def get_dealer_reviews(request, dealer_id):
    dealer = None
    for d in DEALERS:
        if d["id"] == dealer_id:
            dealer = d
            break

    if dealer is None:
        return JsonResponse({"error": "Dealer not found"}, status=404)

    reviews = DEALER_REVIEWS.get(dealer_id, [])
    return JsonResponse({
        "dealer_id": dealer_id,
        "dealer": dealer,
        "reviews": reviews,
    })
