import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import unquote

def evaluate_sentiment(text):
    text = text.lower()
    positive_words = ["fantastic", "excellent", "great", "good", "amazing", "wonderful", "best"]
    negative_words = ["bad", "poor", "terrible", "awful", "worst", "horrible"]

    if any(w in text for w in positive_words):
        return "positive"
    elif any(w in text for w in negative_words):
        return "negative"
    return "neutral"

def analyze_sentiment_get(request, input_txt):
    text = unquote(input_txt)
    sentiment = evaluate_sentiment(text)
    return JsonResponse({"sentiment": sentiment})

@csrf_exempt
def analyze_review_post(request):
    if request.method == "GET":
        text = request.GET.get("review", "")
        sentiment = evaluate_sentiment(text)
        return JsonResponse({"sentiment": sentiment})

    try:
        data = json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    review = data.get("review", "").strip()
    sentiment = evaluate_sentiment(review)
    return JsonResponse({
        "review": review,
        "sentiment": sentiment
    })