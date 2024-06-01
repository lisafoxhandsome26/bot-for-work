from databasa.utils.CRUD import CRUDInteface
from databasa.common.models import db, History

db.connect()
db.create_tables([History])


crud = CRUDInteface()


if __name__ == "main":
    crud()
