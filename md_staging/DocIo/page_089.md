```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_089.jpeg
document_name: DocIo
page_number: 089
page_id: DocIo#page_089
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:34:05Z
fidelity: lossless
-->

## Essential DocIO

### Use Case Scenario

This feature allows you to preserve macros present in the input macro-enabled document during conversion to another macro-enabled document (*.docm to *.docm, *.dotm to *.dotm, *.docm to *.dotm, and vice versa).

The following code illustrates how to open and save a Word macro-enabled document.

```csharp
[C#]
WordDocument doc = new WordDocument();
// Opens the Word macro-enabled document.
doc.Open("SourceDocument.docm", FormatType.Automatic);
// Saves as the Word macro-enabled document.
doc.Save("OutDocument.docm", FormatType.Word2007Docm);
```

```vb.net
[VB.NET]
Dim doc As New WordDocument()
' Opens the Word macro-enabled document.
doc.Open("SourceDocument.docm", FormatType.Automatic)
' Saves as the Word macro-enabled document.
doc.Save("OutDocument.docm", FormatType.Word2007Docm)
```

The following code illustrates how to open a Word macro-enabled document and save it as a macro-free document.

```csharp
[C#]
WordDocument doc = new WordDocument();
// Opens the Word macro-enabled document.
doc.Open("SourceDocument.docm", FormatType.Automatic);
// Determines whether the document has Macros.
if (doc.HasMacros)
{
    // Removes the macro commands present in the macro-enabled document.
    doc.RemoveMacros();
}
// Saves as the macro-free Word document.
doc.Save("OutDocument.docx", FormatType.Word2007);
```

<!-- tags: [DocIo, macros, Word, macro-enabled documents, C#, VB.NET] keywords: [DocIO, convert, macro, Word, document] -->
```