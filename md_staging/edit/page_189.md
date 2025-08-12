```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_189.jpeg
document_name: edit
page_number: 189
page_id: edit#page_189
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:28Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## 4.8.1 Creating, Loading, Saving And Dropping Files

This section discusses the file operations supported in Edit Control.

### Creating Files

The New and NewFile methods are used to create a new stream or file, and optionally allow you to set the language to be used by specifying the appropriate configuration settings.

| **Edit Control Method** | **Description**                                                                 |
|--------------------------|--------------------------------------------------------------------------------|
| New                      | Creates an empty stream and allows the editor to for editing.                |
| NewFile                  | Creates new empty file with specified coloring.                               |

**[C#]**

```csharp
// Creates a new stream with default configuration settings.
this.editControl.New();

// Creates a new file with default configuration settings.
this.editControl.NewFile();

// Creates a new stream with specified configuration settings.
this.editControl.New(ConfigLanguage lang);

// Creates a new file with specified configuration settings.
this.editControl.NewFile(IConfigLanguage lang);
```

**[VB.NET]**

```vbnet
' Creates a new file.
Me.editControl.NewFile()

Me.editControl.[New]()

' "config" is Configuration Settings file of type IConfigLanguage.
Me.editControl.NewFile(config)

Me.editControl.[New](config)
```

### Loading Files
```html
<!-- tags: [Winforms, EditControl, New, NewFile, FileOperations, StreamCreation, LanguageConfiguration, C#, VB.NET] keywords: [creating files, edit control, default settings, configuration, language settings, new stream, new file, C# example, VB.NET example] -->
``` 
``` Contemporary