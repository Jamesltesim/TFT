from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app,db

manager = Manager(app)

# 使用migrate绑定app和db
migrate = Migrate(app,db)

# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()


    # 目前只能检测 表字段增加或者删除
    # 不能检测 表字段的修改
    # python manage.py db init

    # python manage.py db migrate - m "desc"

    # python manage.py db upgrade
