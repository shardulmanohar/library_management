from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from library_app.models import AdminUser, Book
from rest_framework_simplejwt.tokens import RefreshToken

class LibraryTests(APITestCase):

    def setUp(self):
        # Create admin user
        self.admin = AdminUser.objects.create_user(email="testadmin@email.com", username="testadmin", password="adminpass123")
        self.token = RefreshToken.for_user(self.admin).access_token
        self.auth_headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.token}"
        }

    def test_admin_signup(self):
        url = reverse("admin-signup")
        data = {
            "email": "newadmin@email.com",
            "username": "newadmin",
            "password": "newadminpass"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_admin_login(self):
        url = reverse("admin-login")
        data = {
            "email": "testadmin@email.com",
            "password": "adminpass123"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
    def test_create_book(self):
        url = reverse("book-list-create")
        data = {
            "title": "New Book",
            "author": "John Doe",
            "publication_date": "2024-01-01",
            "isbn": "1234567890"
        }
        response = self.client.post(url, data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_books(self):
        Book.objects.create(title="Book 1", author="Author 1", publication_date="2024-01-01", isbn="isbn-list-1")
        Book.objects.create(title="Book 2", author="Author 2", publication_date="2023-05-15", isbn="isbn-list-2")
        response = self.client.get(reverse("book-list-create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_update_book(self):
        book = Book.objects.create(title="Old Title", author="Old Author", publication_date="2023-06-10", isbn="isbn-old")
        url = reverse("book-detail-update-delete", args=[book.id])
        data = {
            "title": "Updated Title",
            "author": "New Author",
            "publication_date": "2024-03-01",
            "isbn": "isbn-updated"
            }
        response = self.client.put(url, data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_delete_book(self):
        book = Book.objects.create(title="Delete Me", author="Author X", publication_date="2022-12-12", isbn="isbn-delete")
        url = reverse("book-detail-update-delete", args=[book.id])
        response = self.client.delete(url, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    def test_duplicate_admin_signup(self):
        url = reverse("admin-signup")
        data = {
            "email": "testadmin@email.com",  # Already used in setUp()
            "username": "testadmin",
            "password": "duplicatepass"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_with_wrong_password(self):
        url = reverse("admin-login")
        data = {
            "email": "testadmin@email.com",
            "password": "wrongpassword"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_without_auth(self):
        url = reverse("book-list-create")
        data = {
            "title": "Unauthorized Book",
            "author": "No Auth"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_nonexistent_book(self):
        url = reverse("book-detail-update-delete", args=[999])
        data = {
            "title": "Does Not Exist",
            "author": "Ghost"
        }
        response = self.client.put(url, data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_nonexistent_book(self):
        url = reverse("book-detail-update-delete", args=[999])
        response = self.client.delete(url, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_view_books_unauthenticated(self):
        url = reverse("book-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
