```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_282.jpeg
document_name: pdf
page_number: 282
page_id: pdf#page_282
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:42:14Z
fidelity: lossless
--> 

# 4.2.9 OCR Support

The Tesseract optical character recognition (OCR) engine was originally developed by Hewlett-Packard. It was one of the top three engines in the 1995 UNLV accuracy test and is probably one of the most accurate open-source OCR engines available. It has been extensively revised with sponsorship from Google. Essential PDF uses the Tesseract OCR engine to perform OCR on a PDF file. Essential PDF eliminates the 32-bit restriction of Tesseract and allows you to work in either x86-bit or x64-bit platforms without any deployment changes.

## Use Case Scenarios

- This will convert an unsearchable PDF document to a searchable PDF document.
- It allows users to search, select, and copy text from images found in the PDF document.

### 4.2.9.1 Tables for Properties and Methods

#### Properties

Table: Properties Table

| Property     | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| Settings     | Gets or sets the settings for performing OCR.                             |
| Paginate     | Gets or sets image pagination in the PDF document.                       |
| Regions      | Gets or sets page regions for performing OCR.                             |
| Language     | Gets or sets the OCR language to process.                                 |
| PageIndex    | Gets or sets page index to process OCR.                                   |
| PageRegions  | Gets or sets a rectangular array for the page to process the OCR in specific regions. |
| Performance  | Gets or sets the performance of the OCR.                                  |
| BlackList    | Gets or sets the black-list values.                                       |

<!-- tags: [product, module, control, api, version?] keywords: [OCR, Tesseract, Essential PDF, OCR Support, Properties, Methods, x86-bit, x64-bit, searchable PDF, text extraction, image pagination, page regions, OCR language, page index, rectangular array, performance, black-list, setting] -->
```