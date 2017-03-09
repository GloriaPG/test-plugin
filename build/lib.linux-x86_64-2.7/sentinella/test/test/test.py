import os
import json
import logging

import trollius as asyncio
from trollius import From

logger = logging.getLogger(__name__)

frequency = 60
hostname = os.uname()[1].split('.')[0]

@asyncio.coroutine
def get_stats(agent):
    yield From(agent.run_event.wait())
    config = agent.config['test']
    plugin_key = config['plugin_key']
    logger.info('plugin_key {}'.format(plugin_key))
    logger.info('starting "get_stats" task for "%s"', hostname)

    while agent.run_event.is_set():
        yield From(asyncio.sleep(frequency))
        try:
            data = {'server_name': hostname,
                    'plugins': {}}
            logger.debug('connecting to data source')
            
            # [START] To be completed with plugin code
            # Here goes your logic
        
            
            instance = ''
            value = ''
            data['plugins'].update({"{}".format(plugin_key):{}})
            data['plugins'][plugin_key].update({"size_data":{"value":100,"type":"integer"}})
            data['plugins'][plugin_key].update({"mem":{"value":3.5,"type":"float"}})
            data['plugins'][plugin_key].update({"data":{"value":30,"type":"integer"}})
                                               

            logger.debug('{}: myplugin={}%'.format(hostname, data))
            yield From(agent.async_push(data))
        except:
            logger.exception('cannot get data source information')

    logger.info('get_stats terminated')
