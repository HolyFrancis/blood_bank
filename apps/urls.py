from django.contrib.auth import views as auth_views
from django.urls import path

from apps.views import analyse, client, donor, home, order, psl, transfusion, solution, user, public

urlpatterns = [
    # -------------------------------User related-------------------------------
    path("login", user.loginview, name="login"),
    path("register", user.register, name="register"),
    path("logout", user.logoutview, name="logout"),
    
    path("users", user.users, name="users"),
    path("user-requests", user.user_requests, name="user_requests"),
    path("settings", user.settings, name="settings"),
    
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(template_name="apps/user/reset_password.html"),
        name="reset_password",
    ),
    path(
        "password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(template_name="apps/user/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="apps/user/password_reset_confirm.html"),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        auth_views.PasswordResetCompleteView.as_view(template_name="apps/user/password_reset_complete.html"),
        name="password_reset_complete",
    ),
    path("change_password/", auth_views.PasswordChangeView.as_view(template_name="apps/user/change_password.html"), name="change-password"),
    path("password_success/", user.password_success, name="password_success"),
    path("", home.home, name="home"),
    # -------------------------------Donor-------------------------------
    path("donor", donor.donor, name="donor"),
    path("create-donor", donor.create_donor, name="create_donor"),
    path("update-donor/<str:id>", donor.update_donor, name="update_donor"),
    path("donor-details/<str:id>", donor.donor_details, name="donor_details"),
    path("delete-donor/<str:id>", donor.delete_donor, name="delete_donor"),
    path("donor-requests", donor.donor_requests, name="donor_requests"),
    path("requests-decision/<str:id>", donor.request_decision, name="request_decision"),
    path("donor-history", donor.donor_history, name="donor_history"),
    # -------------------------------Transfusion-------------------------------
    path("blood", transfusion.blood, name="transfusion"),
    path("create-transfusion/<int:id>", transfusion.create_blood, name="create_blood"),
    path("update-transfusion/<int:id>/", transfusion.update_blood, name="update_blood"),
    path("blood-transfusion/<int:id>/", transfusion.blood_details, name="blood_details"),
    path("blood-delete/<int:id>", transfusion.blood_delete, name="delete_blood"),
    path("blood-request", transfusion.blood_request, name="blood_request"),
    path("blood-history", transfusion.blood_history, name="blood_history"),
    # -------------------------------psl-------------------------------
    path("psl", psl.psl, name="psl"),
    path("create-psl/<int:id>", psl.create_psl, name="create_psl"),
    path("update-psl/<int:id>", psl.update_psl, name="update_psl"),
    path("psl-details/<int:id>", psl.psl_details, name="psl_details"),
    path("psl-delete/<int:id>", psl.psl_delete, name="psl_delete"),
    path("create-type", psl.create_type, name="create_type"),
    path("update-type/<int:id>", psl.update_type, name="update_type"),
    path("delete-type/<int:id>", psl.delete_type, name="delete_type"),
    # -------------------------------analyse-------------------------------
    path("analyse", analyse.analyse, name="analyse"),
    path("create-analysis/<str:id>", analyse.create_analysis, name="create_analysis"),
    path("update-analysis/<str:id>", analyse.update_analysis, name="update_analysis"),
    path("analysis-details", analyse.analysis_details, name="analysis_details"),
    path("delete-analysis/<str:id>", analyse.delete_analysis, name="delete_analysis"),
    path("request-analysis", analyse.request_analysis, name="request_analysis"),
    path("analysis-history", analyse.analysis_history, name="analysis_history"),
    # -------------------------------Solution-------------------------------
    path("solution", solution.solution, name="solution"),
    path(
        "save-solution",
        solution.save_solution,
        name="create_solution",
    ),
    path(
        "update-solution/<int:id>",
        solution.update_solution,
        name="update_solution",
    ),
    path(
        "solution-delete/<int:id>",
        solution.delete_solution,
        name="solution_delete",
    ),
    # -------------------------------Client-------------------------------
    path("client", client.client, name="client"),
    path("create-client", client.create_client, name="create_client"),
    path("update-client/<str:id>", client.update_client, name="update_client"),
    path("client-details/<str:id>", client.client_details, name="client_details"),
    path("delete-client/<str:id>", client.delete_client, name="delete_client"),
    # -------------------------------Order-------------------------------
    path("order", order.order, name="order"),
    path("create-order", order.create_order, name="create_order"),
    path("update-order/<str:id>", order.update_order, name="update_order"),
    path("delete-order/<str:id>", order.delete_order, name="delete_order"),
    path("blood-order-quantity/<str:id>", order.BloodQantityOrderDetatils, name="blood_quantity"),
    path("blood-order-requests", order.order_request, name="order_requests"),
    path("blood-order-decision/<str:id>", order.blood_order_decision, name="order_decision"),
    path("blood-order-history", order.blood_order_history, name="order_history"),
    path("blood-order-history-decision/<int:id>", order.blood_history_decision, name="order_history_decision"),
    # -------------------------------Public-------------------------------
    path("public-home", public.public, name="public"),
]
