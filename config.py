import configparser


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        if not self.config.has_section('database'):
            self.config.add_section('database')
        if not self.config.has_section('time'):
            self.config.add_section('time')
        # 读取参数
        self.db_host = self.config.get(
            'database', 'host', fallback='localhost')
        self.db_port = self.config.getint('database', 'port', fallback='8000')
        self.db_user = self.config.get('database', 'username', fallback='user')
        self.db_password = self.config.get(
            'database', 'password', fallback='user')
        self.db_name = self.config.get('database', 'database', fallback='db')
        self.web_port = self.config.getint('web', 'port', fallback='1024')

        # 修改参数
        self.config.set('database', 'password', 'newpassword')

        # 保存到文件
        with open('config.ini', 'w') as f:
            self.config.write(f)

    def SetTime(self, time):
        self.config.set('time', 'last_time', time)
        with open('config.ini', 'w') as f:
            self.config.write(f)
