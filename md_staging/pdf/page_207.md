```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_207.jpeg
document_name: pdf
page_number: 207
page_id: pdf#page_207
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:37:58Z
fidelity: lossless
-->

## How to add a Custom Metadata Field

To add a custom metadata field,

- Add namespace in the project
- Create an XML document container
- Create a custom schema

### Adding Namespace in the Project

The user needs to add the namespace Syncfusion.Pdf.Xmp in the project to enable addition of custom metadata fields in the PDF document.

Add the namespace using the following code.

```csharp
using Syncfusion.Pdf.Xmp;
```

### Creating an XML Document Container

The custom metadata to be created has to be stored and linked to the PDF document in use. Here an XML document is used as a container to save the custom metadata fields for the PDF document.

Add the following code to create an XML document to store custom metadata fields.

```csharp
XmpMetadata xmp = new XmpMetadata(pdfDoc.DocumentInformation.XmpMetadata.XmlData);
```

The following table provides more information on the code.

| Property    | Type      | Value It Accepts |
|-------------|-----------|------------------|
| XmlData     | XmlElement| XmlElement      |

### Creating a Custom Schema

### Conclusion
This section explains how to add custom metadata fields in a PDF document by incorporating the necessary namespaces, creating an XML document container, and defining a custom schema. The provided code snippets and table illustrate the steps involved in achieving this functionality within a Syncfusion Winforms application.

## Cross References
- Refer to the Syncfusion Winforms documentation for more information on PDF manipulation and metadata handling.
- See the API Reference for detailed information about the Syncfusion.Pdf.Xmp namespace and its methods.

<!-- tags: [Syncfusion Winforms, PDF, Metadata, Custom Field, Namespace, XML Document, Xmp, C#] keywords: [custom metadata, XML container, PDF document, Syncfusion.Pdf.Xmp, XmpMetadata, XmlData] -->
```