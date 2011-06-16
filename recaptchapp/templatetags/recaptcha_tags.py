from django.conf import settings
from django.utils import simplejson
from django.utils.translation import get_language_from_request
from django import template
register = template.Library()


@register.inclusion_tag("recaptcha_options.dtml", takes_context=True)
def recaptcha_options(context):
    """ Template tag which displays the <script/> tag with settings for ReCaptcha.
        Also takes the opportunity to set settings.RECAPTCHA_USE_SSL based on request.is_secure().
    """
    request = context['request']
    set_recaptcha_ssl(request)
    recaptcha_options = {}
    if hasattr(settings, 'RECAPTCHA_OPTIONS'):
        recaptcha_options.update(settings.RECAPTCHA_OPTIONS)
    recaptcha_options['lang'] = get_language_from_request(request) #returns a language code
    return {
        'recaptcha_options_json': simplejson.dumps(recaptcha_options)
    }




def set_recaptcha_ssl(request):
    """ Change settings.RECAPTCHA_USE_SSL depending on request.is_secure(). """
    settings.RECAPTCHA_USE_SSL = request.is_secure()


