from datetime import datetime
import peewee as pw

db = pw.SqliteDatabase('history_users.db')


class ModelBase(pw.Model):
    created_at = pw.DateField(default=datetime.now())

    class Meta():
        database = db


class History(ModelBase):
    user_id = pw.IntegerField()
    message = pw.TextField()
    self_req = pw.TextField()
