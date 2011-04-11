from django import forms
from .models import MyModel
from recaptchapp.fields import ReCaptchaField



class MyModelForm(forms.Modelform):
    """ This form will get a recaptcha form field automatically beacuse we have got a recaptcha model field on the model. """
    
    class Meta:
        model = MyModel



class MyForm(forms.Form):
    """ This is a plain, non-model form.  We can add the recaptcha form field directly. """
    
    captcha = ReCaptchaField()



