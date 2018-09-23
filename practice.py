#!/usr/bin/python
import requests
from argparse import ArgumentParser

API_KEY = 'trnsl.1.1.20180921T202554Z.2f0ebf91fae2d8e4.9ce767aec09c8fc6dbf3fcae566a21c15408f8ac'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text, from_lang, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '%s-%s' % (from_lang, to_lang),
    }
    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--lang-to', dest='langto')
    parser.add_argument('--lang-from', dest='langfrom', required=True)
    parser.add_argument('--path-to', dest='pathto', required=True)
    parser.add_argument('--path-from', dest='pathfrom', required=True)

    args = parser.parse_args()
    langto = 'ru'
    if args.langto:
        langto = args.langto
    with open(args.pathfrom, 'r') as pf:
        with open(args.pathto, 'w') as pt:
            text = pf.read()
            res = translate_it(text, args.langfrom, langto)
            pt.write(res)
