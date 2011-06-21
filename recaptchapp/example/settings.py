

RECAPTCHA_PUBLIC_KEY = "ABC"
RECAPTCHA_PRIVATE_KEY = "XYZ"
RECAPTCHA_USE_SSL = True #This gets set from request.is_secure() when you use the {% recaptcha_options %} template tag
RECAPTCHA_OPTIONS = {
    #http://code.google.com/apis/recaptcha/docs/customization.html
    'theme' : 'custom',
    'custom_theme_widget': 'recaptcha_widget',
    #etc
}
