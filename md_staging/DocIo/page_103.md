```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_103.jpeg
document_name: DocIo
page_number: 103
page_id: DocIo#page_103
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:34:23Z
fidelity: lossless
-->

# Essential DocIO

## Content

### Importing Content with Formatting

- C#

```csharp
// Open the destination word document.
WordDocument destination = new WordDocument("Destination.doc");
// Open the source word document.
WordDocument source = new WordDocument("Source.doc");

// Imports the contents with import option keep source formatting.
destination.ImportContent(source, ImportOptions.KeepSourceFormatting);

// Save the document.
destination.Save("Sample.doc", FormatType.Doc);
```

- VB.NET

```vb
' Open the destination word document.
Dim destination As New WordDocument("Destination.doc")
' Open the source word document.
Dim source As New WordDocument("Source.doc")

' Imports the contents with import option keep source formatting.
destination.ImportContent(source, ImportOptions.KeepSourceFormatting)

' Save the document.
destination.Save("Sample.doc", FormatType.Doc)
```

### 4.3.2 Headers and Footers

#### Overview
- Headers and Footers are displayed at the top and bottom of the document pages respectively.
- Headers and Footers can include text, graphics, and nearly any other information that can be contained by a document.

## Page-level Navigation/TOC (if applicable)

<!-- tags: [DocIO, headers, footers, formatting, import, document] keywords: [headers, footers, formatting, import, document, word document, source, destination, formatting options, KeepSourceFormatting, C#, VB.NET] -->
```