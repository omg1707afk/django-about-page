from django.http import JsonResponse
from django.views.decorators.http import require_GET
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

def load_dealers():
    p = BASE_DIR / "dealerships.json"
    if p.exists():
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("dealerships", [])
    return []

DEALERS = load_dealers()

@require_GET
def get_all_dealers(request):
    return JsonResponse(DEALERS, safe=False)

@require_GET
def get_dealers_by_state_param(request):
    state = request.GET.get("state", "").strip()
    if state:
        dealers = [
            d for d in DEALERS
            if d.get("state", "").lower() == state.lower() or d.get("st", "").lower() == state.lower()
        ]
        return JsonResponse(dealers, safe=False)
    return JsonResponse(DEALERS, safe=False)

@require_GET
def get_dealers_by_state_path(request, state):
    dealers = [
        d for d in DEALERS
        if d.get("state", "").lower() == state.lower() or d.get("st", "").lower() == state.lower()
    ]
    return JsonResponse(dealers, safe=False)

@require_GET
def get_dealer_by_id(request, dealer_id):
    for dealer in DEALERS:
        if dealer.get("id") == dealer_id:
            return JsonResponse(dealer)
    return JsonResponse({"error": "Dealer not found"}, status=404)
