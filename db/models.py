from django.db.models import CharField
from ..fields import ReCaptchaField as ReCaptchaFormField #don't clash our form field class with our model field class


class ReCaptchaField(CharField):
    """ Just like a normal CharField but uses a recaptchapp.fields.ReCaptchaField as its form field. """
    
    def formfield(self, form_class=None, **kwargs):
        """ Just call the standard CharField's formfield method, but pass the ReCaptchaFormField as the field class. """
        form_class = form_class or ReCaptchaFormField
        return super(CharField, self).formfield(form_class=form_class, **kwargs)


