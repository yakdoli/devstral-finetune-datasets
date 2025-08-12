```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_193.jpeg
document_name: edit
page_number: 193
page_id: edit#page_193
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:39Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
this.editControl1.FlushChanges();

// Saves content to the specified stream using specified encoding and line end style.
this.editControl1.SaveStream(System.IO.Stream.Null, Encoding.BigEndianUnicode, Syncfusion.IO.NewLineStyle.Mac);
```

## [VB.NET]

```vb
' Loads the content of the specified stream into the edit control.
Me.editControl1.LoadStream(streamName)

' Loads the specified stream and configuration.
Me.editControl1.LoadStream(streamName, config)

' Saves changes made to the contents of the Edit Control into the current stream.
Me.editControl1.FlushChanges()

' Saves content to the specified stream using specified encoding and line end style.
Me.editControl1.SaveStream(System.IO.Stream.Null, Encoding.BigEndianUnicode, Syncfusion.IO.NewLineStyle.Mac)
```

### Getting Details of Currently Loaded File

The name of the file that is currently loaded can be set by using the `FileName` property.

| Edit Control Property | Description                                      |
|-----------------------|--------------------------------------------------|
| FileName              | Gets / sets the name of the currently opened file. |

### [C#]

```csharp
// Gets or sets the name of the file loaded in the Edit Control.
this.editControl1.FileName = "Temp.txt";
```

### [VB.NET]

```vb
' Gets or sets the name of the file loaded in the Edit Control.
Me.editControl1.FileName = "Temp.txt"
```

<!-- tags: [essential edit, windows forms, edit control, stream, encoding, new line style, file name, loading, saving] keywords: [edit control, windows forms, file name, stream operations, encoding, new line style, loading file, saving file, flush changes] -->
```