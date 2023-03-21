from yandexfreetranslate import YandexFreeTranslate
import multiprocessing as mp
import json

def _worker(queue: str) -> str:
    if not queue:
        return ''
    yt = YandexFreeTranslate(api = "ios")
    text = yt.translate("en", "ru", queue)
    return text


def run_translate(lst: list[str])-> list[str]:
    with mp.Pool(mp.cpu_count()) as process:
        workreturn = process.map(_worker, lst)
    return workreturn


if __name__ == '__main__':
    with open(
        file='crap.ipynb'
    ) as file:
        text = json.loads(file.read())
        name = text['cells'][1]['outputs'][0]['text'][0].strip()
    
    with open(
        file=f'{name}.txt'
    ) as file:
        text = file.read()
    
    text_rus = run_translate(text.split('\n'))
    
    text_rus = '\n'.join(text_rus)
    
    with open(
        file=f'{name}_rus.txt',
        mode='w',
        encoding='utf-8'
    ) as file:
        file.write(text_rus)




