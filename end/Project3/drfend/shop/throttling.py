from rest_framework import throttling


class MyAnon(throttling.AnonRateThrottle):
    THROTTLE_RATES = {
        'anon': '3/minutes'
    }


class MyUser(throttling.UserRateThrottle):
    THROTTLE_RATES = {
        'user': '8/minutes'
    }
