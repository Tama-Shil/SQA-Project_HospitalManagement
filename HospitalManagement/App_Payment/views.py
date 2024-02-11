from django.shortcuts import render, redirect
from .forms import advancePaymentForm,  emiPaymentForm
from .models import PaymentModel

def selectPaymentMethod(request):
  
    if request.method == 'POST':
        selectedMethod = request.POST.get('payment_method')
        if selectedMethod  == 'advance':
            return redirect('advance_payment_form')
        elif selectedMethod  == 'emi':
            return redirect('emi_payment_form')

    return render(request, 'selectPaymentMethod.html')

def advancePayment(request):

    if request.method == 'POST':
        form = advancePaymentForm(request.POST)
        if form.is_valid():
            advancepatientId = form.cleaned_data['advancepatientId']
            advanceTotalAmount = form.cleaned_data['advanceTotalAmount']
            payment = PaymentModel.objects.create(patientId=advancepatientId, totalAmount=advanceTotalAmount)
            return render(request, 'advancePaymentSuccess.html', {'payment': payment})
    else:
        form = advancePaymentForm()

    return render(request, 'payBill.html', {'form': form})



def emiPayment(request):

    if request.method == 'POST':
        form = emiPaymentForm(request.POST)
        if form.is_valid():
            emipatientId= form.cleaned_data['emipatientId']
            emitTotalAmount = form.cleaned_data['emitTotalAmount']
            emiTimeStamp = form.cleaned_data['emiTimeStamp']
            payment = PaymentModel.objects.create(patientId=emipatientId, totalAmount=emitTotalAmount, timeStamp=emiTimeStamp)
            return render(request, 'payment_success.html', {'payment': payment})
    else:
        form = emiPaymentForm()

    return render(request, 'payEMI.html', {'form': form})

def payment_success(request):

    latest_payment = PaymentModel.objects.filter(m_isSuccess=True).order_by('-id').first()

    return render(request, 'payment_success.html', {'latest_payment': latest_payment})
