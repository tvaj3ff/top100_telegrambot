#   KinoMaster3bot
KinoMaster3Bot – это Telegram-бот, который поможет вам открыть для себя топ-100  
лучших фильмов всех времён и получить подробную информацию о каждом из них,  
включая название, описание, оценку и год выпуска.

## Описание
Этот бот предоставляет удобный и быстрый доступ к информации о лучших фильмах  
всех времён. Вы можете получить список топ-100 фильмов, выбрать интересующий  
вас фильм и узнать все необходимые детали.

## Установка
Следуйте этим инструкциям для установки и запуска KinoMaster3bot:  
Клонируйте репозиторий на ваш локальный компьютер:
```bash
git clone https://gitlab.skillbox.ru/dzheffri_tagne/python_basic_diploma.git
cd kinomaster3_bot
```

Создайте виртуальное окружение и активируйте его:
```bash
python3 -m venv venv
source venv/bin/activate  # для Windows используйте `venv\Scripts\activate`
```

Установите необходимые **зависимости**:
```bash
pip install -r requirements.txt
```

Создайте файл `.env` в корне проекта и добавьте в него ваш Telegram API токен  
и RapidAPI ключ:
```env
BOT_TOKEN = your_telegram_api_token
RAPIDAPI_KEY=your_rapidapi_key
```
Запустите бота:

```bash
python main.py
```
## Использование
После запуска бота, вы можете взаимодействовать с ним в Telegram, используя  
следующие команды:

- `/start` – Запуск бота;
- `/help` - помощь по командам бота;
- `/helloworld` - Анекдот про выражение **"Hello world"**;
- `/history` - Вывод истории 10 последних запросов пользователей;
- `/hundred_list` – Показать топ-100 фильмов и получить информацию  
о конкретном фильме;
- `/low` - Показать фильмов №1 из топ-100 (Название, описание, оценка,  
год выпуска и обложка);
- `/high` - Показать фильмов №100 из топ-100 (Название, описание, оценка,  
год выпуска и обложка).

## Зависимости
- [pyTelegramBotAPI](https://pytba.readthedocs.io/en/latest/index.html)
- [requests](https://requests.readthedocs.io/en/latest/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [peewee](https://docs.peewee-orm.com/en/latest/)

### RapidAPI
KinoMaster3Bot использует API из [RapidAPI.com](https://rapidapi.com/rapihub-rapihub-default/api/imdb-top-100-movies/playground/apiendpoint_e356f09e-d37e-4eab-b36b-28ed1e4f95e2)
для получения списка топ-100 фильмов и детальной информации о них.
Убедитесь, что у вас есть действующий ключ API, чтобы бот мог получать данные.
## Разработка
Если вы хотите внести свой вклад в проект, выполните следующие шаги:  
Форкните этот репозиторий
Создайте новую ветку.
Внесите свои изменения и закоммитьте их.
Запушьте изменения в свою ветку.
Создайте новый Pull Request.

## Лицензия
Этот проект не имеет лицензии.

## Контакты
Если у вас есть вопросы или предложения, пожалуйста, свяжитесь со мной  
по электронной почте: jeffjeffreytagne@gmail.com.
