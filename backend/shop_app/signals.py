from django.db.models.signals import post_save, pre_save
from .models import User
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from rest_framework_simplejwt.tokens import RefreshToken


@receiver(pre_save, sender=User)
def user_to_inactive(sender, instance, **kwargs):
    if instance._state.adding is True:
        instance.is_active = False


@receiver(post_save, sender=User)
def email_verification(sender, instance, **kwargs):
    if kwargs['created']:
        user = instance

        merge_data = {
            'user': user,
            'protocol': "http",
            'domain': '127.0.0.1:8000',
            'token': RefreshToken.for_user(user=user).access_token
        }

        subject = render_to_string("email/email_verification/email_subject.txt", merge_data).strip()
        html_body = render_to_string("email/email_verification/email_body.html", merge_data)

        msg = EmailMultiAlternatives(subject=subject, to=["mbanach2@edu.cdv.pl"])
        msg.attach_alternative(html_body, "text/html")
        msg.send()


pre_save.connect(user_to_inactive, sender=User)
post_save.connect(email_verification, sender=User)

