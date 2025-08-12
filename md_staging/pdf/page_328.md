```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_328.jpeg
document_name: pdf
page_number: 328
page_id: pdf#page_328
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:51Z
fidelity: lossless
-->

# Essential PDF

## Limitations

Image extraction does not work with the following constraints:

- If the image has multiple filters in the PDF document.
- You cannot extract the image which is placed on the Xobject, also known as PdfTemplate.

## 4.4.4 Doc To PDF

Essential DocIO enables to export the Word document into a PDF document. By using the ConvertToPDF method of the DocToPDFConverter class, you can convert the Word document to PDF, and save the PDF document.

### Note: You need to have Essential PDF and Essential DocIO installed in your system. This is because "Syncfusion.DocToPDFConverter.Base.dll" is conditionally shipped when both DocIO.Base and Pdf.Base is installed.

This section covers the following:

- Assemblies Dependent for this Conversion
- Supported Elements and Limitations
- UnSupported Elements and Limitation

### Assembly Dependency for this Conversion

- Syncfusion.DocToPDFConverter.Base.dll
- Syncfusion.DocIO.Base.dll
- Syncfusion.Pdf.Base.dll
- Syncfusion.Core.dll
- Syncfusion.Compression.Base.dll

### Converting a Word Document to PDF

The following code illustrates how to convert a word document, say, "sample.doc" to a PDF document.

```csharp
[C#]

WordDocument wordDoc = new WordDocument("sample.doc");
DocToPDFConverter converter = new DocToPDFConverter();
```

### Page-level Navigation/TOC (if applicable)

- **Limitations**
- **4.4.4 Doc To PDF**
  - Note
  - Assemblies Dependent for this Conversion
  - Supported Elements and Limitations
  - UnSupported Elements and Limitation
  - Assembly Dependency for this Conversion
  - Converting a Word Document to PDF

<!-- tags: [Essential PDF, Essential DocIO, Word to PDF, DocToPDFConverter, Assembly Dependency, Unsupported Elements, Converting Word Document, Syncfusion Winforms, version 11.4.0.26] keywords: [ConvertToPDF, DocToPDFConverter, PDF document, Word document, image extraction, Xobject, filters, Ytandar, note, assembly dependency, limitations, supported elements, unsupported elements, C# code, Syncfusion, version 11.4.0.26] -->
```