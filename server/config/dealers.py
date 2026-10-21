from django.http import JsonResponse
from django.views.decorators.http import require_GET

DEALERS = [
    {
        "id": 1,
        "name": "Demo Dealer",
        "city": "Topeka",
        "state": "Kansas",
        "st": "KS",
        "address": "123 Main Street",
        "zip": "66002",
        "lat": 39.0473,
        "long": -95.6752,
        "short_name": "Demo",
        "full_name": "Demo Dealer of Kansas",
        "location": "Pune",
    },
    {
        "id": 2,
        "name": "Sample Dealer",
        "city": "Los Angeles",
        "state": "California",
        "st": "CA",
        "address": "456 Market St",
        "zip": "90001",
        "lat": 34.0522,
        "long": -118.2437,
        "short_name": "Sample",
        "full_name": "Sample Dealer of California",
        "location": "Mumbai",
    },
]

@require_GET
def get_dealers(request):
    state = request.GET.get("state", "").strip()
    if state:
        dealers = [
            d for d in DEALERS
            if d.get("state", "").lower() == state.lower() or d.get("st", "").lower() == state.lower()
        ]
        return JsonResponse({"dealers": dealers})
    return JsonResponse({"dealers": DEALERS})
