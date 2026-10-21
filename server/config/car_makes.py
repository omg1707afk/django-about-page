from django.http import JsonResponse
from django.views.decorators.http import require_GET

CAR_MAKES = [
    {
        "make": "Toyota",
        "models": ["Camry", "Corolla", "Prius"]
    },
    {
        "make": "Honda",
        "models": ["Civic", "Accord", "CR-V"]
    },
    {
        "make": "Ford",
        "models": ["Focus", "Mustang", "Explorer"]
    },
    {
        "make": "BMW",
        "models": ["3 Series", "5 Series", "X5"]
    }
]

@require_GET
def get_all_car_makes(request):
    return JsonResponse({"car_makes": CAR_MAKES})