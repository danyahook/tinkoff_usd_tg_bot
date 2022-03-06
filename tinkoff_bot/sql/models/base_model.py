import peewee

database = peewee.PostgresqlDatabase('my_database', user='', password='')


class BaseModel(peewee.Model):

    class Meta:
        database = database
