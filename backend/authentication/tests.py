from rest_framework.test import APITestCase
from .models import User, Employee, Employer
from .serializers import UserCreateSerializer, EmployeeSerializer
from rest_framework_simplejwt.tokens import AccessToken
from django.urls import reverse
from rest_framework import status


class TestCreateListEmployees(APITestCase):
    def setUp(self):
        self.url = reverse('create-list-employees')

        self.user1 = User.objects.create(
            email="ionescu@gmail.com",
            password="qwerty",
            is_employee=True
        )

        self.employee1 = Employee.objects.create(
            employee_id=self.user1,
            phone_number="07243456546",
            first_name="Vasile",
            last_name="Ionescu",
            birthdate="1990-3-12",
            country="Romania",
            city="Constanta",
            description="Nice guy",
        )

        self.user2 = User.objects.create(
            email="tudorescu@gmail.com",
            password="qwerty",
            is_employee=True
        )

        self.valid_request_body = {
            "id": self.user2.id,
            "phone_number": "07123456",
            "first_name": "George",
            "last_name": "Tudorescu",
            "birthdate": "2000-01-21",
            "country": "Romania",
            "city": "Iasi",
            "description": "A construction worker."
        }

        self.invalid_request_body = {
            "id": self.user2.id,
            "phone_number": "07123456",
            "first_name": "George",
        }

        self.request_body_with_id_of_other_credentials = {
            "id": self.user1.id,
            "phone_number": "07123456",
            "first_name": "George",
            "last_name": "Tudorescu",
            "birthdate": "2000-01-21",
            "country": "Romania",
            "city": "Iasi",
            "description": "A construction worker."
        }

    def test_employee_creation_with_valid_data(self):
        response = self.client.post(self.url, self.valid_request_body, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_employee_creation_with_invalid_data(self):
        response = self.client.post(self.url, self.invalid_request_body, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_employee_creation_using_the_credentials_of_another_employee(self):
        response = self.client.post(self.url, self.request_body_with_id_of_other_credentials, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_all_employees(self):
        self.client.post(self.url, self.valid_request_body, format='json')
        response = self.client.get(self.url)

        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(serializer.data, response.data)


class TestRetrieveUpdateEmployees(APITestCase):
    def setUp(self):
        self.update_url = reverse('retrieve-update-delete-employees', kwargs={"employee_id": 1})
        self.user1 = User.objects.create(
            email="ionescu@gmail.com",
            password="qwerty",
            is_employee=True
        )

        self.user2 = User.objects.create(
            email="tudorescu@gmail.com",
            password="qwerty",
            is_employee=True
        )

        self.employee1 = Employee.objects.create(
            employee_id=self.user1,
            phone_number="07243456546",
            first_name="Vasile",
            last_name="Ionescu",
            birthdate="1990-3-12",
            country="Romania",
            city="Constanta",
            description="Nice guy",
        )

        self.valid_request_body = {
            "employee_id": self.user1.id,
            "phone_number": "07123456",
            "first_name": "George",
            "last_name": "Tudorescu",
            "birthdate": "2000-01-21",
            "country": "Romania",
            "city": "Iasi",
            "description": "A construction worker."
        }

        self.invalid_request_body = {
            "employee_id": self.user1.id,
            "phone_number": "07123456",
            "first_name": "George",
        }

    def test_update_without_authentication(self):
        response = self.client.put(self.update_url, self.valid_request_body, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_with_wrong_authentication(self):
        token = AccessToken.for_user(self.user2)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.put(self.update_url, self.valid_request_body, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_with_valid_request_body(self):
        token = AccessToken.for_user(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.put(self.update_url, self.valid_request_body, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_with_invalid_request_body(self):
        token = AccessToken.for_user(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.put(self.update_url, self.invalid_request_body, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_existent_employee(self):
        url = reverse('retrieve-update-delete-employees', kwargs={'employee_id': self.user1.id})
        token = AccessToken.for_user(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_non_existent_employee(self):
        url = reverse('retrieve-update-delete-employees', kwargs={'employee_id': 2000})
        token = AccessToken.for_user(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)












