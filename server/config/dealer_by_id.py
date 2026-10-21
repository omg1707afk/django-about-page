from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .dealers import DEALERS

@require_GET
def get_dealer_by_id(request, dealer_id):
    for dealer in DEALERS:
        if dealer["id"] == dealer_id:
            return JsonResponse({"dealer": dealer})

    return JsonResponse({"error": "Dealer not found"}, status=404)