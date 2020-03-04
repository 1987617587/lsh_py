from rest_framework import throttling


class MyAnon(throttling.AnonRateThrottle):
    THROTTLE_RATES = {
        'anon': '100/minutes'
    }


class MyUser(throttling.UserRateThrottle):
    THROTTLE_RATES = {
        'user': '100/minutes'
    }
