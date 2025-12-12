from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import UsuarioEdit, UsuarioDetailView, alterar_usuario, AcessoNegadoView, CustomPasswordResetCompleteView


urlpatterns = [
    path('perfil/', UsuarioDetailView.as_view(), name='perfil'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path('senha/', UsuarioEdit.as_view(), name='alterar_senha'),
    path('usuario/', alterar_usuario, name='alterar_usuario'),

    path('acesso-negado/', AcessoNegadoView.as_view(), name='acesso-negado'),

    # Formulário para enviar e-mail
    path('reset_senha/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'
    ), name='reset_password'),

    # Mensagem de e-mail enviada
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_sent.html'
    ), name='password_reset_done'),

    # Link de redefinição do e-mail
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_form.html'
    ), name='password_reset_confirm'),

    # Redefinição concluída
    path('reset_password_complete/',
        CustomPasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),


]