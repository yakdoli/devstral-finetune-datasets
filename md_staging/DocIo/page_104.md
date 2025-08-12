```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_104.jpeg
document_name: DocIo
page_number: 104
page_id: DocIo#page_104
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:34:35Z
fidelity: lossless
-->

Essential DocIO

## Headers and Footers in Documents

### Overview
- Headers and Footers are properties of the document section that allow for custom formatting on each page.
- Each section can have a unique set of headers and footers, including different variations for the first, odd, and even pages.

### Content

#### Header and Footer Customization
Headers and Footers are characteristics (properties) of the document section. Each document section can have its own set of headers/footers. Each section can also have different headers on the first, odd, and even pages.

**Figure 35: Header added to the Document**

Headers and footers are set using the `HeadersFooters` property of the Word Document's section. The `HeadersFooters` property returns the object of the `WHeadersFooters` type.

To access a particular header/footer, you can use the following properties of the `WHeadersFooters` class:

- **FirstPageHeader**
- **FirstPageFooter**
- **OddHeader**
- **OddFooter**
- **EvenHeader**
- **EvenFooter**

#### Accessing Header and Footer Objects
The following properties return the object of the `HeaderFooter` type:

- **EvenFooter**: Gets even footer.
- **EvenHeader**: Gets even header.
- **FirstPageFooter**: Gets first page footer.
- **FirstPageHeader**: Gets first page header.
- **Footer**: Gets default footer.

#### Public Properties

| Name            | Description                |
|-----------------|----------------------------|
| **EvenFooter**  | Gets even footer.         |
| **EvenHeader**  | Gets even header.         |
| **FirstPageFooter** | Gets first page footer. |
| **FirstPageHeader** | Gets first page header. |
| **Footer**      | Gets default footer.      |

<!-- tags: [product, module, control, api, version?] keywords: [headers, footers, document section, Syncfusion Winforms, Word document, even footer, even header, first page footer, first page header, Default footer] -->
```