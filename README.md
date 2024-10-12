# 2ytmusic

**[English](README_EN.md)**

Перенос понравившихся треков из файла в YouTube Music.

## Интерфейс программы

```bash
python main.py --help                                                         
usage: main.py [-h] [--file FILE] [--output OUTPUT] [--youtube YOUTUBE]

Transfer tracks from file to YouTube Music

options:
  -h, --help         show this help message and exit
  --file FILE        File with liked tracks. You can find example in root of project
  --output OUTPUT    Output json file
  --youtube YOUTUBE  Youtube Music credentials file. If file not exists, it will be created.
```

## Использование

1. Получить ваш плейлист в виде файла с названиями артистов и названием треков. Для экспорта плейлиста(в том числе и понравившихся треков) из Яндекс музыки в подходящий файл можно воспользоваться сервисом: https://file.u-pov.ru/programs/YandexMusicExport/
2. Установить зависимости и запустить программу:
```bash
pip install -r requirements.txt
python main.py --youtube <Path to file where youtube credentials will be stored>
```
3. При запуске программы перейти по предложенной ссылке для авторизации в YouTube Music, разрешить доступ к аккаунту и нажать `Enter` для продолжения.
4. Дождаться завершения работы программы. Программа также экспортирует музыку Json в файл:

```json
{
    // треки из плейлиста
    "liked_tracks":[
        {
            "artist": "Исполнитнль",
            "name": "Название трека"
        }
    ],
    // треки, которые не были найдены при переносе
    "not_found":[], 
    // треки, при переносе которых произошла ошибка
    "errors":[]
}
```

## Используемые ресурсы

- ytmusicapi - не официальное python API YouTube Music

### P.s.

Данный форк был создан по причине отказа работы yandex-music API. А также с целью увеличить охват сервисов откуда можно сделать импорт треков

