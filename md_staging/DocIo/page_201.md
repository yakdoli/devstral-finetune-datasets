```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_201.jpeg
document_name: DocIo
page_number: 201
page_id: DocIo#page_201
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:41:19Z
fidelity: lossless
-->

## Inserting Objects

**DoclO** provides various overloads for the `AppendOleObject` method to enable insertion of objects as bytes or streams by using a single line of code. The following overloads of the `AppendOleObject` can be used to insert an OLE object.

- **AppendOleObject(byte[] oleBytes, WPicture olePicture, OleObjectType type)**
- **AppendOleObject(byte[] oleBytes, WPicture olePicture, string fileExtension)**
- **AppendOleObject(Stream oleStream, WPicture olePicture, OleObjectType type)**
- **AppendOleObject(Stream oleStream, WPicture olePicture, string fileExtension)**

The following code examples illustrate insertion of an OLE object by using this method.

### C#
```csharp
paragraph.AppendOleObject(buffer, pic, OleObjectType.AdobeAcrobatDocument);
paragraph.AppendOleObject(buffer, pic, "pdf");
paragraph.AppendOleObject(stream, pic, OleObjectType.Excel_97_2003_Worksheet);
paragraph.AppendOleObject(stream, pic, "pdf");
```

### VB
```vb
paragraph.AppendOleObject(Buffer, pic, OleObjectType.AdobeAcrobatDocument)
paragraph.AppendOleObject(Buffer, pic, "pdf")
paragraph.AppendOleObject(stream, pic, OleObjectType.Excel_97_2003_Worksheet)
paragraph.AppendOleObject(stream, pic, "pdf")
```

DoclO not only allows inserting objects through container, but also allows inserting objects from disk through file path by using the following overload:

- **AppendOleObject(string pathToFile, WPicture olePicture, OleObjectType oleObjectFileType)**

### DisplayAsIcon

**Essential DoclO** provides support for embedding OLE objects in a Word document to display them as icons or content using the `DisplayAsIcon` property.

- **If the `DisplayAsIcon` property is set to true**, the OLE object in the Word document is displayed as an icon.
- **If the `DisplayAsIcon` property is set to false**, the OLE object in the Word document is displayed as content. This enables the Word document to dynamically update images based on the content present within the OLE object.

```html
<!-- tags: [DocIo, OLE objects, embedding, DisplayAsIcon, OLEObject, stream, file path, Word document] keywords: [inserting objects, AppendOleObject, OleObjectType, OLE object insertion, display options, dynamic content updating, OLE object types] -->
``` 
```