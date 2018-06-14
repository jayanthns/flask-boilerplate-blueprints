import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from application import create_app, db

from models.users import User

app = create_app(config_name=os.getenv('env') or 'dev')

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    manager.run()