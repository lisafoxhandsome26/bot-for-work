import json
from typing import Dict

import requests

from config_data.config import RAPID_API_KEY, RAPID_API_HOST, url_adres
from API_requests.processing.proces import Take_analiz
from API_requests.form_data.form_data import Take_form


def make_request(params: Dict, user_ch: str) -> str:
	headers = {
		"X-RapidAPI-Key": RAPID_API_KEY,
		"X-RapidAPI-Host": RAPID_API_HOST
	}

	response = requests.get(url_adres, headers=headers, params=params)

	if response.ok:
		data = json.loads(response.text)
		if len(data.get('data')) != 0:
			new_data = Take_analiz.analiz_data()
			prep_data = new_data(data, user_ch)

			form_d = Take_form.take_form()
			redy = form_d(prep_data)

			return redy
		return 'Ошибка поиска, возможно данные введены не верно!'
	return 'Ошибка сервер не отвечает!'
