# Создание базы данных MySQL для хранения логов
1. В файле create_db_log.py внести логин и пароль для доступа к базе
> host=<> \
> user=<> \
> password=<>

2. Далее выполнить скрипт:
> python create_db_log.py

# Парсинг лог-файлов в базу данных
1. В файле create_db_log.py внести логин и пароль для доступа к базе
> host=<> \
> user=<> \
> password=<>

Путь к лог-файлам для парсинга (по-умолчанию):
> /var/log/rsyslog_remote/mikrotik/

Имена лог-файлов для парсинга (по-умолчанию):
> input.log \
> output.log \
> forward.log \
> user.log \
> log.log \
> filter.log \
> script.log

2. Далее выполнить скрипт:
> python get_log_data.py
