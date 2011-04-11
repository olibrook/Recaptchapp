from django.db import models
from recaptchapp.db.models import ReCaptchaField

class MyModel(models.Model):
    """ A model which has a ReCaptchaField on it.  The submitted text from the form field will be saved on the model. """
    
    captcha = ReCaptchaField(max_length=500) #currently requires the max_length argument because it extends from CharField, feel free to fix it.



