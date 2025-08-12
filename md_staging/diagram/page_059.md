```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_059.jpeg
document_name: diagram
page_number: 059
page_id: diagram#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:10:16Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- Describes how to set up the page layout for a diagram document.
- Explains the use of a dialog box for configuring page borders.
- Demonstrates code snippets for implementing page setup and border customization.

## Content

### Setting Up the Diagram Page

The following code snippet can be used for setting the page setup for a diagram document.

```csharp
[C#]
if (diagram1 == null || diagram1.Model == null)
    return;
using (PageSetupDialog dlgPageSetup = new
    PageSetupDialog(diagram1.View))
{
    if (dlgPageSetup.ShowDialog() == DialogResult.OK)
    {
        diagram1.UpdateView();
    }
}
```

#### Diagram Page Setup Dialog Box

Figure 31: Diagram page Setup Dialog Box

The page setup dialog box allows users to configure various settings such as printer paper size, orientation, and print zoom. Adjustments can be made visually, and settings are applied to the diagram page.

#### Page Borders

**2. Page Borders**

The **Page Borders** dialog provides an interactive form-based interface for setting the page borders of a diagram. This dialog initializes the `Syncfusion.Windows.Forms.Diagram.PageBorderDialog` with the `PageBorderStyle` property corresponding to the `Syncfusion.Windows.Forms.Diagram.View.PageBorderStyle` member of the diagram's view. This setup enables users to configure page border settings using the dialog controls.

The following code snippet can be used for setting the page border for a diagram document.

```csharp
[C#]
if (diagram1 != null && diagram1.Model != null)
```

### API Reference

**Page Border Properties**
- `Syncfusion.Windows.Forms.Diagram.View.PageBorderStyle`: Represents the style of the page border.
- `Syncfusion.Windows.Forms.Diagram.PageBorderDialog`: A dialog to configure page border settings.

### Code Examples

**Setting the Page Border**

```csharp
[C#]
if (diagram1 != null && diagram1.Model != null)
    diagram1.View.PageBorderStyle = PageBorderStyle.ThinLine;
```

### Conclusion

By utilizing the dialog interfaces and associated properties, developers can effectively manage the page setup and border configurations for diagrams in a Windows Forms application.

<!-- tags: [Syncfusion, WindowsForms, Diagram, PageSetup, BorderSettings] keywords: [diagram, page setup, border settings, dialog box, Syncfusion, Windows Forms, properties, API] -->
```