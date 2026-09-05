from datetime import date, time

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Booking, Service


class BookingTrackingTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			username='booked-user',
			email='booked@example.com',
			password='StrongPass123!',
		)
		self.service = Service.objects.create(
			name='Cleaning',
			description='Home cleaning',
			price='500.00',
		)

	def create_booking(self):
		return Booking.objects.create(
			booked_by=self.user,
			name='Booked User',
			email=self.user.email,
			phone='1234567890',
			service=self.service,
			date=date(2026, 9, 10),
			time=time(10, 30),
			address='Test address',
		)

	def login(self):
		return self.client.post(reverse('login'), {
			'email': self.user.email,
			'password': 'StrongPass123!',
		})

	def test_user_with_booking_is_sent_to_tracker_after_login(self):
		self.create_booking()

		response = self.login()

		self.assertRedirects(response, reverse('my_bookings'))

	def test_booked_user_is_sent_to_tracker_even_with_booking_next_url(self):
		self.create_booking()

		response = self.client.post(
			reverse('login') + '?next=' + reverse('book_service'),
			{
				'email': self.user.email,
				'password': 'StrongPass123!',
				'next': reverse('book_service'),
			},
		)

		self.assertRedirects(response, reverse('my_bookings'))

	def test_user_without_booking_is_sent_home_after_login(self):
		response = self.login()

		self.assertRedirects(response, reverse('home'))

	def test_user_without_booking_cannot_open_tracker(self):
		self.client.force_login(self.user)

		response = self.client.get(reverse('my_bookings'))

		self.assertRedirects(response, reverse('home'))
