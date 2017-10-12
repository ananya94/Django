from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone
from .models import Course,Step

# Create your tests here.

class CourseModelTest(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title = "Python Regex",
            description = "Learn to write regular expressions in Python"
        )
        now = timezone.now()
        self.assertLessEqual(course.created_at, now)

class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
        title = "Python testing",
        description = "learn how to test in python"
        )
        self.course2 = Course.objects.create(
        title= "New Course",
        description = "A new course"
        )
        self.step = Step.objects.create(
            title="Intro to doctest",
            description = "learn to write tests in docstrings",
            course=self.course
        )
    def test_course_list_view(self):
        resp=self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course,resp.context['courses'])
        self.assertIn(self.course2,resp.context['courses'])
