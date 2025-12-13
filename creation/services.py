# accounts/services.py
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db import transaction
from django.utils.crypto import get_random_string

from profiles.models import Profile

User = get_user_model()


@transaction.atomic
def create_user_from_request(access_request):
    password = get_random_string(10)

    user, _ = User.objects.get_or_create(
        username=access_request.username,
        defaults={
            'email': access_request.email,
        },
    )

    # 🔐 SEMPRE atualizar a senha provisória
    user.set_password(password)
    user.first_name = access_request.full_name
    user.email = access_request.email
    user.save()

    Profile.objects.update_or_create(
        user=user,
        defaults={
            'cpf': access_request.cpf,
            'function': access_request.role,
        },
    )

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
