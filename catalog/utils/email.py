from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string
from products.models import Order
from django.conf import settings

def send_email_confirm(request, user, new_email):
    confirm_url = request.build_absolute_uri(reverse("accounts:confirm_email"))
    confirm_url += f"?user={user.id}&email={new_email}"
    subject = "Confirm New Email"
    message = f"Hello, {user.username}, you want to change your email? " \
                f"To confirm this operation click on link: {confirm_url}"
    send_mail(subject, message, from_email="noreply@gmail.com", recipient_list = [f"{new_email}"], fail_silently=False)
    messages.info(request, "Confirmation Email Sent!")
    
def send_order_confirmation_email(order: Order  ):
    subject = f"Confirmation order{order.id}"
    context = {"order": order}
    text_content = render_to_string("email/confirmation_email.txt", context)
    to_email = order.contact_email
    try:
        send_email(subject, text_content, settings.DEFAULT_FROM_EMAIL, [to_email, settings.ADMIN_EMAIL])
    except Exception as e:
        print("Error sending email: {e}")
        
    