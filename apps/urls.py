from django.contrib.auth import views as auth_views
from django.urls import path

from apps.views import analyse, client, donor, equipement, home, order, psl, stock, transfusion, user

urlpatterns = [
    path("login", user.loginview, name="login"),
    path("register", user.register, name="register"),
    path("logout", user.logoutview, name="logout"),
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
    path("", home.home, name="home"),
    path("donor", donor.donor, name="donor"),
    path("create-donor", donor.create_donor, name="create_donor"),
    path("update-donor/<str:id>", donor.update_donor, name="update_donor"),
    path("donor-details/<str:id>", donor.donor_details, name="donor_details"),
    path("delete-donor/<str:id>", donor.delete_donor, name="delete_donor"),
    path("blood", transfusion.blood, name="transfusion"),
    path("create-transfusion", transfusion.create_blood, name="create_blood"),
    path("update-transfusion/<int:id>/", transfusion.update_blood, name="update_blood"),
    path("blood-transfusion/<int:id>/", transfusion.blood_details, name="blood_details"),
    path("blood-delete/<int:id>", transfusion.blood_delete, name="delete_blood"),
    path("psl", psl.psl, name="psl"),
    path("create-type-psl", psl.create_type_PSL, name="create_type_psl"),
    path("update-type-psl/<int:id>", psl.update_type_psl, name="update_type_psl"),
    path("type-psl-details/<int:id>", psl.type_psl_details, name="type_psl_details"),
    path("type-psl-delete/<int:id>", psl.type_psl_delete, name="type_psl_delete"),
    path("create-psl", psl.create_psl, name="create_psl"),
    path("update-psl/<int:id>", psl.update_psl, name="update_psl"),
    path("psl-details/<int:id>", psl.psl_details, name="psl_details"),
    path("psl-delete/<int:id>", psl.psl_delete, name="psl_delete"),
    path("analyse", analyse.analyse, name="analyse"),
    path("equipement", equipement.equipement, name="equipement"),
    path(
        "save-equipment-type",
        equipement.save_equipmentType,
        name="create_equipment_type",
    ),
    path(
        "update-equipment-type/<int:id>",
        equipement.update_equipmentType,
        name="update_equipment_type",
    ),
    path(
        "equipment-type-details/<int:id>",
        equipement.equipmentType_details,
        name="equipment_type_details",
    ),
    path(
        "equipment-type-delete/<int:id>",
        equipement.delete_equipmentType,
        name="equipment_type_delete",
    ),
    path("save-equipment", equipement.save_equipment, name="create_equipment"),
    path(
        "update-equipment/<int:id>",
        equipement.update_equipment,
        name="update_equipment",
    ),
    path(
        "equipment-details/<int:id>",
        equipement.equipment_details,
        name="equipment_details",
    ),
    path(
        "equipment-delete/<int:id>",
        equipement.delete_equipment,
        name="equipment_delete",
    ),
    path("client", client.client, name="client"),
    path("order", order.order, name="order"),
    path("stock", stock.stock, name="stock"),
    path("users", user.users, name="users"),
]
