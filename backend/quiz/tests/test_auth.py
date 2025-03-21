from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from quiz.models import Question


class QuestionAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='benjamin', password='123456')
        self.client.login(username='benjamin', password='123456')
        self.question = Question.objects.create(text="What is 2+2?", category="math", difficulty=1)

    def test_get_questions(self):
        """Test retrieving questions list"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/questions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_question(self):
        """Test creating a new question"""
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/questions/', {
            "text": "What is the capital of France?",
            "category": "verbal",
            "difficulty": 2
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
