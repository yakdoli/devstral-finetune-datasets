```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_173.jpeg
document_name: HTMLUI
page_number: 173
page_id: HTMLUI#page_173
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:13:12Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Demonstrates how to set the path to the Startup Document for an HTMLUI control.
- Explains loading HTML documents at runtime from disk and URI.

## Content

### Setting the Startup Document

In the following example, the path to the Startup Document for the HTMLUI control is configured during the initialization of the form.

```csharp
[C#]

// Get or Set the path to the Startup Document for the control.
private void Form1_Load(object sender, System.EventArgs e)
{
    this.htmluiControl1.StartupDocument = 
        @"C:\MyProjects\Startup\startup_page.htm";
}
```

```vb.net
[VB.NET]

' Get or Set the path to the Startup Document for the control.
Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.htmluiControl1.StartupDocument = "C:\MyProjects\Startup\startup_page.htm"
End Sub
```

### 5.13.2 Loading At Run Time

HTML documents can also be loaded at runtime. For example, in a file link where an HTML file may link to another file. In that case, a new file is loaded in the control after the one that was initially loaded.

The various ways of loading the document at runtime from various resources are:

#### Loading from Disk

To load the file from disk into the HTMLUI, the following code snippet can be used.

```csharp
[C#]

// Load the specified HTML document from Disk at runtime.
string filepath = @"C:\MyProjects\LoadHTML\FromDisk.htm";
this.htmluiControl1.LoadHTML(filepath);
```

```vb.net
[VB.NET]

' Load the specified HTML document from Disk at runtime.
Private filepath As String = "C:\MyProjects\LoadHTML\FromDisk.htm"
Me.HtmluiControl1.LoadHTML(filepath)
```

The above snippet can also be used to load HTML documents which are linked to the specified HTML documents, as links are easily invoked in HTMLUI.

#### Loading from URI

To load a file from the URI, the following code snippet can be used.

```csharp
[C#]
```

---
© 2013 Syncfusion. All rights reserved. 173 | Page
```

<!-- tags: [htmlui, windows forms, startup document, runtime loading, file links] keywords: [htmlui, windows forms startup document, load html from disk, load html from uri, runtime document loading, file links] -->
```