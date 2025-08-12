```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_092.jpeg
document_name: DocIo
page_number: 092
page_id: DocIo#page_092
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:54Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- This section describes how to check and accept track changes in a Word document.
- It includes code examples to demonstrate字体 substitution techniques for Word documents.

## Content

### WinForms-specific code example

```vb
[VB]

Dim doc As Syncfusion.DocIO.DLS.WordDocument = New WordDocument(".../.../Essential DocIO.doc", FormatType.Doc)
For Each section As WSection In doc.Sections
    For i As Integer = 0 To section.Paragraphs.Count - 1
        para = section.Paragraphs(i)

        ' Check each paragraph items revisions.
        For Each item As ParagraphItem In para.Items
            Console.WriteLine((item.EntityType.ToString() & " Inserted: ") + item.IsInsertRevision.ToString())
            Console.WriteLine((item.EntityType.ToString() & "Deleted:") + item.IsDeleteRevision.ToString())
        Next
    Next
Next

' Accept tracking changes of the document.
doc.AcceptChanges()
doc.Save("sample.doc")
```

### 4.2.7 Font Substitution for Word Documents

Font substitution is the process of using an alternate font for fonts that are not installed in the system. MS Word renders the text based on the alternate font defined, if the actual font is not installed in the system. MS Word displays the actual font name of the text in the font dialog box, but the text will be rendered based on the alternate font. Below screen shot illustrates the “Arial (W1)” font is substituted by the alternate font “Gabriola” in MS Word document.

## API Reference (if applicable)

### Code Examples

The provided code examples demonstrate how to:
1. Check and process tracked changes in a Word document.
2. Accept all tracked changes in a document.

## Cross References

See also:
- Other sections related to Word document handling and font management.

<!-- tags: DocIO, Word Documents, Font Substitution, Track Changes, WinForms, C# Examples, VB Examples, Syncfusion, Word Document Processing keywords: track changes, font substitution, Word document, MS Word, text rendering, alternate font, Gabriola, Arial -->
```