from databasa.core import crud, db, History


def select_datas(user: int) -> str:

    db_read = crud.retrieve()
    result = db_read(db, History, History.created_at, History.message, History.self_req).\
        where(user == History.user_id).order_by(-History.id).limit(5)

    message_text = ''
    for elem in result:
        text_massage = f'Дата запроса - {elem.created_at}\n' \
                       f'Сообщение - {elem.message}\n\n'
        message_text += text_massage
    return message_text


datas = {'user_id': None, 'self_req': None, 'message': None}


def write_datas() -> None:
    db_write = crud.create()
    db_write(db, History, datas)
