```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_670.jpeg
document_name: tools
page_number: 670
page_id: tools#page_670
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:27:48Z
fidelity: lossless
-->

### Essential Tools for Windows Forms

#### Setting the BackgroundColor Properties for the GradientPanelExt

**Figure 412: Setting the BackgroundColor properties for the GradientPanelExt**

This section demonstrates how to set the `BackgroundColor` property for the `GradientPanelExt` control in a Windows Forms application. Below is a detailed explanation of the process, including both the property grid settings and the equivalent code snippet:

## Property Grid Setup

In the property grid, you can configure the `BackgroundColor` for the `GradientPanelExt` control as follows:

- **BackgroundColor**: Set to `Gradient; PathEllipse; LightCoral`.
- **Style**: Set to `Gradient`.
- **BackColor**: Set to `Bisque`.
- **ForeColor**: Set to `LightCoral`.
- **GradientStyle**: Set to `PathEllipse`.
- **GradientColors**: Set to a collection of colors: `Bisque`, `LightSalmon`, `LightCoral`.

## Code Snippet for Setting BackgroundColor

Alternatively, the `BackgroundColor` for the control can be set programmatically using the following snippets:

### C#

```csharp
gradientPanelExt1.BackgroundColor = new
Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.PathEllipse,
    new System.Drawing.Color[] {
        System.Drawing.Color.Bisque,
        System.Drawing.Color.LightSalmon,
        System.Drawing.Color.LightCoral});
```

### VB.NET

```vb
Private gradientPanelExt1.BackgroundColor = New
Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.PathEllipse,
    New System.Drawing.Color() {
        System.Drawing.Color.Bisque, System.Drawing.Color.LightSalmon,
        System.Drawing.Color.LightCoral})
```

This approach provides flexibility in dynamically setting the gradient background color based on application logic or user preferences.

<!-- tags: [GradientPanelExt, WinForms, backgroundColor, propertyGrid, GradientStyle, PathEllipse, C#, VB.NET, Syncfusion.Drawing.BrushInfo] keywords: [GradientPanelExt, backgroundColor, WinForms, propertyGrid, GradientStyle, PathEllipse, C#, VB.NET, Syncfusion, Windows Forms] -->
```