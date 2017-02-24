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
    logger.info('starting "get_stats" task for "%s"', hostname)

    while agent.run_event.is_set():
        yield From(asyncio.sleep(frequency))
        try:
            data = {'server_name': hostname,
                    'measurements': []}
            logger.debug('connecting to data source')
            
            # [START] To be completed with plugin code
            # Here goes your logic
        
            
            instance = ''
            value = ''
            data['measurements'].append({'name': 'myplugin.cpu',
                                         'tags': {'instance': instance},
                                         'value': value})
                                         
            data['measurements'].append({'name': 'myplugin.mem',
                                         'tags': {'instance': instance},
                                         'value': value})
                                         
            data['measurements'].append({'name': 'myplugin.iops',
                                         'tags': {'instance': instance},
                                         'value': value})


            logger.debug('{}: myplugin={}%'.format(hostname, data))
            yield From(agent.async_push(data))
        except:
            logger.exception('cannot get data source information')

    logger.info('get_stats terminated')