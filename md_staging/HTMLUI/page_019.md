```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_019.jpeg
document_name: HTMLUI
page_number: 019
page_id: HTMLUI#page_019
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:03:36Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- The `HTMLUI` control in Windows Forms is designed for loading and displaying HTML content.
- This example illustrates how to handle file loading using the `OpenFileDialog` control.

## Content

### C# Implementation

```csharp
this menuItem2.Click += new System.EventHandler(this.menuItem2_Click);

private void menuItem2_Click(object sender, System.EventArgs e)
{
    // Gets or Sets the initial directory displayed by file dialog box
    openDlg.InitialDirectory = GetFilesLocation();

    // Gets or Sets the current file name filter string, which determines the
    // choices that appear in the "Save as File Type" or "File of Type" box in the dialog box.
    openDlg.Filter = "HTML files (*.htm)|*.htm|HTML Files (*.html)|*.html";

    if (DialogResult.OK == openDlg.ShowDialog())
    {
        string filePath = openDlg.FileName;
        this.htmluiControl1.LoadHTML(filePath);
    }
}
```

### VB.NET Implementation

```vb.net
Me.menuItem2.Click += New System.EventHandler(Me.menuItem2_Click)

Private Sub menuItem2_Click(ByVal sender As Object, ByVal e As System.EventArgs)
    ' Gets or Sets the initial directory displayed by file dialog box
    openDlg.InitialDirectory = GetFilesLocation()

    ' Gets or Sets the current file name filter string, which determines the
    ' choices that appear in the "Save as File Type" or "File of Type" box in the dialog box.
    openDlg.Filter = "HTML files (*.htm)|*.htm|HTML Files (*.html)|*.html"

    If DialogResult.OK = openDlg.ShowDialog() Then
        Dim filePath As String = openDlg.FileName
        Me.htmluiControl1.LoadHTML(filePath)
    End If
End Sub
```

### Instructions

5. Now run the sample and try loading an HTML document into the HTMLUI control.

<!-- tags: [HTMLUI, WindowsForms, openFileDialog, html, loading, C#, VB.NET] keywords: [HTMLUI, Windows Forms, openFileDialog, LoadHTML] -->
```