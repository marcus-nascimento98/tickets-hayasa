from datetime import datetime
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import logout

def timestamp():
    return int(datetime.now().timestamp())

class SessionTimeoutMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')

            if last_activity:
                elapsed_time = timestamp() - last_activity
                if elapsed_time > settings.SESSION_COOKIE_AGE:
                    logout(request)
                    return redirect('login') 

            request.session['last_activity'] = timestamp()

        return self.get_response(request)
