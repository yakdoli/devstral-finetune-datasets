```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_301.jpeg
document_name: XlsIO
page_number: 301
page_id: XlsIO#page_301
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:08:36Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- XlsIO supports OLE objects with two types of associations: linked and embedded types.
- Demonstrates linking an OLE object to an Excel document.

## Content

### OLE Objects and Linking Types

XlsIO supports two types of association of objects:
- Objects can be linked to the program
- Objects can be embedded in the program

#### 1. Linked Objects

Linked objects remain as separate files. The linked object would expect the object to be in the same location as created, when the file is opened in another machine.

#### Linking an OLE Object to an Excel document

The following sample code illustrates how to link an OLE Object to an Excel document.

```csharp
[C#]

Image image = Image.FromFile(@"..\..\image.png");

// Select the object to insert, image for the display icon and the type of
// the OLEObject field.
IOleObject ole2 = sheet.OleObjects.Add(@"..\..\Document.docx", image, OleLinkType.Link);

// Set the location
ole2.Location = sheet[5, 12];

// Set the size
```

---

## Cross References
- For further details on OleLinkType, refer to the relevant documentation.

<!-- tags: [xlsio, ole objects, linking, embedded objects, linked objects, c#, image display, document linking, version: 11.4.0.26] keywords: [excel, object linking, embedding, linking, object association, document embedding, linked, embedded, ole support, source file path] -->
```