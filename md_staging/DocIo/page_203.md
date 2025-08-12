```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_203.jpeg
document_name: DocIo
page_number: 203
page_id: DocIo#page_203
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:40:33Z
fidelity: lossless
-->

# Essential DocIO

## Adding OLE Objects to a Document

### C#

```csharp
WordDocument document = new WordDocument();
document.EnsureMinimal();

// Loads the OlePicture from the file.
WPicture pic = new WPicture(document);
pic.LoadImage(Image.FromFile(@"logo.jpg"));
pic.Width = 100f;
pic.Height = 100f;

// Adding new OLE Object.
document.LastParagraph.AppendOleObject(@"Startup.wav", pic, OleObjectType.Package);
```

### VB.NET

```vbnet
Dim document As WordDocument = New WordDocument()
document.EnsureMinimal()

' Loads the OlePicture from the file.
Dim pic As WPicture = New WPicture(document)
pic.LoadImage(Image.FromFile(@"logo.jpg"))
pic.Width = 100.0F
pic.Height = 100.0F

' Adding new OLE Object.
document.LastParagraph.AppendOleObject(@"startup.wav", pic, OleObjectType.Package)
```

### Extracting and Inserting OLE Objects

The following code example illustrates how to extract an OLE object from an existing document and insert it into a new document.

### C#

```csharp
WordDocument oleSource = new WordDocument("OleTemplate.doc");
WordDocument dest = new WordDocument();
dest.EnsureMinimal();

// Gets OLE object from source document.
WOLEObject oleObject = oleSource.LastParagraph.Items[0] as WOLEObject;
WPicture pic = oleObject.OlePicture.Clone() as WPicture;

// Inserts the OLE object into the destination document.
```

<!-- tags: [syncfusion-sdk, essential docio, ole objects, document manipulation, document api, ole insertion, ole extraction] keywords: [DocIO, OLE, WordDocument, WPicture, WOLEObject, OlePicture, OleObjectType, ensure minimal, append ole object] -->
```