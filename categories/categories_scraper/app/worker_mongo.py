import os
import pymongo

from celery_base import app
from docker_logs import get_logger

logging = get_logger("worker-mongo")

mongo_uri = ''.join([
    'mongodb://',
    os.environ['MONGO_INITDB_ROOT_USERNAME'],
    ':',
    os.environ['MONGO_INITDB_ROOT_PASSWORD'],
    '@mongodb:27017'
])


@app.task(bind=True, name='save_category')
def save_category(
    self,
    category: str,
    parent_category: str,
    main_category: str,
    level: int
):

    myclient = pymongo.MongoClient(mongo_uri)
    mydb = myclient["wiki"]
    mycol = mydb["categories"]

    category = {
        'category_name': category,
        'parent_category': parent_category,
        'main_category': main_category,
        'level': level
    }

    try:
        _ = mycol.insert_one(category)
    except pymongo.errors.WriteError as e:
        logging.info('Cannot send item to MongoDB')
        logging.info(e)
    finally:
        # logging.info('Item send to MongoDB - ', str(category))
        logging.info('Item send to MongoDB')

    myclient.close()