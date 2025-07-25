# Baidu Wenku Downloader

A self-developed tool for downloading documents from Baidu Wenku (百度文库), based on reverse engineering Baidu Wenku's Canvas rendering mechanism.

[中文文档](README_zh.md)

## Official Website

Official website: [Gitea Repository](https://lostjay.xyz/gitea/github/baiduwenkudownloader)

GitHub mirror: [GitHub Repository](https://github.com/lostjay/baiduwenkudownloader)

For complete source code access, please contact the author at: lostjaychi@gmail.com

## Features

- Download PDF documents from Baidu Wenku
- Support for various document formats
- Asynchronous processing for better performance

## Demo Video

Watch the demo video on Bilibili: [Baidu Wenku Downloader Demo](https://www.bilibili.com/video/BV1FhMnzwEeK)

## How to Find Document ID

The document ID is a unique identifier in the Baidu Wenku URL. For example, in the URL:
```
https://wenku.baidu.com/view/1898f455874769eae009581b6bd97f192279bff4.html
```
The document ID is: `1898f455874769eae009581b6bd97f192279bff4`

You can find this ID in the URL of any Baidu Wenku document page. It's the string of characters between `/view/` and `.html` in the URL.

## Test API

A test API endpoint is available for testing PDF downloads:

```
https://lostjay.xyz/api/get_pdf?doc_id=6bb03e2669dc5022aaea00e5
```

**Important Note**: Only one PDF can be processed at a time. If the server is busy, you may receive a "Server is busy, please try again later" response.

## Prerequisites

- Python 3.11 or higher
- Node.js and npm

## Installation

1. Install Python dependencies:
```bash
pip install .
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Start the Node.js service:
```bash
npm start
```

## Project Structure

- `baiduwenkudownloader/`: Main Python package
- `CrawlerUtils/`: Utility functions for web crawling
- `test/`: Test files
  - `test_downloader.py`: Contains main test functions

## Testing

The main test function is located in `test/test_downloader.py`. To run the PDF download test:

```bash
cd test
python -m unittest test_downloader -k test_get_pdf
```

## Dependencies

### Python Dependencies
- bs4
- lxml
- curl-cffi
- tenacity

### Node.js Dependencies
- canvas
- express
- jspdf

## Disclaimer

This project is for educational and research purposes only. Users are responsible for complying with all applicable laws and regulations. The authors do not endorse or encourage any unauthorized use of this software. Please respect intellectual property rights and use this tool responsibly.

## License

ISC License

