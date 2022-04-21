import requests


def save_file(url: str, filename: str):
    """Save webpage from url to file in current folder
    url - set in quotes
    filename - set in quotes with file extension"""
    res = requests.get(url)
    if res.status_code == requests.codes.ok:
        with open(filename, 'w', encoding='utf-8') as ouf:
            ouf.write(res.text)
        print('save ok')
    else:
        print(f'response error, status code: {res.status_code}')
