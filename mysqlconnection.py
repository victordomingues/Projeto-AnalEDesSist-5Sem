import mysql.connector
import collections
def _convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(_convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(_convert, data))
    else:
        return data

class MySQLConnection(object):

    def __init__(self, bdgbg):

        self.config = {
            'user': 'root',
            'password': 'bdvictor2002$',
            'database': bdgbg,
            'host': 'localhost',

        }
        self.conn = mysql.connector.connect(**self.config)

    def fetch(self, query):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query)
        data = list(cursor.fetchall())
        cursor.close()
        return _convert(data)

    def run_mysql_query(self, query):
        cursor = self.conn.cursor(dictionary=True)
        data = cursor.execute(query)
        self.conn.commit()
        cursor.close()
        return data
    def escape_string(self, query):
        string_escaper = self.conn.converter.escape
        escaped_string = string_escaper(query)
        return escaped_string

def MySQLConnector(bdgbg):
    return MySQLConnection(bdgbg)