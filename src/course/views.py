from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Subject, Topic, Homework
from registration.models import RegistrationProfile


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
    return render(request, 'course-detail.html', {'subject': subject, 'topics': topics, 'homeworks': homeworks,
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
    n_of_teachers = RegistrationProfile.objects.filter(is_teacher=True).count()
    n_of_members = RegistrationProfile.objects.filter(is_teacher=False).count()
    return render(request, 'index.html', {'courses': all_subjects, 'n_of_teacher': n_of_teachers, 'n_of_student': n_of_members})
