const path = require("path");
const fs = require('fs').promises;
const id = '6bb03e2669dc5022aaea00e5'
const readerInfoFilePath = path.join(__dirname, `../test/reader_info_${id}.json`);
const docInfoFilePath = path.join(readerInfoFilePath, `../doc_info_${id}.json`);
const {generate_pdf} = require('../baiduwenkudownloader/jspdfextractor.js')

console.log(docInfoFilePath)

async function saveDataUriToFile(dataUri, outputPath) {
    const matches = dataUri.match(/^data:(.*?);base64,(.*)$/);
    if (!matches) {
        throw new Error('Invalid data URI');
    }
    const base64Data = matches[2];
    const fileBuffer = Buffer.from(base64Data, 'base64');
    await fs.writeFile(outputPath, fileBuffer);
}

async function test() {
    try {
        const [readerData, docData] = await Promise.all([
            fs.readFile(readerInfoFilePath, 'utf8'),
            fs.readFile(docInfoFilePath, 'utf8')
        ]);
        const readerInfo = JSON.parse(readerData);
        const docInfo = JSON.parse(docData);
        console.log('Reader Info:', readerInfo);
        console.log('Document Info:', docInfo);
        const input = {
            readerInfo: readerInfo,
            docInfo: docInfo,
            title: 'test',
            format: 'pdf'
        }
        const dataUri = await generate_pdf(input);
        await saveDataUriToFile(dataUri, `./${id}.pdf`);
    } catch (err) {
        console.error('Error reading or parsing JSON files:', err);
        throw err;
    }
}

test();