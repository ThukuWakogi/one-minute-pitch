from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User

# creating app instance
app = create_app('production')

# command to serve app
manager = Manager(app)
manager.add_command('server', Server)

# command to handle database migration
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# command to run unit tests. change app configuration to test
@manager.command
def test():
  '''
  run unit tests
  '''

  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)

# command to create shell to interact with database
@manager.shell
def make_shell_context():
  return dict(app=app, db=db, User=User)

if __name__ == "__main__":
    manager.run()
