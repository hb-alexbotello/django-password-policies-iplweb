try:
    from django.urls import re_path as url
    from django.urls import path
except ImportError:
    # Before Django 2.0
    from django.conf.urls import url, path

import django.conf.urls
if hasattr(django.conf.urls, 'patterns'):
    # patterns was deprecated in Django 1.8
    from django.conf.urls import patterns
else:
    # patterns is unavailable in Django 1.10+
    patterns = False

from password_policies.views import (
    PasswordChangeDoneView,
    PasswordChangeFormView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetFormView,
)

urlpatterns = [
    url(
        r"^change/done/$", PasswordChangeDoneView.as_view(), name="password_change_done"
    ),
    url(r"^change/$", PasswordChangeFormView.as_view(), name="password_change"),
    url(r"^reset/$", PasswordResetFormView.as_view(), name="password_reset"),
    url(
        r"^reset/complete/$",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path(
        'reset/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    url(r"^reset/done/$", PasswordResetDoneView.as_view(), name="password_reset_done"),
]

if patterns:
    # Django 1.7
    urlpatterns = patterns("", *urlpatterns)
