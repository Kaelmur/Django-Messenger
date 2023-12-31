from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render


class MyPasswordResetView(UserPassesTestMixin, PasswordResetView):
    template_name = "users/password_reset.html"

    def test_func(self):
        return self.request.user.is_anonymous
