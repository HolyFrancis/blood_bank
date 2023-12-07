from django.urls import path
from django.contrib.auth import views as auth_views

from apps.views import home, user, donor, transfusion, psl, analyse, equipement, client, order, stock

urlpatterns = [
    path("login", user.loginview, name="login"),
    path("register", user.register, name="register"),
    path("logout", user.logoutview, name="logout"),
    path("users", user.users, name="users"),  
    path("settings", user.settings, name="settings"),  
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="apps/user/reset_password.html"), name="reset_password"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="apps/user/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="apps/user/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="apps/user/password_reset_complete.html"), name="password_reset_complete"),
    
    
    path("", home.home, name="home"),
    
    path("donor", donor.donor, name="donor"),
    path("create-donor", donor.create_donor, name="create_donor"),
    path("update-donor/<str:id>", donor.update_donor, name="update_donor"),
    path("donor-details/<str:id>", donor.donor_details, name="donor_details"),
    path("delete-donor/<str:id>", donor.delete_donor, name="delete_donor"),
    
    path("transfusion", transfusion.transfusion, name="transfusion"),
    path("psl", psl.psl, name="psl"),
    path("analyse", analyse.analyse, name="analyse"),
    path("equipement", equipement.equipement, name="equipement"),
    path("client", client.client, name="client"),
    path("order", order.order, name="order"),
    path("stock", stock.stock, name="stock"),
]
