from django.shortcuts import render, redirect
from .models import Product, Order, Feedback


def cart(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'core/cart.html', {'products': products})


def shop(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'core/shop.html', {'products': products})


def checkout(request):
    return render(request, 'core/checkout.html')


def feedback_page(request):

    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        Feedback.objects.create(
            name=name,
            message=message
        )

        return redirect("/comments/")

    feedbacks = Feedback.objects.all()

    return render(request, "core/comments.html", {
        "feedbacks": feedbacks
    })