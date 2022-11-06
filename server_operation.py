from datetime import datetime


class Server(object):
    @staticmethod
    def send_msg(conn, msg, coder="utf-8"):
        conn.send(msg.encode(coder))

    @staticmethod
    def recv_msg(conn, buffer=1024, coder="utf-8"):
        return conn.recv(buffer).decode(coder)

    @staticmethod
    def server_created_date():
        dt = datetime.now()
        dt = dt.strftime("%d/%m/%Y %H:%M:%S")
        return dt

    def __init__(self):
        self.version = "Server v.4.2"
        self.created = Server.server_created_date()
        self.start_time = datetime.now()
        self.commands = {
            "help": "commands list with short description",
            "uptime": "return server life time",
            "info": "info about server version, server created date",
            "get_data_1": "Get 'SD' packet",
            "get_data_2": "Get 'M' packet",
            "stop": "connection closed (end client / server)",
        }

        self.handlers = {
            "info": self.show_server_info,
            "help": self.show_server_commands,
            "uptime": self.show_server_uptime,
            "get_data_1": self.get_data_1,
            "get_data_2": self.get_data_2,
            "stop": self.connection_closed,
        }

    def server_uptime(self):
        now = datetime.now()
        uptime = str(now - self.start_time)
        return uptime[:-7]

    def show_server_info(self, *args, **kwargs):
        return "info", f"{self.version} | created: {self.created}"

    def show_server_commands(self, *args, **kwargs):
        return "help", self.commands

    def show_server_uptime(self, *args, **kwargs):
        return "uptime", self.server_uptime()

    def get_data_1(self, *args, **kwargs):
        d = {1: '#SD', 2: "#04012011;135515;5544.6025;N;03739.6834;E;35;215;110;7"}
        return "get_data_1", d

    def get_data_2(self, *args, **kwargs):
        d = {1: '#M', 2: "#груз доставлен"}
        return "get_data_2", d

    def connection_closed(self, *args, conn):
        self.send_msg(conn, "CONNECTION CLOSED")
        print("CONNECTION CLOSED")


