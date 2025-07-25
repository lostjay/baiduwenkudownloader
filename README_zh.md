# 百度文库下载器

一个基于百度文库 Canvas 渲染机制逆向工程的自研文档下载工具。

## 官方网站

官方网站：[Gitea 仓库](https://lostjay.xyz/gitea/github/baiduwenkudownloader)

GitHub 镜像：[GitHub 仓库](https://github.com/lostjay/baiduwenkudownloader)

如需获取完整源代码，请联系作者：lostjaychi@gmail.com

## 功能特点

- 支持下载百度文库 PDF 文档
- 支持多种文档格式
- 异步处理提升性能

## 演示视频

观看 B 站演示视频：[百度文库下载器演示](https://www.bilibili.com/video/BV1FhMnzwEeK)

## 如何查找文档 ID

文档 ID 是百度文库 URL 中的唯一标识符。例如，在 URL：
```
https://wenku.baidu.com/view/1898f455874769eae009581b6bd97f192279bff4.html
```
文档 ID 为：`1898f455874769eae009581b6bd97f192279bff4`

您可以在任何百度文库文档页面的 URL 中找到此 ID。它是 URL 中 `/view/` 和 `.html` 之间的字符串。

## 测试 API

提供测试 API 端点用于测试 PDF 下载：

```
https://lostjay.xyz/api/get_pdf?doc_id=6bb03e2669dc5022aaea00e5
```

**重要提示**：同一时间只能处理一个 PDF。如果服务器繁忙，您可能会收到"Server is busy, please try again later"的响应。

## 环境要求

- Python 3.11 或更高版本
- Node.js 和 npm

## 安装步骤

1. 安装 Python 依赖：
```bash
pip install .
```

2. 安装 Node.js 依赖：
```bash
npm install
```

3. 启动 Node.js 服务：
```bash
npm start
```

## 项目结构

- `baiduwenkudownloader/`: 主 Python 包
- `CrawlerUtils/`: 网络爬虫工具函数
- `test/`: 测试文件
  - `test_downloader.py`: 包含主要测试函数

## 测试

主要测试函数位于 `test/test_downloader.py`。要运行 PDF 下载测试：

```bash
cd test
python -m unittest test_downloader -k test_get_pdf
```

## 依赖项

### Python 依赖
- bs4
- lxml
- curl-cffi
- tenacity

### Node.js 依赖
- canvas
- express
- jspdf

## 免责声明

本项目仅供教育和研究目的使用。用户需遵守所有适用的法律法规。作者不认可或鼓励任何未经授权使用本软件的行为。请尊重知识产权并负责任地使用本工具。

## 许可证

ISC License
