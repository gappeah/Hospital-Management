from django.shortcuts import render, redirect
def BASE(request):
    return render(request,'base.html')

def ADD_PATIENT(request):
    return render(request,'patients/add_patient.html')