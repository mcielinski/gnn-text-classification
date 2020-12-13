
import sys
import rapidjson as json

from joblib import Parallel, delayed
from tqdm import tqdm

from rubyslippers import extract_pages_from_dump
from rubyslippers import WikiExtractor

def parallelize_preprocess(func, iterator, processes, progress_bar=False):
    iterator = tqdm(iterator) if progress_bar else iterator
    if processes <= 1:
        return map(func, iterator)
    return Parallel(n_jobs=processes)(delayed(func)(line) for line in iterator)

processes = 4
quiet = True
we = WikiExtractor('pl')

output_dir = sys.argv[1]

pages = []
for idx, page in tqdm(enumerate(extract_pages_from_dump(sys.stdin))):
    pages.append(page)
    if len(pages) % processes == 0:
        for wiki_page in parallelize_preprocess(
            we.extract, pages, processes, progress_bar=(not quiet)
        ):
            if wiki_page:

                # znalezc main category
                # dopisac annotations do csv 
                # zapisac jezeli jest main category
                with open(output_dir + str(wiki_page['id']) +'.json', 'w') as fout:
                    json.dump(wiki_page, fout)
        pages = []

if len(pages) > 0:
    for wiki_page in parallelize_preprocess(
        we.extract, pages, processes, progress_bar=(not quiet)
    ):
        if wiki_page:
            with open(output_dir + str(wiki_page['id']) +'.json', 'w') as fout:
                json.dump(wiki_page, fout)
