```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_278.jpeg
document_name: pdf
page_number: 278
page_id: pdf#page_278
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:42:00Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Note: This template can be scaled, rotated, placed at different coordinates, and so on.
- Covers the limitations of converting annotations and accessing document information using Essential PDF.

## Content

### Restrictions

This above process can convert annotations also but with some limitations as follows:

- It does not pay attention to the fields
- It takes the first appearance stream from the annotation's normal appearance dictionary, (if it isn't a stream)
- It places the appearance stream as a template on the page according to its states, say, on, off or some other states.
- This may lead to unexpected results.

For more details, see **Import Pages as Templates**.

### 4.2.7 Document Information

Essential PDF enables the user to access the following information of the existing document with the help of the **PdfDocumentInformation** class.

- Author
- Creator
- Keywords
- Producer
- Subject
- Title and so on

#### Accessing Document Information

The following code example illustrates how to access the document information.

```csharp
[C#]

PdfLoadedDocument doc = new PdfLoadedDocument(filename);

// Accessing document information
authorBox.Text = doc.DocumentInformation.Author;
titleBox.Text = doc.DocumentInformation.Title;
subjectBox.Text = doc.DocumentInformation.Subject;
kwBox.Text = doc.DocumentInformation.Keywords;
creatorBox.Text = doc.DocumentInformation.Creator;
prodBox.Text = doc.DocumentInformation.Producer;
```

### Cross References

See also: **PdfDocumentInformation**, **Annotations Conversion Limitations**, **Templates**

### Advanced Considerations

This section highlights the restrictions encountered when converting annotations, focusing on how unexpected results can arise due to the limitations in handling appearance streams. Additionally, it emphasizes the importance of understanding document metadata access for effective document manipulation using the Essential PDF library.

### Summary

This section details the use of **PdfDocumentInformation** to access and retrieve various metadata of a PDF document, highlighting potential limitations in converting annotations within PDFs, crucial for developers working with Syncfusion Winforms.

### RAG Annotations

<!-- tags: essential-pdf, winforms, document-information, document-metadata, annotations-conversion, pdfdocumentinformation, version-11.4.0.26 keywords: annotations, pdf, templates, document information, metadata, appearance streams, pdfloadeddocument, document states -->
```