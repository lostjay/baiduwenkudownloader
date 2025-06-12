# Baidu Wenku Downloader

A self-developed tool for downloading documents from Baidu Wenku (百度文库), based on reverse engineering Baidu Wenku's Canvas rendering mechanism.

[中文文档](README_zh.md)

## Official Website

Official website: https://lostjay.xyz/gitea/github/baiduwenkudownloader

For complete source code access, please contact the author at: lostjaychi@gmail.com

## Features

- Download PDF documents from Baidu Wenku
- Support for various document formats
- Asynchronous processing for better performance

## How to Find Document ID

The document ID is a unique identifier in the Baidu Wenku URL. For example, in the URL:
```
https://wenku.baidu.com/view/1898f455874769eae009581b6bd97f192279bff4.html
```
The document ID is: `1898f455874769eae009581b6bd97f192279bff4`

You can find this ID in the URL of any Baidu Wenku document page. It's the string of characters between `/view/` and `.html` in the URL.

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

## Buy Me a Milk Tea

If you find this project helpful, feel free to buy the author a milk tea via WeChat Pay!

![WeChat Pay QR Code](https://lostjay.xyz/wechatpay)
