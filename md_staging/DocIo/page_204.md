```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_204.jpeg
document_name: DocIo
page_number: 204
page_id: DocIo#page_204
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:41:10Z
fidelity: lossless
-->

## Overview
- This section discusses embedding OLE objects into a Word document using the DocIO library. It highlights the use of VB.NET code to extract and insert OLE objects into a destination document. Additionally, it introduces styles and formatting in Word documents, detailing the different style types supported.

### Summary
- OLE object handling and embedding in Word documents.
- Explanation of styles and formatting, including character, paragraph, and table styles.
- Description of DocIO's functionality for managing Word styles and emphasizing limitations such as the lack of support for table styles.

## Content

### Embedding OLE Objects

Here is an example of appending an OLE object to a paragraph in a Word document using VB.NET.

```vb
Dim oleSource As WordDocument = New WordDocument("OleTemplate.doc")
Dim dest As WordDocument = New WordDocument()
dest.EnsureMinimal()

' Gets OLE object from source document.
Dim oleObject As WOleObject = TryCast(oleSource.LastParagraph.Items(0), WOleObject)
Dim pic As WPicture = TryCast(oleObject.OlePicture.Clone(), WPicture)

' Inserts the OLE object into the destination document.
dest.LastParagraph.AppendOleObject(oleObject.Container, pic, OleLinkType.Embed)
```

#### Notes
- **Currently OLE Object support is not available in Silverlight application.**

---

### 4.4.2 Styles and Formatting

Every word document contains a number of styles. They are as follows:

- **Character Style**
- **Paragraph Style**
- **Table Style**

In Word document style hierarchy, there is also a base style, **Normal**.

DocIO has three classes which represent Word styles:

- **CharacterStyle**: represents Word character style
- **WParagraphStyle**: represents Word paragraph style
- **ListStyle**: represents list properties in the Word paragraph style

**Note**: DocIO does not support table styles.

DocIO gives user an opportunity to add user-defined paragraph and list styles to the document. For details, see `WParagraphStyle`.

## Page-level Navigation/TOC (if applicable)
- **4.4.2 Styles and Formatting**

## Cross References
- See also: User-defined paragraph and list styles in the document (`WParagraphStyle`).

<!-- tags: [DocIO, Word document, OLE object, embedding, styles, formatting, paragraph style, character style, table style, base style, Normal, Silverlight, WParagraphStyle] keywords: [Embedding OLE objects, WordDocument, Silverlight limitation, styles and formatting, character style, paragraph style, table style, base style, Normal, DocIO limitations, user-defined styles, OLETemplate.doc, WParagraphStyle class] -->
```