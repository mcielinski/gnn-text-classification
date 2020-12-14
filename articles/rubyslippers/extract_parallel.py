import csv
import sys
import rapidjson as json

import pandas as pd
from joblib import Parallel, delayed
from tqdm import tqdm

from rubyslippers import extract_pages_from_dump
from rubyslippers import WikiExtractor


# Categories DataFrame
cats_file_path = '../categories/categories.csv'
cats_df = pd.read_csv(cats_file_path)
cats_df.drop_duplicates(inplace=True)
# List of categories we are interested in
cats_to_save = cats_df.category_name.unique().tolist()


def parallelize_preprocess(func, iterator, processes, progress_bar=False):
    iterator = tqdm(iterator) if progress_bar else iterator
    if processes <= 1:
        return map(func, iterator)
    return Parallel(n_jobs=processes)(delayed(func)(line) for line in iterator)


def get_main_cat_level(page_category):
    row = cats_df[cats_df['category_name'] == page_category].sort_values(by=['level']).iloc[0]

    return row['main_category'], row['level']


def wiki_page_processing(wiki_page):
    wiki_page_cats = wiki_page['categories']

    if len(wiki_page_cats) < 1:
        return None
    
    main_cat = None
    level = 1000
    for wiki_page_cat in wiki_page_cats:
        if wiki_page_cat in cats_to_save:
            wpc_main_cat, wpc_level = get_main_cat_level(page_category=wiki_page_cat)
            if wpc_level < level:
                main_cat = wpc_main_cat
                level = wpc_level
    
    if main_cat is None:
        return None
    else:
        wiki_page['main_category'] = main_cat

    return wiki_page


def get_annotation_info(wiki_page):
    source_page = wiki_page['url'].split('/')[-1]
    annotations = []
    for annotation in wiki_page['annotations']:
        annotations.append(annotation['uri'])
    
    return source_page, annotations


processes = 4
quiet = True
we = WikiExtractor('pl')

output_dir = sys.argv[1]
annotations_file_path = 'rubyslippers/out/annotations.csv'

pages = []
for idx, page in tqdm(enumerate(extract_pages_from_dump(sys.stdin))):
    pages.append(page)
    if len(pages) % processes == 0:
        for wiki_page in parallelize_preprocess(
            we.extract, pages, processes, progress_bar=(not quiet)
        ):
            if wiki_page:
                # Returns None if none of the page categories are in the list cats_to_save
                # otherwise, returns the wiki_page dict extended by the corresponding main category
                wiki_page = wiki_page_processing(wiki_page)
                
                if wiki_page is not None:
                    with open(output_dir + str(wiki_page['id']) +'.json', 'w') as fout:
                        json.dump(wiki_page, fout)

                    # Save annotation pairs do csv (row: <source_pade, annotation>)
                    source_page, annotations = get_annotation_info(wiki_page)

                    with open(annotations_file_path, 'a') as f:
                        writer = csv.writer(f, delimiter=',', lineterminator='\n',)
                        for annotation in annotations:
                            row = [source_page, annotation]
                            writer.writerow(row)
        pages = []

if len(pages) > 0:
    for wiki_page in parallelize_preprocess(
        we.extract, pages, processes, progress_bar=(not quiet)
    ):
        if wiki_page:
            # Returns None if none of the page categories are in the list cats_to_save
                # otherwise, returns the wiki_page dict extended by the corresponding main category
                wiki_page = wiki_page_processing(wiki_page)
                
                if wiki_page is not None:
                    with open(output_dir + str(wiki_page['id']) +'.json', 'w') as fout:
                        json.dump(wiki_page, fout)

                    # Save annotation pairs do csv (row: <source_pade, annotation>)
                    source_page, annotations = get_annotation_info(wiki_page)

                    with open(annotations_file_path, 'a') as f:
                        writer = csv.writer(f, delimiter=',', lineterminator='\n',)
                        for annotation in annotations:
                            row = [source_page, annotation]
                            writer.writerow(row)
