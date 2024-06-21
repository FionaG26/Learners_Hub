from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('bank-transfer/<int:course_id>/', views.bank_transfer_payment, name='bank_transfer_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
]
