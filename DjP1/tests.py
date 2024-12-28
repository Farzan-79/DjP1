import os
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.test import TestCase
from django.core.exceptions import ValidationError, ImproperlyConfigured

class DjP1Test (TestCase):
    def test_secret_key(self):
        try:
            validate_password(settings.SECRET_KEY)
        except ValidationError as e:
            msg = f'Weak Secret Key("{settings.SECRET_KEY}"): {e.messages}.'
            self.fail(msg)
        except ImproperlyConfigured as e:
            msg = 'no secret key found'
            self.fail(msg)
        self.assertNotEqual(settings.SECRET_KEY, 'fkn4850217184', 'you cannot have 0217184 as the secret key you dumbass')

    