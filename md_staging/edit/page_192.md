```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_192.jpeg
document_name: edit
page_number: 192
page_id: edit#page_192
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:05:00Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
// Drops all files onto Edit Control.
this.editControl.DropAllFiles = true;

// Specifies the file extensions of files that can be dropped onto Edit Control.
this.editControl.FileExtensions = new string[] { ".cs", ".sql", ".vb", ".xml" };
```

```vb.net
' Drops all files onto Edit Control.
Me.editControl.DropAllFiles = True

' Specifies the file extensions of files that can be dropped onto Edit Control.
Me.editControl.FileExtensions = New String() { ".cs", ".sql", ".vb", ".xml" }
```

## 4.8.2 Loading And Saving Contents

The contents of the Edit Control can be loaded and saved to a particular stream. This can be achieved by using the methods given below.

| Edit Control Method | Description |
| --- | --- |
| LoadStream | Loads the stream and the corresponding configuration. |
| FlushChanges | Flushes changes to the current stream. |
| SaveStream | Saves content to the specified stream using specified encoding and line end style. |

```csharp
// Loads the content of the specified stream into the Edit Control.
this.editControl.LoadStream(streamName);

// Loads the specified stream and configuration.
this.editControl.LoadStream(streamName, config);

// Saves changes made to the contents of the Edit Control into the current stream.
```

<!-- tags: [Syncfusion, WinForms, Edit Control, Drag and Drop, File Extensions, LoadStream, FlushChanges, SaveStream, version 11.4.0.26] keywords: [edit control, drag and drop functionality, file extensions, stream management, C#, VB.NET, loading content, saving content, configuration, encoding, line end style] -->
```