```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_110.jpeg
document_name: HTMLUI
page_number: 110
page_id: HTMLUI#page_110
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:09:39Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Demonstrates the usage of Syncfusion HTMLUI Control in rendering an HTML Editor.
- Provides an example of implementing a web browser in HTMLUI.

## Content

### HTMLUI Browser Sample

This sample demonstrates the implementation of a Web Browser in HTMLUI.

**Figure 37: HTML Editor rendered by using the HTMLUI Control**

![HTML Editor rendered by using the HTMLUI Control](https://example.com/image_url)

### Description
The figure illustrates the rendered HTML Editor using the HTMLUI Control. The editor displays the content with a background color set to `#dae5f5` and the text "Syncfusion HTMLUI" styled within `<pre>` tags. The corresponding HTML code is also visible below the rendered content, showing how the layout and styles are defined.

### HTML Code Example
Below is the HTML code snippet used to render the content displayed in the HTML Editor:

```html
<HTML>
<head>
  <title>Editor</title>
</head>
<body bgcolor="#dae5f5">
  <h2><pre>Syncfusion HTMLUI</pre></h2>
</body>
</HTML>
```

### Key Features
- **Rendering HTML Content**: The HTMLUI Control seamlessly renders HTML content within a Windows Forms application.
- **Customizable Output**: Allows customization of styles and layout using standard HTML and CSS.

### Additional Notes
The example showcases the simplicity and versatility of using HTMLUI for incorporating web-like functionality within Windows Forms applications.

## API Reference
- **Control Name**: Syncfusion.Windows.Forms.HTMLUI
- **Namespace**: Syncfusion.Windows.Forms

### Properties
- `HTML`: Contains the HTML content to be rendered.
- `Refresh()`: Updates the rendered content based on the latest HTML.

## Code Examples

### Example Using C#
```csharp
using Syncfusion.Windows.Forms.HTMLUI;

public class HTMLUIExample
{
    public void RenderHTMLUI()
    {
        // Initialize HTMLUI control
        HTMLUI htmlUI = new HTMLUI();

        // Set the HTML content
        htmlUI.HTML = @"
<HTML>
<head>
  <title>Editor</title>
</head>
<body bgcolor=""#dae5f5"">
  <h2><pre>Syncfusion HTMLUI</pre></h2>
</body>
</HTML>";

        // Refresh to display the content
        htmlUI.Refresh();
    }
}
```

### Example Using VB.NET
```vb.net
Imports Syncfusion.Windows.Forms.HTMLUI

Public Class HTMLUIExample
    Public Sub RenderHTMLUI()
        ' Initialize HTMLUI control
        Dim htmlUI As New HTMLUI()

        ' Set the HTML content
        htmlUI.HTML = @"
<HTML>
<head>
  <title>Editor</title>
</head>
<body bgcolor=""#dae5f5"">
  <h2><pre>Syncfusion HTMLUI</pre></h2>
</body>
</HTML>"

        ' Refresh to display the content
        htmlUI.Refresh()
    End Sub
End Class
```

## Cross References
- **Related Topics**: This section provides additional information on HTMLUI and its usage within Windows Forms applications.
- **See also**: Refer to the documentation for advanced styling options and other controls available in Syncfusion WinForms.

## References
- **Version**: Syncfusion WinForms 11.4.0.26
- **Copyright**: © 2013 Syncfusion. All rights reserved.

<!-- tags: [Syncfusion, WinForms, HTMLUI, Control, Windows Forms, Web Browser, Editor, Rendering, HTML] keywords: [HTMLUI Control, Windows Forms, Web Browser, HTML Editor, Syncfusion, HTML Rendering, C#, VB.NET, Code Example, Documentation] -->
```