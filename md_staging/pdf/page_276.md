```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_276.jpeg
document_name: pdf
page_number: 276
page_id: pdf#page_276
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:39Z
fidelity: lossless
-->

# Essential PDF

```
[C#]

PdfLoadedDocument ldDoc = new PdfLoadedDocument(defDocumentPath);
const string destFilePattern = OutputPath + "split{0:00}.pdf";
ldDoc.Split(destFilePattern);
```

```
[VB.NET]

Dim ldDoc As PdfLoadedDocument = New PdfLoadedDocument(defDocumentPath)
Const String destFilePattern = OutputPath + "split{0:00}.pdf"
ldDoc.Split(destFilePattern)
```

**Note:** Splitting algorithm uses the Import Page methods. So the result would be similar to it.

Essential PDF also allows to split the pages as per the user's need. The following code example illustrates this.

```
[C#]

// To load an existing document which needs to be split.
PdfLoadedDocument ldDoc = new PdfLoadedDocument(filename);

// Create a pdf document.
PdfDocument doc1 = new PdfDocument();
PdfDocument doc2 = new PdfDocument();

// To add page 9 into pdf document1.
doc1.ImportPage(ldDoc, 9);

// To add page 10 into pdf document1.
doc1.ImportPage(ldoc, 10);

// To add page 5 into pdf document2.
doc2.ImportPage(ldoc, 5);

// To add page 6 into pdf document2.
doc2.ImportPage(ldoc, 6);

// Save pdf document1.
doc1.Save("Document1.pdf");

// Save pdf document1.
doc2.Save("Document2.pdf");
```

## Page-Level Navigation/TOC (if applicable)

- *No explicit local TOC present*

## Cross References

- None provided in the visible content

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```