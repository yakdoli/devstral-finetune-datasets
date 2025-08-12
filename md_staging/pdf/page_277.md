```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_277.jpeg
document_name: pdf
page_number: 277
page_id: pdf#page_277
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:43Z
fidelity: lossless
-->

### [VB.NET]

```vb
' To load an existing document which needs to be split.
Dim lDoc As PdfLoadedDocument = New PdfLoadedDocument(filename)
' Create a pdf document.
Dim doc1 As PdfDocument = New PdfDocument()
Dim doc2 As PdfDocument = New PdfDocument()
' To add page 9 into pdf document1.
doc1.ImportPage(ldoc, 9)
' To add page 10 into pdf document1.
doc1.ImportPage(ldoc, 10)
' To add page 5 into pdf document2.
doc2.ImportPage(ldoc, 5)
' To add page 6 into pdf document2.
doc2.ImportPage(ldoc, 6)
' Save pdf document1.
doc1.Save("Document1.pdf")
' Save pdf document1.
doc2.Save("Document2.pdf")
```

## 4.2.6 Transform PDF

The pdf pages can be converted to PdfTemplate object if you want to create a **booklet** or just place a few pages onto a single page like an image. The template can be created using the below code.

### [C#]

```csharp
PdfTemplate template = lpage.CreateTemplate();
```

### [VB.NET]

```vb
Dim template As PdfTemplate = lpage.CreateTemplate()
```
```