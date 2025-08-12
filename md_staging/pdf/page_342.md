```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_342.jpeg
document_name: pdf
page_number: 342
page_id: pdf#page_342
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:46:05Z
fidelity: lossless
-->

# Essential PDF

## 5 Frequently Asked Questions

This section illustrates the solutions for various task-based queries about Essential PDF.

### 5.1 PDF Generator

This section shows some specific tasks that are supported in a PDF Generator.

#### 5.1.1 Common

This section shows some common tasks in a PDF Generator.

##### 5.1.1.1 How To Add Sections And Pages?

Essential PDF enables to add any number of sections and pages. A PDF document should contain atleast one section. Each section can have any number of pages in it. PdfSection class is used to create sections and PdfPage class is used to add pages.

```csharp
[C#]
PdfDocument document = new PdfDocument();
//Adds a section to the document
PdfSection section = doc.Sections.Add();
//Adds a page to the section
PdfPage = section.Pages.Add();
```

```vb
[VB.NET]
Dim document As PdfDocument = New PdfDocument()
'Adds a section to the document
Dim section As PdfSection = doc.Sections.Add()
'Adds a page to the section
Dim page As PdfPage = section.Pages.Add()
```
```