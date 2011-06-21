from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

if not hasattr(settings, 'RECAPTCHA_PUBLIC_KEY') or not hasattr(settings, 'RECAPTCHA_PRIVATE_KEY'):
    raise ImproperlyConfigured(
        "recaptchapp requries RECAPTCHA_PUBLIC_KEY and RECAPTCHA_PRIVATE_KEY to be declared in settings.py"
        )
