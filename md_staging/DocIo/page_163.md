```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_163.jpeg
document_name: DocIo
page_number: 163
page_id: DocIo#page_163
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:38:13Z
fidelity: lossless
-->

## Overview

- Describes the `MERGEREC` and `SECTION` fields in a merged document.
- Explains how to update fields present in a document using C# and VB.NET code examples.

## Content

### MERGEREC

This field displays the ordinal position of the current data record in a merged document. The number reflects any sorting or filtering applied to the data source before the merge.

#### Syntax
```
{ MERGEREC }
```

### SECTION

This field displays the number of the current section.

#### Syntax
```
{ SECTION }
```

#### Example: Updating Fields in the Document

The following example illustrates how to update the fields present in the document using both C# and VB.NET.

```csharp
[C#]
// Opening the Word document.
WordDocument document = new WordDocument("Input.doc");

// Updating the fields present in the document.
document.UpdateDocumentFields();

// Saving the document.
document.Save("Sample.doc", FormatType.Doc);
```

```vbnet
[VB.NET]
' Opening the Word document.
Dim document As WordDocument = New WordDocument("Input.doc")

' Updating the fields present in the document.
document.UpdateDocumentFields()

' Saving the document.
document.Save("Sample.doc", FormatType.Doc)
```

### 4.4.1.3 Bookmark

<!-- tags: [DocIO, field, MERGEREC, SECTION, update document, C#, VB.NET, WordDocument, Field updating, bookmark, document toolbar] -->
```