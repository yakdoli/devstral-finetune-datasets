```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_032.jpeg
document_name: HTMLUI
page_number: 032
page_id: HTMLUI#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:04:27Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Introduction to HTMLUI control properties grid.
- Explanation of configuring the Startup Document using code.
- Code examples in C# and VB.NET for setting the Startup Document.

## Content

### HTMLUI Properties Grid

![HTMLUI Properties Grid](https://placeholder.com/image)

**Figure 12: HTMLUI Properties Grid**

Before the form is displayed for the first time, the `StartupDocument` for the HTMLUI control should be written in the `form_load` event handler.

#### C# Example

```csharp
// Get or Set the path to the Startup Document for the control.
private void Form1_Load(object sender, System.EventArgs e)
{
    this.htmluiControl1.StartupDocument = @"C:\MyProjects\Startup\startup_page.htm";
}
```

#### VB.NET Example

```vb
' Get/Set the path to the Startup Document for the control.
Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.htmluiControl1.StartupDocument = "C:\MyProjects\Startup\startup_page.htm"
End Sub
```

### Loading an HTML Document as the Startup Document

The following image illustrates the process of loading an HTML document as the Startup Document.

<!-- tags: [HTMLUI, StartupDocument, Form_Load, C#, VB.NET, Windows Forms, Syncfusion] keywords: [Startup Document, HTMLUI, Code Examples, Windows Forms, Start-up Configuration] -->
```