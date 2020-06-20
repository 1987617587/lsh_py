from datetime import timedelta
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'ptask': {
        'task': 'tasks.period_task',
        'schedule': timedelta(seconds=5),
    },
}
CELERY_RESULT_BACKEND = 'redis://@127.0.0.1:6379/2'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True
'''
配置中 schedule 就是间隔执行的时间，这里可以用 datetime.timedelta 戒者 crontab
甚至太阳系经纬度坐标进行间隔时间配置
如果定时任务涉及到 datetime 需要在配置中加入时区信息，否则默认是以 utc 为准。例
如中国可以加上：
CELERY_TIMEZONE = 'Asia/Shanghai'
'''
