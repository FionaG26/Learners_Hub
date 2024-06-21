from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import BankTransferPaymentForm
from courses.models import Course

@login_required
def bank_transfer_payment(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = BankTransferPaymentForm(request.POST, request.FILES)
        if form.is_valid():
            bank_payment = form.save(commit=False)
            bank_payment.user = request.user
            bank_payment.course = course
            bank_payment.amount = course.price  # Assuming each course has a price field
            bank_payment.payment_status = 'pending'
            bank_payment.save()
            return redirect(reverse('payment_success'))
    else:
        form = BankTransferPaymentForm(initial={'course': course, 'amount': course.price})

    return render(request, 'payments/bank_transfer_payment.html', {'form': form, 'course': course})

def payment_success(request):
    return render(request, 'payments/payment_success.html')
