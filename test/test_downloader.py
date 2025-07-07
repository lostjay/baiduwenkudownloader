from unittest import IsolatedAsyncioTestCase
from base64 import b64decode
from contextlib import suppress

from baiduwenkudownloader.downloader import BaiduWenkuDownloader

from CrawlerUtils import init_logger, FileManager
from CrawlerUtils.RequestManager import post

logger = init_logger()


class TestBaiduWenkuDownloader(IsolatedAsyncioTestCase):
    def setUp(self):
        self.ids = [
            '6bb03e2669dc5022aaea00e5', 
            '1898f455874769eae009581b6bd97f192279bff4',  # FIXME Missing necessary fonts.
            '3ab5710b7a563c1ec5da50e2524de518964bd341', 
            '1c37025a75eeaeaad1f34693daef5ef7bb0d1205', 
            '653a5c04ee630b1c59eef8c75fbfc77da26997aa',
            '50dc55b5a98271fe900ef9b1',
            '93e5d5febd1e650e52ea551810a6f524cdbfcbf7',
            '39f6a743cbd376eeaeaad1f34693daef5ff713d0',
            '750afec94731b90d6c85ec3a87c24028915f85b8',
            'dc7aeae4551810a6f5248686'
        ]

    def get_downloader(self):
        for id_ in self.ids:
            downloader = BaiduWenkuDownloader(id_)
            if (f := FileManager(f'doc_info_{downloader.id}.json')).exists():
                downloader._doc_data = f.read_json()
            if (f := FileManager(f'reader_info_{downloader.id}.json')).exists():
                downloader._reader_info = f.read_json()
            yield downloader

    async def test_get_html(self):
        for downloader in self.get_downloader():
            html: str = await downloader.html
            logger.debug(f'Got html: {html}', trace_id=downloader.trace_id)
            self.assertTrue(html.strip())

    async def test_get_reader_info(self):
        for downloader in self.get_downloader():
            with suppress(AttributeError):
                delattr(downloader, '_reader_info')
            reader_info: dict = await downloader.reader_info
            logger.debug(f'Got reader_info: {reader_info}', trace_id=downloader.trace_id)
            logger.debug(f'Got docdata: {await downloader.doc_data}', trace_id=downloader.trace_id)
            FileManager(f'reader_info_{downloader.id}.json').write_json(reader_info)
            FileManager(f'doc_info_{downloader.id}.json').write_json(await downloader.doc_data)
            self.assertTrue(reader_info.get('htmlUrls', {}).get('json'))

    async def test_api(self):
        for downloader in self.get_downloader():
            input_ = {
                'readerInfo': await downloader.reader_info,
                'docInfo': await downloader.doc_data,
                'title': 'test',
                'format': 'pdf'
            }
            res = await post('http://127.0.0.1:17020/generate_pdf', json=input_)
            content = b64decode(res.split(',', 1)[1])
            FileManager(f'{downloader.id}_api.pdf').write_byte(content)

    async def test_download_api_json(self):
        for downloader in self.get_downloader():
            await downloader.download_api_json((await downloader.reader_info)['htmlUrls']['json'][0])

    async def test_get_pdf(self):
        for downloader in self.get_downloader():
            try:   
                content = await downloader.pdf_content
                FileManager(f'{downloader.id}.pdf').write_byte(content)
            except Exception as e:
                logger.warn(f'Failed to downlod the file, {e}.', exc_info=e)
                
    def test_for_public(self):
        from fastapi import FastAPI, Response
        from time import strftime
        from uvicorn import run
        from asyncio import Event
        from baiduwenkudownloader.downloader import BaiduWenkuDownloader
        
        BaiduWenkuDownloader.node_server = 'http://10.13.13.2:17020'
        handling = Event()
        app = FastAPI()
        
        @app.get('/')
        async def hello():
            return {"code": 2, "message": "Welcome to use the baiduwenku downloader test api.", "time": strftime('%Y-%m-%d %H:%M:%S'), 'path': './get_pdf'}
        
        @app.get('/get_pdf')
        async def get_pdf(doc_id: str):
            if handling.is_set():
                return {"code": 5, "message": "Server is busy, please try again later.", "time": strftime('%Y-%m-%d %H:%M:%S')}
            handling.set()
            try:
                content = await BaiduWenkuDownloader(doc_id).pdf_content
                return Response(content=content, media_type='application/pdf')
            except Exception as e:
                return {"code": 4, "message": str(e), "time": strftime('%Y-%m-%d %H:%M:%S')}
            finally:
                handling.clear()
            
        run(app, host='0.0.0.0', port=17071)

    # @run_async
    # async def test_update_api_ttf(self):
    #     for downloader in self.get_downloader():
    #         await downloader.update_api_ttf((a := (await downloader.reader_info)['htmlUrls'])['ttf'], a['ttf_offset'])
