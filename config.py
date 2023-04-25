import configparser
import time


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

    def SetTime(self, period_time):
        l_time = int(time.time())
        self.config.set('time', 'last_time', str(l_time))
        self.config.set('time', 'period_time', period_time)
        with open('config.ini', 'w') as f:
            self.config.write(f)

    def GetPeriod(self) -> int:
        if not self.config.get('time', 'period_time', fallback='0'):
            return 0
        return self.config.getint('time', 'period_time', fallback=0)

    def GetLastTime(self) -> int:
        if not self.config.get('time', 'last_time', fallback='0'):
            return 0
        return self.config.getint('time', 'last_time', fallback=0)

    def SetRepeat(self, repeat):
        self.config.set('time', 'repeat', str(repeat))
        with open('config.ini', 'w') as f:
            self.config.write(f)

    def GetRepeat(self) -> bool:
        if not self.config.get('time', 'repeat', fallback='0'):
            return 0
        return self.config.getint('time', 'repeat', fallback=0)
