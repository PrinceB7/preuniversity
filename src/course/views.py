from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Subject, Topics


@login_required
def dashboard(request):
    all_subjects = Subject.objects.all()
    return render(request, 'dashboard.html', {'subjects': all_subjects})


@login_required
def detail_of_subject(request, name):
    subject = get_object_or_404(Subject, name=name)
    topics = subject.topics.all()
    return render(request, 'detail_of_subject.html', {'subject': subject, 'topics': topics})


def detail_of_topic(request, topic_title):
    current_topic = get_object_or_404(Topics, title=topic_title)
    return render(request, 'detail_of_topic.html', {'topic': current_topic})
