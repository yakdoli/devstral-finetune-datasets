```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_674.jpeg
document_name: tools
page_number: 674
page_id: tools#page_674
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:28:01Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Utilizes the GradientPanelExt control with CornerRadius property.
- Demonstrates how to enable or disable rounded corners using the CornerRadius property.
- Shows code examples in both C# and VB.NET to set the CornerRadius value.

## Content

### CornerRadius Property

#### Figure 416: GradientPanelExt with CornerRadius

The CornerRadius can be turned off by giving a value of zero for it.

```csharp
gradientPanelExt1.CornerRadius = 0;
```

```vb
Private gradientPanelExt1.CornerRadius = 0
```

#### Figure 417: GradientPanelExt without Rounded Corners

![GradientPanelExt without Rounded Corners](image.png)

### Border Gap

This section introduces the concept of configuring the border gap of the GradientPanelExt control.

## Border Gap

[To Be Continued in the Next Section]

## API Reference (if applicable)

### Namespace: Syncfusion.Windows.Forms.Tools

#### Member: GradientPanelExt

```csharp
public class GradientPanelExt : Panel
{
    // Properties
    public float CornerRadius { get; set; }
}
```

#### Properties

- **CornerRadius**: Determines the radius of the rounded corners for the panel.

### Parameters

- `CornerRadius`: Type - `float`<br>
  Description: Specifies the radius of the rounded corners. A value of `0` disables rounding.

### Returns

- No return value, as properties directly set the corner radius.

#### Exceptions

- InvalidOperationException if the value is invalid.

## Code Examples

### C#

```csharp
gradientPanelExt1.CornerRadius = 10f;
```

### VB.NET

```vb
gradientPanelExt1.CornerRadius = 10
```

## See also

- [Syncfusion WinForms Documentation](https://www.syncfusion.com/documentation/windowsforms/)
- [GradientPanelExt Control](https://www.syncfusion.com/products/windowsforms/controls/gradientpanel)

<!-- tags: [Syncfusion, Windows Forms, GradientPanelExt, CornerRadius, BorderGap, C#, VB.NET] keywords: [Syncfusion, Windows Forms, GradientPanelExt, CornerRadius, BorderGap, C#, VB.NET] -->
```