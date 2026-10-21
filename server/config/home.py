from django.shortcuts import render

def home(request):
    dealers = [
        {"id": 1, "name": "Demo Dealer", "location": "Pune", "state": "Kansas"},
        {"id": 2, "name": "Sample Dealer", "location": "Mumbai", "state": "California"},
    ]

    selected_state = request.GET.get("state", "").strip()

    if selected_state:
        dealers = [
            dealer for dealer in dealers
            if dealer["state"].lower() == selected_state.lower()
        ]

    return render(request, "home.html", {
        "dealers": dealers,
        "selected_state": selected_state,
        "username": request.user.username if request.user.is_authenticated else "",
        "is_logged_in": request.user.is_authenticated,
    })