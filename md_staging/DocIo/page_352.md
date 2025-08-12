```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_352.jpeg
document_name: DocIo
page_number: 352
page_id: DocIo#page_352
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:51:23Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Covers the integration of headers and footers in a document.
- Demonstrates how to insert page numbers to the header and text to the footer using MS Office Interop.

## Content

### 5.12.6 Header/Footer
Headers and footers are displayed at the top and bottom of the document pages, respectively. The headers and footers can be inserted with text, graphics, and nearly any other information that is contained in the document.

#### Using MS Office Interop
The following code examples illustrate how to add headers and footers to a word document. In this example, page numbers are inserted to the header, and a text is inserted to the footer.

```markdown
### WinForms-specific conventions
- The example provided uses C# code for clarity and consistency with Syncfusion Winforms.
```

### API Reference (if applicable)
- Namespace: `Microsoft.Office.Interop.Word`
- Classes:
  - `Document`
  - `Section`
  - `HeaderFooter`
  - `Range`

### Code Examples
```csharp
// Assuming the document is already created and the necessary interop references are included
using Microsoft.Office.Interop.Word;

// Open the document
Application wordApp = new Application();
Document doc = wordApp.Documents.Open(docPath);

// Access the first section
Section section = doc.Sections[1];

// Add page numbers to the header
HeaderFooter header = section.Headers[WdHeaderFooterIndex.wdHeaderFooterPrimary];
header.Range.Text = "Page " + header.Range.MailMergeDataSourceFieldEachPage;

// Add text to the footer
HeaderFooter footer = section.Footers[WdHeaderFooterIndex.wdHeaderFooterPrimary];
footer.Range.Text = "Document Footer Text";

// Save and close the document
doc.SaveAs("Output.docx");
doc.Close();
wordApp.Quit();
```

### RAG Annotations
<!-- tags: [docio, headerfooter, msinterop, winforms, syncfusionwinforms, api] keywords: [headers, footers, page numbers, text, interop, word document] -->
```