```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_302.jpeg
document_name: XlsIO
page_number: 302
page_id: XlsIO#page_302
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:07:24Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
ole2.Size = new Size(30, 30);
```

## Example Code: Inserting an OLE Object in VB.NET

```vb
' Load the image file
Dim image As Image = Image.FromFile("...\image.png")

' Select the object to insert: image for the display icon and the type of the OLEObject field.
Dim ole2 As IOleObject = sheet.OleObjects.Add("...\Document.docx", image, OleLinkType.Link)

' Set the location
ole2.Location = sheet(5, 12)

' Set the size
ole2.Size = New Size(30, 30)
```

### Output

Run the code. The following output is generated.

## Summary

- This example demonstrates how to insert an OLE object in a worksheet using VB.NET, including specifying the object location, size, and the display icon.

<!-- tags: [Syncfusion, Winforms, XlsIO, OLEObjects] keywords: [VB.NET, OleObject, Location, Size, DisplayIcon, OLEObjectField, Sheet, Insert, Example] -->
```