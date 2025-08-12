```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_246.jpeg
document_name: pdf
page_number: 246
page_id: pdf#page_246
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:04Z
fidelity: lossless
-->

## Essential PDF

### Overview
- This section focuses on PDF document management using Syncfusion's Essential PDF. It includes details on signing documents, extracting signature information, and configuring page settings.

## Content

### Document Signed with Timestamp
![Document Signed with Timestamp](https://example.com/syncfusion-doc-images/signed_document.png)

#### Figure 54: Document Signed with Timestamp
The figure displays a document, signed with a timestamp by Syncfusion. It highlights the signature's validity, timestamp, and other details, including employee number, platform (.NET), and the language German being selected.

### 4.1.7.7 Page Settings
This section outlines the page settings options available in Essential PDF for customizing the display of documents.

#### Overview
- Essential PDF supports various page settings options that control the display attributes of the generated document pages.

#### Supported Page Settings
- **Page orientation**
- **Page size**
- **Page layout**
- **Page mode**
- **Page scale**
- **Page transition**

#### Supported Page Sizes
- A0 to A9
- B0 to B5
- ArchA to ArchE

#### Example Usage
To configure page settings, you can use the `PDFDocument` class and set properties such as `PageOrientation`, `PageSize`, etc.

```csharp
PDFDocument doc = new PDFDocument();
doc.PageOrientation = PDFPageOrientation.Portrait;
doc.PageSize = PDFSize.A4;
```

### Cross References
- **Related Topics:** For more information on page properties and configuration, refer to sections 4.1.7.

---

<!-- tags: [pdf, page settings, document signing, timestamp, essential pdf, syncfusion winforms] keywords: [page orientation, page size, page layout, page mode, page scale, page transition, document management] -->
```