from multiprocessing import Pool
from tqdm import tqdm

tasks = range(5)
pool = Pool()
pbar = tqdm(total=len(tasks))

def do_work(x):
    
    pbar.update(1)
    return x*x

pool.map(do_work, tasks)
pool.close()
pool.join()
pbar.close()