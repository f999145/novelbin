from yandexfreetranslate import YandexFreeTranslate
from multiprocessing.dummy import Pool as ThreadPool
import json
from tqdm import tqdm

# def _worker(queue: str) -> str:
#     if not queue:
#         return ''
#     yt = YandexFreeTranslate(api = "ios")
#     text = yt.translate("en", "ru", queue)
#     return text


# def run_translate(lst: list[str])-> list[str]:
#     with mp.Pool(mp.cpu_count()) as process:
#         workreturn = process.map(_worker, lst)
#     return workreturn



def _worker(que: tuple) -> str:
    queue, pbar = que
    if not queue:
        pbar.update(1)
        return ''
    yt = YandexFreeTranslate(api = "ios")
    text = yt.translate("en", "ru", queue)
    pbar.update(1)
    return text

def run_translate(lst: list[str])-> list[str]:
    with tqdm(total=len(lst) ) as pbar:
        l_b = list(zip(lst, ( pbar for _ in range(len(lst)))))
        with ThreadPool(30) as pool:
            workreturn = pool.map(_worker, l_b)
    return workreturn


if __name__ == '__main__':
    with open(
        file='crap.ipynb'
    ) as file:
        text = json.loads(file.read())
        name = text['cells'][2]['outputs'][0]['text'][0].strip()
    
    with open(
        file=f'{name}.txt'
    ) as file:
        text = file.read()
    
    lst = text.split('\n')
    
    text_rus = run_translate(lst)
    
    text_rus = '\n'.join(text_rus)
    
    with open(
        file=f'{name}_rus.txt',
        mode='w',
        encoding='utf-8'
    ) as file:
        file.write(text_rus)




