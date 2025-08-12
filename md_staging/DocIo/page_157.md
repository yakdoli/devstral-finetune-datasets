```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_157.jpeg
document_name: DocIo
page_number: 157
page_id: DocIo#page_157
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:38:09Z
fidelity: lossless
-->

## Overview

- Demonstrates the process of finding and replacing web hyperlinks in a document using the `DocIO` library.
- Explains how to manipulate hyperlinks, specifically converting an email link to a standard web link.

## Content

### Handling Hyperlinks in Documents

The following code illustrates how to find and replace the web hyperlinks.

| Column 1                           | Column 2                                                                                         |
|------------------------------------|--------------------------------------------------------------------------------------------------|
|                                   | EMailLink - Sets the URI <br> Bookmark - Sets the name of the bookmark <br> FileLink - Sets the file path |
| TextToDisplay                      | Gets or sets the text, which will be displayed on the place of hyperlink.                              |

#### Example Code: C#

```csharp
WordDocument doc = new WordDocument();
doc.Open("WebLink_1.doc");
Hyperlink hlink = null;

foreach (ParagraphItem item in doc.LastParagraph.Items)
{
    if (item is WField && (item as WField).FieldType == FieldType.FieldHyperlink)
    {
        hlink = new Hyperlink(item as WField);
        if (hlink.Type == HyperlinkType.EMailLink)
        {
            hlink.Type = HyperlinkType.WebLink;
            hlink.TextToDisplay = "Football";
            hlink.Uri = "http://www.football.ua/";
        }
    }
}
doc.Save("WebLink_modified.doc");
```

#### Example Code: VB.NET

```vb
Dim doc As New WordDocument()
doc.Open("WebLink_1.doc")
Dim hlink As Hyperlink = Nothing
For Each item As ParagraphItem In doc.LastParagraph.Items
    If TypeOf item Is WField AndAlso TryCast(item, WField).FieldType = FieldType.FieldHyperlink Then
        hlink = New Hyperlink(TryCast(item, WField))
        If hlink.Type = HyperlinkType.EMailLink Then
            hlink.Type = HyperlinkType.WebLink
            hlink.TextToDisplay = "Football"
            hlink.Uri = "http://www.football.ua/"
        End If
    End If
Next
doc.Save("WebLink_modified.doc")
```

### Explanation

- **Opening the Document**: The document is opened using the `WordDocument` class.
- **Iterating Through Paragraph Items**: The code iterates through each `ParagraphItem` in the last paragraph of the document.
- **Checking for Hyperlinks**: It checks if an item is a `WField` of type `FieldHyperlink`.
- **Converting Email Links to Web Links**: If the hyperlink type is an email link (`EMailLink`), it converts it to a web link (`WebLink`) by setting the `Type`, `TextToDisplay`, and `Uri` properties.
- **Saving the Modified Document**: The modified document is saved with a new filename.

## API Reference

### `Hyperlink`

- **Properties**
  - `Type`: Sets the type of hyperlink (e.g., `HyperlinkType.WebLink`, `HyperlinkType.EMailLink`).
  - `TextToDisplay`: Gets or sets the text displayed for the hyperlink.
  - `Uri`: Sets the URI for web or email links.

### `WField`

- **Properties**
  - `FieldType`: Represents the type of field in the document.
  - `FieldHyperlink`: Indicates that the field is a hyperlink.

## Code Examples

The provided code examples demonstrate how to:
- Open a document.
- Identify hyperlinks in the document.
- Modify the hyperlink type and details.
- Save the modified document with changes.

## Page-level Navigation/TOC

This section provides a code snippet to handle hyperlinks by converting email links to web links, complete with both C# and VB.NET implementations. It is a practical example of using the `DocIO` library for documents.

## Cross References

See also:
- Documentation on `DocIO` library for handling various document types.
- Examples of other hyperlink types, such as `FileLink` and `Bookmark`.

<!-- tags: DocIO, WinForms, Hyperlinks, Document Manipulation, C#, VB.NET, version 11.4.0.26 keywords: HyperlinkType, EMailLink, WebLink, FileLink, Bookmark, DocIO, WordDocument, WField, FieldType, Hyperlink, Document Manipulation -->
```