from django.http import JsonResponse
from django.views.decorators.http import require_GET
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

def load_reviews():
    p = BASE_DIR / "reviews.json"
    if p.exists():
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("reviews", [])
    return []

ALL_REVIEWS = load_reviews()

@require_GET
def get_dealer_reviews(request, dealer_id):
    dealer_reviews = [
        r for r in ALL_REVIEWS
        if r.get("dealership") == dealer_id
    ]
    return JsonResponse(dealer_reviews, safe=False)
