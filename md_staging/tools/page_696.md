```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_696.jpeg
document_name: tools
page_number: 696
page_id: tools#page_696
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:28:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section describes the FolderBrowser method and its properties.
- Demonstrates how to use FolderBrowser with both code and design approaches.

## Content

### FolderBrowser Method

This method is a modal function, and if the return code indicates success, the `FolderBrowser.DirectoryPath` property may be used to access the selected folder.

#### Code Examples

- **C#**
  ```csharp
  this.folderBrowser1.ShowDialog();
  ```

- **VB.NET**
  ```vb
  Me.folderBrowser1.ShowDialog()
  ```

#### FolderBrowser UI

![](./image.png)
*Figure 434: FolderBrowser created Through Designer*

##### FolderBrowser UI Description
The FolderBrowser dialog allows the user to navigate and select a folder. The options displayed include:

- **My Computer**
  - `3½ Floppy (A:)`
  - `Local Disk (C:)`
  - `CD-RW Drive (D:)`
  - `My Sharing Folders`

### Programmatic Approach

The programmatic approach for using the FolderBrowser component is shown below.

1. **Create an instance of the FolderBrowser component.**

#### See Also
- **Through Code**
- **3.5.7.1.2.2 Through Code**

The programmatic approach for using the FolderBrowser component is shown below.

---

### API Reference (If applicable)

#### Properties
- **DirectoryName**: Gets or sets the path of the folder that will be initially displayed when the dialog is shown.

#### Methods
- **ShowDialog()**: Displays the folder selection dialog.

---

### Code Examples

#### Example: Using FolderBrowser in Windows Forms

**C#**
```csharp
using Syncfusion.Windows.Forms.Tools;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();
        FolderBrowser browser = new FolderBrowser();
        if (browser.ShowDialog() == DialogResult.OK)
        {
            string selectedDirectory = browser.DirectoryPath;
            // Use the selected directory path
        }
    }
}
```

**VB.NET**
```vb
Imports Syncfusion.Windows.Forms.Tools

Public Class Form1
    Inherits Form

    Public Sub New()
        InitializeComponent()
        Dim browser As New FolderBrowser()
        If browser.ShowDialog() = DialogResult.OK Then
            Dim selectedDirectory As String = browser.DirectoryPath
            ' Use the selected directory path
        End If
    End Sub
End Class
```

## References

### See Also
- [Through Code](#through-code)
- [3.5.7.1.2.2 Through Code](#3.5.7.1.2.2-through-code)

---

<!-- tags: [tools, folderbrowser, windows forms, essentialutils, syncfusion winforms, design time, runtime, properties, methods, events] keywords: [folderbrowser, dialog, directorypath, modal function, programmatic approach, code example, windows forms, syncfusion] -->
```