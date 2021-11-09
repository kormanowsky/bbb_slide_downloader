# bbb_slide_downloader
Программа на Python, которая скачивает презентации в формате PDF. 
__Важно!__ Программа работает только во время лекции. 

# Установка 
```bash 
git clone git@github.com:kormanowsky/bbb_slide_downloader.git
cd bbb_slide_downloader
pip3 install -r requirements.txt
```

# Программа использует ChromeDriver для имитации работы браузера Google Chrome. Если Ваша версия Google Chrome отличается от версии ChromeDriver по умолчанию:
Если у Вас установлена версия Chrome, отличная от версии драйвера, находящегося в этом репозитории, Вам необходимо скачать и поместить в соответствующую папку (chromedriver/(linux/macos/windows)) нужную Вам версию ChromeDriver, а также выдать права на исполнение. 
Скачать ChromeDriver: https://sites.google.com/a/chromium.org/chromedriver/downloads (старая ссылка) https://sites.google.com/chromium.org/driver/downloads (новая)

__С 06.12.2020 версия по умолчанию - 87__

### Для пользователей macOS: 
Чтобы chromedriver запустился, нужно нажать ctrl и кликнуть по файлу в Finder. 

# Запуск 
```bash 
python3 main.py
```
По запросу программы введите ссылку (из почты/вк) и имя выходного файла. 

# По всем вопросам: 

Создавайте новый issue.
