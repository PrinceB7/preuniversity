from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Subject, Topic, Homework


@login_required
def dashboard(request):
    all_subjects = Subject.objects.all()
    return render(request, 'dashboard.html', {'subjects': all_subjects})


@login_required
def detail_of_subject(request, name):
    subject = get_object_or_404(Subject, slug=name)
    topics = subject.topics.all()
    quizzes = subject.quizzes.all()
    homeworks = Homework.objects.filter(subject__name=name)
    return render(request, 'detail_of_subject.html', {'subject': subject, 'topics': topics, 'homeworks': homeworks,
                                                      'quizzes': quizzes})


@login_required
def detail_of_topic(request, topic_title):
    current_topic = get_object_or_404(Topic, slug=topic_title)
    return render(request, 'detail_of_topic.html', {'topic': current_topic})


def detail_of_homework(request, title):
    homework = Homework.objects.get(slug=title)
    return render(request, 'detail_of_homework.html', {'homework': homework})


def index(request):
    all_subjects = Subject.objects.all()
    return render(request, 'index.html', {'courses': all_subjects})
