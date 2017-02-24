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
    logger.info('starting "get_stats" task for "%s"', hostname)

    while agent.run_event.is_set():
        yield From(asyncio.sleep(frequency))
        try:
            data = { "{}".format(plugin_key):{}}

            data["{}".format(plugin_key)] = {
                                                "size_data":{
                                                    "value":100,
                                                    "type":"integer"
                                                },
                                                "mysql_mem":{
                                                    "value":2.5,
                                                    "type":"float"
                                                },
                                                "mysql_performance":{
                                                    "value":50,
                                                    "type":"percent"
                                                }
                                            }
                                            
            logger.debug('connecting to data source')
            
            # [START] To be completed with plugin code
            # Here goes your logic
            '''
            Example:
            
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

            '''
            # [END] To be completed with plugin code
            
            logger.debug('{}: {}%'.format(hostname,data))
            yield From(agent.async_push(data))
        except:
            logger.exception('cannot get data source information')

    logger.info('get_stats terminated')
