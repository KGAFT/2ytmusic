import argparse
import json

from core import YoutubeImoirter
from core import Track

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Transfer tracks from file to YouTube Music'
    )
    parser.add_argument(
        '--file', type=str, help='File with liked tracks. You can find example in root of project'
    )
    parser.add_argument(
        '--output', type=str, default='tracks.json', help='Output json file'
    )
    parser.add_argument(
        '--youtube', type=str, default='youtube.json', 
        help='Youtube Music credentials file. If file not exists, it will be created.'
    )
    return parser.parse_args()


def move_tracks(
        fileWithTracks: str, exporter: YoutubeImoirter, out_path: str
    ) -> None:
    data = {
        'liked_tracks': [],
        'not_found': [],
        'errors': [],
    }
    tracks = []
    file = open(fileWithTracks).readlines()
    for i in range(len(file)):
        args = file[i].split("-")
        tracks.append(Track(args[0], args[1][:-1]))
    print('Importing liked tracks to Youtube Music...')
    tracks.reverse()

    for track in tracks:
        data['liked_tracks'].append({
            'artist': track.artist,
            'name': track.name
        })

    print('Importing liked tracks to Youtube Music...')
    not_found, errors = exporter.import_liked_tracks(tracks)

    for track in not_found:
        data['not_found'].append({
            'artist': track.artist,
            'name': track.name
        })
        print(f'{track.artist} - {track.name}')
    
    for track in errors:
        data['errors'].append({
            'artist': track.artist,
            'name': track.name
        })
    
    print(f'{len(not_found)} not found tracks, {len(errors)} errors.')

    str_data = json.dumps(data)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(str_data)


def main() -> None:
    args = parse_args()
    exporter = YoutubeImoirter(args.youtube)
    move_tracks(args.file, exporter, args.output)


if __name__ == '__main__':
    main()