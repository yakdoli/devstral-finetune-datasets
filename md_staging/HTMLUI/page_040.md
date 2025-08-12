```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_040.jpeg
document_name: HTMLUI
page_number: 040
page_id: HTMLUI#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:04:48Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Demonstrates how to load file links in HTMLUI.
- Explains the process of loading the file from a URI (Uniform Resource Identifier).

## Content

### File Links Sample

**Figure 18: File Links Sample**
![](attachment:file-links-sample.png)

By default, this sample can be found under the following location:

```
C:\Documents and Settings\username\My Documents\Syncfusion\EssentialStudio\Version Number\Windows\HTMLUI.Windows\Samples\2.0\Loading HTML\File Links
```

#### 4.1.2.3 Loading the File From URI
HTML contents can also be loaded from the URI (Uniform Resource Identifier). This is a great advantage of HTMLUI that it can be used for browsing purposes like popular web browsers.

##### C#
```csharp
// Load the HTML document from the specified Uri in to HTMLUI Control.
Uri uri = new Uri("http://www.syncfusion.com");
htmluiControl1.LoadHTML(uri);
```

##### VB.NET
```vb
' Load the HTML document from the specified Uri in to HTMLUI Control.
```

## API Reference

### Loading HTML From a URI
- **Method:** `LoadHTML(Uri uri)`
  - **Parameters:**
    - `uri`: Type `System.Uri`
      - The URI representing the location of the HTML document to load.
  - **Description:**
    - Loads the HTML document from the specified URI into the HTMLUI control.
  - **Returns:**
    - `void`
  - **Exceptions:**
    - `System.ArgumentNullException`: If the `uri` parameter is null.
    - `System.InvalidOperationException`: If the HTMLUI control is not in a valid state to load the HTML.

### Parameters for Loading
- **C#:**
  - `Uri uri`: The URI to the HTML document.
- **VB.NET:**
  - `uri As Uri`: The URI to the HTML document.

## Code Examples

### C# Example
```csharp
using System;
using System.Windows.Forms;
using Syncfusion.HtmlUI.Windows.Forms;

public class Form1 : Form
{
    private HtmlUI htmluiControl1;

    public Form1()
    {
        InitializeComponent();

        // Load the HTML document from the specified Uri in to HTMLUI Control.
        Uri uri = new Uri("http://www.syncfusion.com");
        htmluiControl1.LoadHTML(uri);
    }

    private void InitializeComponent()
    {
        this.htmluiControl1 = new HtmlUI();
        this.SuspendLayout();
        // 
        // htmluiControl1
        // 
        this.htmluiControl1.Location = new System.Drawing.Point(12, 12);
        this.htmluiControl1.Name = "htmluiControl1";
        this.htmluiControl1.Size = new System.Drawing.Size(600, 400);
        this.htmluiControl1.TabIndex = 0;
        // 
        // Form1
        // 
        this.ClientSize = new System.Drawing.Size(624, 450);
        this.Controls.Add(this.htmluiControl1);
        this.Name = "Form1";
        this.ResumeLayout(false);
    }
}
```

### VB.NET Example
```vb
Imports System
Imports System.Windows.Forms
Imports Syncfusion.HtmlUI.Windows.Forms

Public Class Form1
    Inherits Form

    Private htmluiControl1 As HtmlUI

    Public Sub New()
        InitializeComponent()

        ' Load the HTML document from the specified Uri in to HTMLUI Control.
        Dim uri As New Uri("http://www.syncfusion.com")
        htmluiControl1.LoadHTML(uri)
    End Sub

    Private Sub InitializeComponent()
        Me.htmluiControl1 = New HtmlUI()
        Me.SuspendLayout()
        '
        ' htmluiControl1
        '
        Me.htmluiControl1.Location = New System.Drawing.Point(12, 12)
        Me.htmluiControl1.Name = "htmluiControl1"
        Me.htmluiControl1.Size = New System.Drawing.Size(600, 400)
        Me.htmluiControl1.TabIndex = 0
        '
        ' Form1
        '
        Me.ClientSize = New System.Drawing.Size(624, 450)
        Me.Controls.Add(Me.htmluiControl1)
        Me.Name = "Form1"
        Me.ResumeLayout(False)
    End Sub
End Class
```

## Page-level Navigation/TOC
- 4.1.2.3 Loading the File From URI
  - File Links Sample
  - Loading HTML From a URI

## Cross References
- **Related Topics:**
  - Essential HTMLUI for Windows Forms
  - File links and URI loading in Syncfusion HTMLUI

<!-- tags: [htmlui, windowsforms, uri, filelinks, syncfusion, 11.4.0.26] keywords: [htmlui, uri, file links, loading, windows forms, syncfusion, file location, document loading, html document, code examples] -->
```