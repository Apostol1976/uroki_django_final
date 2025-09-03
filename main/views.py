from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from main.forms import ContactForm


def index(request):
    context = {"title": "Home - Главная"}
    return render(request, "main/index.html", context)


def about(request):
    context = {"title": "Home - Главная"}
    return render(request, "main/about.html", context)


def kontakti(request):
    context = {"title": "Home - Главная"}
    return render(request, "main/kontakti.html", context)


def message(request):
    context = {}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(
                form.cleaned_data["name"],
                form.cleaned_data["email"],
                form.cleaned_data["message"],
            )
            context = {"success": 1}
    else:
        form = ContactForm()
    context["form"] = form

    return render(request, "main/message.html", context)


def send_message(name, email, message):
    text = get_template("main/mesage.html")
    html = get_template("main/mesage.html")
    context = {"name": name, "email": email, "message": message}
    subject = "Сообщение от пользователя"
    from_email = "from@example.com"
    text_content = text.render(context)
    html_content = text.render(context)

    msg = EmailMultiAlternatives(
        subject, text_content, from_email, ["manager@example.com"]
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
