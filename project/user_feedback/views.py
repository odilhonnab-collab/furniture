from django.shortcuts import render, redirect
from .models import Feedback

def feedback_page(request):

    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        Feedback.objects.create(
            name=name,
            message=message
        )

        return redirect("feedback")

    feedbacks = Feedback.objects.all().order_by("-created_at")

    return render(request, "comments.html", {"feedbacks": feedbacks})