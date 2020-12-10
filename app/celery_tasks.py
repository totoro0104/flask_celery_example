from app import celery as celery_app
from app.models import User


@celery_app.task(name='test')
def test():
    user = User.query.get(1)
    return user.username
