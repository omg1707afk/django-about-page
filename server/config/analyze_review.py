import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def analyze_review(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    review = data.get("review", "").strip()

    if not review:
        return JsonResponse({"error": "Review is required"}, status=400)

    positive_words = ["fantastic", "excellent", "great", "good", "amazing"]
    negative_words = ["bad", "poor", "terrible", "awful", "worst"]

    text = review.lower()

    if any(word in text for word in positive_words):
        sentiment = "Positive"
    elif any(word in text for word in negative_words):
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return JsonResponse({
        "review": review,
        "sentiment": sentiment
    })