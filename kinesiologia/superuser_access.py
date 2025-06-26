from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

def superuser_required(function=None):
    """Decorator para views basadas en función: solo permite acceso a superusuarios."""
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_superuser,
        login_url='/login/'
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

class SuperuserRequiredMixin(UserPassesTestMixin):
    """Mixin para views basadas en clase: solo permite acceso a superusuarios."""
    login_url = '/login/'
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser
    def handle_no_permission(self):
        return redirect(self.login_url)
