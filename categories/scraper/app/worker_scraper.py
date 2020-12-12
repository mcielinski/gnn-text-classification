import requests
import os
from celery import signature

from celery_base import app
from docker_logs import get_logger

logging = get_logger("worker-mongo")


@app.task(bind=True, name='get_subcategories')
def get_subcategories(
    self,
    category: str,
    parent_category: str,
    main_category: str,
    level: int
):
    max_level = os.environ['max_level']

    url = ''.join([
        'https://pl.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=',
        category,
        '&cmtype=subcat&format=json'
    ])

    r = requests.get(url)
    json_object = r.json()
    logging.info(json_object)
    sub_cats = json_object['query']['categorymembers']

    if ((max_level == 0) or (level <= max_level)) and (len(sub_cats) > 0):

        for cat in sub_cats:

            x = signature(
                'get_subcategories',
                args=[
                    cat,
                    category,
                    main_category,
                    level + 1
                ]
            )
            x.apply_async()

    else:

        x = signature(
            'save_category',
            args=[
                category,
                parent_category,
                main_category,
                level
            ]
        )
        x.apply_async()
