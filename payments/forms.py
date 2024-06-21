from django import forms
from .models import BankTransferPayment

class BankTransferPaymentForm(forms.ModelForm):
    class Meta:
        model = BankTransferPayment
        fields = ['course', 'amount', 'proof_of_payment']
        widgets = {
            'course': forms.HiddenInput(),
            'amount': forms.HiddenInput(),
            'proof_of_payment': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'placeholder': 'Upload proof of payment',
            }),
        }
        labels = {
            'proof_of_payment': 'Proof of Payment',
        }
        help_texts = {
            'proof_of_payment': 'Upload an image or screenshot of your payment receipt.',
        }

    def __init__(self, *args, **kwargs):
        super(BankTransferPaymentForm, self).__init__(*args, **kwargs)
        self.fields['proof_of_payment'].widget.attrs.update({'class': 'form-control'})
        self.fields['proof_of_payment'].label = "Upload Proof of Payment"
        self.fields['proof_of_payment'].help_text = "Please upload a clear image of your bank transfer receipt."
