from django.core.mail import send_mail

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(["POST"])
def portfolio_contact_me(request):
    """
    DRF API VIEW
    """
    subject = request.data.get("subject")
    message = request.data.get("message")
    email = request.data.get("email")
    print(subject, message, email)

    try:
        send_mail(
            subject,
            message,
            email,
            ["agr.rituraj@gmail.com"],
            fail_silently=False,
        )
        return Response({"message": "mail sent successfully!"})

    except Exception as e:
        return Response({"error": "An Error occurred!"})
