from peewee import *

mysql_db = MySQLDatabase(database='crud_python', password='12345', user='root', autocommit=True)


class BaseModel(Model):
    class Meta:
        database = mysql_db