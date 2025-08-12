```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_097.jpeg
document_name: HTMLUI
page_number: 097
page_id: HTMLUI#page_097
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:08:26Z
fidelity: lossless
-->

## Essential HTMLUI for Windows Forms

```html
<ul>
    <li>Essential HTMLUI</li>
</ul>
</body>
</html>
```

### C#
```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\listItem\ul.html");
```

### VB.NET
```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\listItem\ul.html")
```

### 4.6.35 HTML Tags Sample

This sample shows the various Tags supported in HTMLUI.

![HTML Tags Sample](https://res.cloudinary.com/dcrcnpotn/image/upload/v1691715350/htmlui_page_097_image.png)
*FigurFigure 27: HTMLTags Sample*

### Conclusion
The HTMLUI control in Windows Forms allows developers to leverage HTML elements directly within their applications. The provided sample demonstrates how to load HTML content into an HTMLUI control, showcasing support for various HTML tags and their rendering within the UI.

### Code Example
Below is a complete example demonstrating how to use HTMLUI with dynamic HTML content:

```csharp
// C#
using Syncfusion.HtmlUI.Windows.Forms;

public partial class MainForm : Form
{
    public MainForm()
    {
        InitializeComponent();

        // Load HTML content into the HTMLUI control
        htmluiControl1.LoadHTML(@"<h1>This is Heading 1</h1>");
    }
}

```vb
' VB
Imports Syncfusion.HtmlUI.Windows.Forms

Public Partial Class MainForm
    Inherits Form

    Public Sub New()
        InitializeComponent()

        ' Load HTML content into the HTMLUI control
        htmluiControl1.LoadHTML("<h1>This is Heading 1</h1>")
    End Sub
End Class
```

### API Reference

- **Namespace**: `Syncfusion.HtmlUI.Windows.Forms`
- **Class**: `HtmlUIControl`
- **Method**: `LoadHTML(string html)`
  - **Parameters**:
    - `html`: The HTML content to be loaded.
  - **Returns**: None
  - **Description**: Loads and renders the specified HTML content into the HtmlUIControl.

### Cross References
- Refer to the HTMLUI documentation for more details on supported tags and rendering capabilities.
- For additional examples and configurations, see the Syncfusion WinForms Samples Library.

<!-- tags: HTMLUI, Windows Forms, WinForms, HTML rendering, Syncfusion, C#, VB.NET -->
```