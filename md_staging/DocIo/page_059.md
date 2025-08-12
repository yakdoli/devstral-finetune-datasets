```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_059.jpeg
document_name: DocIo
page_number: 059
page_id: DocIo#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:31:35Z
fidelity: lossless
-->

## 4.2 Word Document

You can open, modify, and create Microsoft Word documents by using the `WordDocument` class. `WordDocument` class models the structure of a Microsoft Word document.

### Creating a Word Document

To create a new document, use the `EnsureMinimal` method. This method creates a document with an empty section, and adds empty paragraphs to the newly created section.

### Opening a Word Document

DocIO also gives you an opportunity to open existing documents, or read data from streams saved in the following `FormatType` variants.

- Doc: Microsoft Word File Format
- Txt: Text File Format
- Docx: Word 2007 File Format
- Dot: Word Template Format
- HTML: HTML Format
- RTF: Rich Text Format
- Docm: Word Macro-enabled Document Format
- Dotm: Word Macro-enabled Template Format
- Dotx: Word Open xml Template Format

To open a document, use the `Open` method. There are several overloads for this method.

- `Open(string fileName)`: opens Word document.
- `Open(string fileName, FormatType formatType)`: opens the document with specified format type (.doc, .xml or .txt file).
- `Open(string fileName, FormatType formatType, string password)`: opens the encrypted document with a specified format type and password.
- `Open(string fileName, FormatType formatType, XHTMLValidationType validationType)`: opens the document with a specified format type and XHTMLValidationType. Ignores validation type if the input document is not XHTML.
- `Open(string fileName, FormatType formatType, XHTMLValidationType validationType, string baseUrl)`: opens the document with specified format type, XHTMLValidationType and the baseUrl of the input document. Ignores validation type and baseUrl if the input document is not HTML.

```html
<!-- tags: [syncfusion-sdk, winforms, word document, worddocument class, word document management] keywords: [docio, microsoft word, file formats, document creation, document opening, document management, text file, HTML, RTF, Word template, macro-enabled document, encrypted document, XHTMLValidationType, base URL] -->
``` 
```