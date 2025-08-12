```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_191.jpeg
document_name: edit
page_number: 191
page_id: edit#page_191
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:05:28Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
this.editControl.SaveFile("Temp.txt", Encoding.Unicode, 
Syncfusion.IO.NewLineStyle.Control);
```

```csharp
// Displays the Save File dialog.
this.editControl.Save();
```

```csharp
// Displays the SaveAs dialog.
this.editControl.SaveAs();
```

```csharp
// Saves the contents of the file after modification, when a new file is loaded, or when a file is closed.
this.editControl.SaveModified();
```

## [VB.NET]

```vb
' Saves the contents of the file.
Me.editControl.SaveFile("Temp.txt", Encoding.Unicode, 
Syncfusion.IO.NewLineStyle.Control)
```

```vb
' Displays the Save File dialog.
Me.editControl.Save()
```

```vb
' Displays the SaveAs dialog.
Me.editControl.SaveAs()
```

```vb
' Saves the contents of the file after modification, when a new file is loaded, or when a file is closed.
Me.editControl.SaveModified()
```

## Dropping Files

Files can be dropped onto the Edit Control by using the properties given below.

| **Edit Control Property** | **Description** |
|---------------------------|------------------|
| DropAllFiles             | Gets / sets value indicating whether all files can be dropped onto Edit Control. If set to False, only files with extensions contained in FileExtensions can be dropped. |
| FileExtensions           | Gets / sets extensions of files that can be dropped to Edit Control. |

## Code Examples

### [C#]

```csharp
/* [C#] */
```

### [VB.NET]

```vb
' [C#]
```

<!-- tags: windowsforms, edit control, saving, file handling, file properties, file extensions, dropping files, Syncfusion.WinForms.EditControl -->
```