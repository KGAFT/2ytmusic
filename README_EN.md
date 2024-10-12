# yandex2ytmusic

**[Русский язык](README.md)**

Transfer liked tracks file to YouTube Music.

## Program Interface

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

## Usage

1. [Obtain your playlist as a file] with artist names and track titles. To export a playlist (including your favorite tracks) from Yandex Music to a suitable file, you can use the service: https://file.u-pov.ru/programs/YandexMusicExport/
2. Install dependencies and run the program:

```bash
pip install -r requirements.txt
python main.py --youtube <Path to file where youtube credentials will be stored> --file <Path to file with tracks>
```

3. When starting the program, follow the provided link to authorize in YouTube Music, allow access to the account, and press `Enter` to continue.
4. Wait for the program to finish. The program will also export music data to a JSON file:

```json
{
    // tracks from your file
    "liked_tracks":[
        {
            "artist": "Artist",
            "name": "Track Name"
        }
    ],
    // tracks not found during transfer
    "not_found":[], 
    // tracks that encountered an error during transfer
    "errors":[]
}
```

## Resources Used

- ytmusicapi - unofficial python API for YouTube Music

### P.S.

This fork was created due to the failure of the yandex-music API. And also in order to increase the coverage of services from which you can import tracks.
