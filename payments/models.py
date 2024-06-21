from django.db import models
from django.conf import settings
from courses.models import Course


# Create your models here.
class BankTransferPayment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    proof_of_payment = models.ImageField(upload_to='payments/proofs/')
    payment_status = models.CharField(max_length=50, choices=(('pending', 'Pending'), ('verified', 'Verified'), ('rejected', 'Rejected')))

    def __str__(self):
        return f'{self.user.username} - {self.course.title} - {self.amount}'

