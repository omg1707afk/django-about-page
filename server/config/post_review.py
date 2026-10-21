
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound

DEALERS = {
    1: {
        "id": 1,
        "name": "Demo Dealer",
        "location": "Pune",
    },
    2: {
        "id": 2,
        "name": "Sample Dealer",
        "location": "Mumbai",
    },
}

# Temporary storage for posted reviews
POSTED_REVIEWS = {}


def post_review(request, dealer_id):
    dealer = DEALERS.get(dealer_id)

    if dealer is None:
        return HttpResponseNotFound("Dealer not found")

    error = ""

    if request.method == "POST":
        reviewer_name = request.POST.get(
            "reviewer_name", ""
        ).strip()

        rating = request.POST.get("rating", "").strip()

        review_text = request.POST.get(
            "review", ""
        ).strip()

        if not reviewer_name or not review_text:
            error = "Please enter your name and review."

        elif rating not in {"1", "2", "3", "4", "5"}:
            error = "Please select a valid rating."

        else:
            review = {
                "username": reviewer_name,
                "rating": int(rating),
                "review": review_text,
            }

            POSTED_REVIEWS.setdefault(dealer_id, []).append(review)

            return redirect(
                "post-review",
                dealer_id=dealer_id,
            )

    return render(
        request,
        "post_review.html",
        {
            "dealer": dealer,
            "reviews": POSTED_REVIEWS.get(dealer_id, []),
            "error": error,
        },
    )
