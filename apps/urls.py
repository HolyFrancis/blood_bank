from django.contrib.auth import views as auth_views
from django.urls import path

from apps.views import analyse, client, donor, equipement, home, order, psl, stock, transfusion, user

urlpatterns = [
    #-------------------------------User related-------------------------------
    path("login", user.loginview, name="login"),
    path("register", user.register, name="register"),
    path("logout", user.logoutview, name="logout"),
    path("users", user.users, name="users"),
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
    path("change_password/", auth_views.PasswordChangeView.as_view(template_name = "apps/user/change_password.html"), name="change-password"),
    path("password_success/", user.password_success, name="password_success"),
    
    
    path("", home.home, name="home"),
    
    
    #-------------------------------Donor-------------------------------
    path("donor", donor.donor, name="donor"),
    path("create-donor", donor.create_donor, name="create_donor"),
    path("update-donor/<str:id>", donor.update_donor, name="update_donor"),
    path("donor-details/<str:id>", donor.donor_details, name="donor_details"),
    path("delete-donor/<str:id>", donor.delete_donor, name="delete_donor"),
    
    
    #-------------------------------Transfusion-------------------------------
    path("blood", transfusion.blood, name="transfusion"),
    path("create-transfusion", transfusion.create_blood, name="create_blood"),
    path("update-transfusion/<int:id>/", transfusion.update_blood, name="update_blood"),
    path("blood-transfusion/<int:id>/", transfusion.blood_details, name="blood_details"),
    path("blood-delete/<int:id>", transfusion.blood_delete, name="delete_blood"),
    
    
    #-------------------------------Type-psl-------------------------------
    path("create-type-psl", psl.create_type_PSL, name="create_type_psl"),
    path("update-type-psl/<int:id>", psl.update_type_psl, name="update_type_psl"),
    path("type-psl-details/<int:id>", psl.type_psl_details, name="type_psl_details"),
    path("type-psl-delete/<int:id>", psl.type_psl_delete, name="type_psl_delete"),
    
    
    #-------------------------------psl-------------------------------
    path("psl", psl.psl, name="psl"),
    path("create-psl", psl.create_psl, name="create_psl"),
    path("update-psl/<int:id>", psl.update_psl, name="update_psl"),
    path("psl-details/<int:id>", psl.psl_details, name="psl_details"),
    path("psl-delete/<int:id>", psl.psl_delete, name="psl_delete"),
    
    
    #-------------------------------analyse-------------------------------
    path("analyse", analyse.analyse, name="analyse"),
    path("create-analysis", analyse.create_analysis, name="create_analysis"),
    path("update-analysis/<str:id>", analyse.update_analysis, name="update_analysis"),
    path("delete-analysis/<str:id>", analyse.delete_analysis, name="delete_analysis"),
    
    
    #-------------------------------equipment-type-------------------------------
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
    
    
    #-------------------------------Equipment-------------------------------
    path("equipement", equipement.equipement, name="equipement"),
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
    
    
    #-------------------------------Client-------------------------------
    path("client", client.client, name="client"),
    path("create-client", client.create_client, name="create_client"),
    path("update-client/<str:id>", client.update_client, name="update_client"),
    path("client-details/<str:id>", client.client_details, name="client_details"),
    path("delete-client/<str:id>", client.delete_client, name="delete_client"),
    
    
    #-------------------------------Order-------------------------------
    path("order", order.order, name="order"),
    path("create-order", order.create_order, name="create_order"),
    path("update-order/<str:id>", order.update_order, name="update_order"),
    path("delete-order/<str:id>", order.delete_order, name="delete_order"),


    path("stock", stock.stock, name="stock"),
    path("create-stock", stock.create_stock, name="create_stock"),
    path("update-stock/<str:id>", stock.update_stock, name="update_stock"),
    path("delete-stock/<str:id>", stock.delete_stock, name="delete_stock"),

    
    path("create-location", stock.create_location, name="create_location"),
    path("update-location/<str:id>", stock.update_location, name="update_location"),
    path("delete-location/<str:id>", stock.delete_location, name="delete_location"),
    

    
    
    #-------------------------------Stock-------------------------------
    path("stock", stock.stock, name="stock"),
    
    
    #-------------------------------Users-------------------------------
    path("users", user.users, name="users"),
]
