```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_367.jpeg
document_name: pdf
page_number: 367
page_id: pdf#page_367
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:48:32Z
fidelity: lossless
-->

# Essential PDF

You can enable and disable PDF layers for customization purposes. For more information on enabling and disabling PDF layers, refer to the section [Creating and Embedding PDF Layers in the PDF document](#creating-and-embedding-pdf-layers-in-the-pdf-document).

## How To Read Conformance Level From PDF?

You can read conformance level applied to a PDF file using `PdfLoadedDocument.Conformance` property. This property will return the levels supported by `PdfConformanceLevel` enum.

Note: It will return none when the PDF file is not applied with any levels.

Following is the code snippet to read conformance level from PDF.

```csharp
PdfLoadedDocument loadedDocument = new PdfLoadedDocument(fileName);
PdfConformanceLevel appliedConformance = loadedDocument.Conformance;
```

```vb
Dim loadedDocument As New PdfLoadedDocument(fileName)
Dim appliedConformance As PdfConformanceLevel = loadedDocument.Conformance
```

## 5.3 PDF Form

This section shows some specific tasks that are supported in a PDF document creation.

### How To Create a Form Which Transfers Data To the Server?

You can create a form and transfer the data to the server by using the `PdfSubmitAction` class. The following code example illustrates how to create a document with a PDF form in it. When the Submit button is clicked, data is sent to the processing script which displays the received data. You can write your own data processing script and manipulate data as needed.

```csharp
[C#]
```

---

**© 2013 Syncfusion. All rights reserved.**  
**Page 367 |**  

<!-- tags: [product, pdf, document, conformance level, form, data transfer, submit action, Syncfusion Winforms, pdf loaded document, pdf conformance level, synchronization, api reference, code examples] -->
```