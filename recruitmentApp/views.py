from django.shortcuts import redirect, render
from .forms import RecruitmentApplicationForm
from siteinfoApp import data


def recruitment(request):
    if request.method == 'POST':
        form = RecruitmentApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recruitment:success')
    else:
        form = RecruitmentApplicationForm()
    return render(request, 'recruitment.html', {
        'form': form,
        'faq': data.FAQ,
    })


def success(request):
    return render(request, 'success.html')
