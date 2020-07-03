from django.urls import path
from payments.views import (
    view_cards,
    add_card,
    delete_card,
    handle_payment ,
    handle_payment_process,
    payment_done,
    payment_failed
)


app_name = 'payments'

urlpatterns = [
    path('cards/', view=view_cards, name='view_card'),
    path('cards/add/', view=add_card, name='add_card'),
    path('cards/delete/<str:card_id>/', view=delete_card, name='delete_card'),
    path('pay/', view=handle_payment, name='pay'),
    path('process/', view=handle_payment_process, name='process'),
    path('done/', view=payment_done, name='done'),
    path('failed/',view=payment_failed, name='failed'),
]

