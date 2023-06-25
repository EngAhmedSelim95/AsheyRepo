# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import asyncio
from requests_html import AsyncHTMLSession
from scrapy import signals
from scrapy.http import HtmlResponse
import logging
class RequestsMiddleware:
    logging.getLogger("websockets").setLevel(20)
    logging.getLogger("pyppeteer").setLevel(20)
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = AsyncHTMLSession()

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        api_key = settings.get('SCRAPINGBEE_API_KEY')
        return cls(api_key)

    async def process_request(self, request, spider):
        if request.meta.get('render'):
            params = {'api_key': self.api_key, 'url': request.url,'render_js': 'false'}
            api_response = await self.session.get('https://app.scrapingbee.com/api/v1/', params=params)
            html = api_response.html
            return HtmlResponse(url=request.url, body=html.html, encoding='utf-8', request=request)

        if not request.meta.get('render'):
            params = {'api_key': self.api_key, 'url': request.url,'render_js': 'false'}
            api_response = await self.session.get('https://app.scrapingbee.com/api/v1/', params=params)
            html = api_response.html
            return HtmlResponse(url=request.url, body=html.html, encoding='utf-8', request=request)

        response = await self.session.get(request.url)
        await response.html.arender()
        return HtmlResponse(url=request.url, body=response.content, encoding='utf-8', request=request)

    def process_exception(self, request, exception, spider):
        if isinstance(exception, asyncio.TimeoutError):
            return request.replace(meta={'render': True}, priority=request.priority-1)

    async def close(self, spider):
        await self.session.close()
class AshleyDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
