from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
BASE_DIR_PARENT = Path(__file__).resolve().parent.parent

command = f'{BASE_DIR}/venv/bin/gunicorn'
pythonpath = f'{BASE_DIR}'
bind = '0.0.0.0:8000'
workers = 5
user = 'kirill2'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=config.settings'