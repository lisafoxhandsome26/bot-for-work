from typing import Dict, List


def _make_sort_data(list_job: List, user_ch: str) -> List:
    for elem in list_job:
        if not isinstance(elem.get('job_min_salary'), int):
            elem['job_min_salary'] = 0

    list_job = sorted(list_job, key=lambda K: K.get('job_posted_at_datetime_utc'), reverse=True)

    if user_ch == 'высокие':
        ready_obj = sorted(list_job[:5], key=lambda K: K.get('job_min_salary'), reverse=True)
        return ready_obj

    list_job = sorted(list_job[:5], key=lambda K: K.get('job_min_salary'))
    return list_job


def _choice_data(data: Dict, user_ch: str) -> (List, str):
    try:
        my_list = data.get('data')
        if len(my_list) >= 5:
            ready_list = _make_sort_data(my_list, user_ch)
            return ready_list
        else:
            ready_list = _make_sort_data(my_list, user_ch)
            return ready_list
    except (TypeError, KeyError):
        return 'Ошибка: некоторых данных не существует'


class Take_analiz():

    @staticmethod
    def analiz_data():
        return _choice_data


if __name__ == '__main__':
    _choice_data()
    Take_analiz()
