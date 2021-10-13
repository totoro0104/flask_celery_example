from flask_migrate import MigrateCommand
from flask_script import Manager, Shell

from app import app, db
from app.models import User
from app.route import generate_routes

generate_routes(app)
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def init_db():
    """
    Init a local database. You probably should not use this on production.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def create_superuser():
    user = User(username='admin', password='123')
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
