from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm
from django.views.generic import DetailView


def feedback_home(request):
    feedback = Feedback.objects.order_by('-date')
    return render(request, 'feedback/feedback_home.html', {'feedback': feedback})

class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'feedback/feedback_detail_view.html'
    context_object_name = 'feedback'

def create_feedback(request):
    error = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_home')
        else:
            error = "Form isn't valid"

    form = FeedbackForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'feedback/create_feedback.html', data)
