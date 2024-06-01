from typing import List


def _form_data(data: List) -> str:
    message_text = ''
    for elem in data:
        if elem.get("job_min_salary") == 0:
            elem["job_min_salary"] = 'Договорная'
        if elem.get("job_salary_currency") is None:
            elem["job_salary_currency"] = 'Any'

        data_time = elem.get("job_posted_at_datetime_utc")[:-4].replace('T', ' ')

        text_massage = f'🔥 {elem.get("job_title")}\n' \
                       f'Компания - {elem.get("employer_name")}\n' \
                       f'Зароботная плата - {elem.get("job_min_salary")} {elem.get("job_salary_currency")}\n' \
                       f'Город - {elem.get("job_city")}\n' \
                       f'Режим работы - {elem.get("job_employment_type")}\n' \
                       f'url компании - {elem.get("employer_website")}\n' \
                       f'Дата размещения - {data_time}\n\n'
        message_text += text_massage
    return message_text


class Take_form():

    @staticmethod
    def take_form():
        return _form_data


if __name__ == '__main__':
    _form_data()
    Take_form()
