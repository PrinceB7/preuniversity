from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic, Homework
from registration.models import RegistrationProfile
from quiz.models import Quiz
from app.models import Testimonial


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def detail_of_subject(request, name):
    topics = Topic.objects.filter(subject__exact=name)
    quizzes = Quiz.objects.filter(subject__exact=name)
    homeworks = Homework.objects.filter(subject__exact=name)
    return render(request, 'course-detail.html', {'subject': name, 'topics': topics, 'homeworks': homeworks,
                                                'quizzes': quizzes})


@login_required
def detail_of_topic(request, topic_title):
    current_topic = get_object_or_404(Topic, slug=topic_title)
    return render(request, 'detail_of_topic.html', {'topic': current_topic})


def detail_of_homework(request, title):
    homework = Homework.objects.get(slug=title)
    return render(request, 'detail_of_homework.html', {'homework': homework})


def index(request):
    n_of_teachers = RegistrationProfile.objects.filter(is_teacher=True).count()
    n_of_members = RegistrationProfile.objects.filter(is_teacher=False).count()
    n_of_topics = Topic.objects.count()
    testimonials = Testimonial.objects.all()[:5]
    return render(request, 'index.html', {'n_of_teacher': n_of_teachers, 'n_of_student': n_of_members, 'n_of_topics': n_of_topics,
                                          'testimonials': testimonials})
