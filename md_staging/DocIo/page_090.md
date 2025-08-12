```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_090.jpeg
document_name: DocIo
page_number: 090
page_id: DocIo#page_090
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:09Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Explains how to remove macros from a Word document using VB.NET code.
- Highlights the ability to control macro presence in destination macro-enabled documents.
- Demonstrates sample viewing instructions for demonstrating macro preservation in the Syncfusion Dashboard.

## Content

### Macro Removal Example

```vb
Dim doc As New WordDocument()
' Opens the Word macro-enabled document.
doc.Open("SourceDocument.docm", FormatType.Automatic)
' Determines whether the document has Macros.
If doc.HasMacros Then
    ' Removes the macro commands present in the macro-enabled document.
    doc.RemoveMacros()
End If
' Saves as the macro-free Word document.
doc.Save("OutDocument.docx", FormatType.Word2007)
```

> **Note:** Now macros will not be cloned/imported to the destination macro-enabled document while cloning/importing a macro-enabled document. If the macros are present in the destination macro-enabled document, then it will be preserved as it is in the macro-enabled document.

### Samples Link

To view samples:

1. Open the Syncfusion's Dashboard.
2. Select Reporting Edition, and then click ASP.NET.
> **Note:** You can select required platform under Reporting Edition.
3. Click Run Samples, and then click Doclo at the bottom.
4. Navigate to View > Macro Preservation.

### Track Changes

#### Track Changes feature enables you to keep track of the changes made to a document in Microsoft Word. Using this feature, you can maintain a record of every insertion, deletion, and modification in the document, including who made the change and when it was made. The objects that carry such information are called "Tracking Changes" or "Revisions".

---

## API Reference

None applicable in this specific context.

## Code Examples

Not applicable beyond the provided macro removal example in VB.NET.

## Page-level Navigation/TOC

Not explicitly provided in the content.

## Cross References

See also:
- Reporting Edition
- Dashboard Overview
- Track Changes Feature 

## RAG Annotations

<!-- tags: [DocIO, macro, track changes, VB.NET, Microsoft Word, document manipulation, Syncfusion Winforms] keywords: [DocIO, macro-enabled, RemoveMacros, WordDocument, doc.HasMacros, Track Changes, Reporting Edition, macro-preserving, document version control] -->
```