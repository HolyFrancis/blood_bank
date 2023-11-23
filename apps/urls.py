from django.urls import path

from apps.views import home, user, donnor, transfusion, psl, analyse, equipement, hressource, client, order, stock

urlpatterns = [
    path("", home.home, name="home"),
    path("register", user.register, name="register"),
    path("donnor", donnor.donnor, name="donnor"),
    path("transfusion", transfusion.transfusion, name="transfusion"),
    path("psl", psl.psl, name="psl"),
    path("analyse", analyse.analyse, name="analyse"),
    path("equipement", equipement.equipement, name="equipement"),
    path("hressource", hressource.hressource, name="hressource"),
    path("client", client.client, name="client"),
    path("order", order.order, name="order"),
    path("stock", stock.stock, name="stock"),
]
