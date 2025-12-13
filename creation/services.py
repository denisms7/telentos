# accounts/services.py
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.conf import settings

User = get_user_model()


def create_user_from_request(access_request):
    password = get_random_string(10)

    user = User.objects.create_user(
        username=access_request.username,
        email=access_request.email,
        password=password,
    )

    user.first_name = access_request.full_name
    user.save()

    send_mail(
        subject='Acesso aprovado',
        message=(
            'Sua solicitação de acesso foi aprovada.\n\n'
            f'Usuário: {user.username}\n'
            f'Senha provisória: {password}\n\n'
            'Recomendamos alterar a senha no primeiro acesso.'
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )

    return user
