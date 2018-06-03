# _*_ coding: utf-8 _*_
from scrapy.cmdline import execute
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl" , "spidertieba"])
# 2018-06-03 10:49:35 [scrapy.core.engine] INFO: Closing spider (finished)
# 2018-06-03 10:49:35 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
# {'downloader/request_bytes': 2144971,
#  'downloader/request_count': 4629,
#  'downloader/request_method_count/GET': 4629,
#  'downloader/response_bytes': 156341348,
#  'downloader/response_count': 4629,
#  'downloader/response_status_count/200': 4627,
#  'downloader/response_status_count/301': 2,
#  'finish_reason': 'finished',
#  'finish_time': datetime.datetime(2018, 6, 3, 2, 49, 35, 153108),
#  'item_scraped_count': 4528,
#  'log_count/DEBUG': 9162,
#  'log_count/INFO': 31,
#  'request_depth_max': 1,
#  'response_received_count': 4627,
#  'scheduler/dequeued': 4629,
#  'scheduler/dequeued/memory': 4629,
#  'scheduler/enqueued': 4629,
#  'scheduler/enqueued/memory': 4629,
#  'start_time': datetime.datetime(2018, 6, 3, 2, 25, 5, 89298)}
# 2018-06-03 10:49:35 [scrapy.core.engine] INFO: Spider closed (finished)