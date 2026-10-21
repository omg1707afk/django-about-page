from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .dealers import DEALERS

@require_GET
def get_dealers_by_state(request):
    state = request.GET.get("state", "").strip()
    dealers = [
        dealer for dealer in DEALERS
        if dealer["state"].lower() == state.lower() or dealer.get("st", "").lower() == state.lower()
    ]
    return JsonResponse({"dealers": dealers})