```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_510.jpeg
document_name: tools
page_number: 510
page_id: tools#page_510
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:17:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Introduces the essential tools and features for Windows Forms using Syncfusion controls.
- Focuses on customizing the color selection in a `ColorUIControl` with specific groups.

## Content

### Setting Color Groups

The `ColorGroups` property can be used to specify which color groups are displayed in the `ColorUIControl`. The following settings demonstrate how to customize the visible color groups.

#### Image: Properties Window

![](image1.png)

**Figure 296: ColorGroups Property**

This image shows the properties window where the `ColorGroups` property is configured. The options include `CustomColors`, `StandardColors`, `SystemColors`, and `UserColors`.

#### Code Example: C#

```csharp
this.colorUIControl1.ColorGroups =
    (Syncfusion.Windows.Forms.ColorUIGroups)((Syncfusion.Windows.Forms.ColorUIGroups.CustomColors |
                                              Syncfusion.Windows.Forms.ColorUIGroups.StandardColors));
```

#### Code Example: VB.NET

```vb
Me.colorUIControl1.ColorGroups =
    DirectCast(((Syncfusion.Windows.Forms.ColorUIGroups.CustomColors Or
                Syncfusion.Windows.Forms.ColorUIGroups.StandardColors)), Syncfusion.Windows.Forms.ColorUIGroups)
```

#### Image: Color Palette

![](image2.png)

**Figure 297: Color Groups = "CustomColors" and "StandardColor Groups"**

This image illustrates the resulting color palette when both `CustomColors` and `StandardColors` groups are selected.

## API Reference

### Properties

- **ColorGroups**  
  - Type: `Syncfusion.Windows.Forms.ColorUIGroups`
  - Description: Specifies the color groups to be displayed in the `ColorUIControl`.
  - Default: `None`

## Code Examples

### C# Example

```csharp
using Syncfusion.Windows.Forms;

public class Form1 : Form
{
    public Form1()
    {
        ColorUIControl colorUIControl1 = new ColorUIControl();
        colorUIControl1.ColorGroups = (Syncfusion.Windows.Forms.ColorUIGroups)((Syncfusion.Windows.Forms.ColorUIGroups.CustomColors |
                                                                                   Syncfusion.Windows.Forms.ColorUIGroups.StandardColors));
        this.Controls.Add(colorUIControl1);
    }
}
```

### VB.NET Example

```vb
Imports Syncfusion.Windows.Forms

Public Class Form1
    Inherits Form

    Public Sub New()
        Dim colorUIControl1 As New ColorUIControl()
        colorUIControl1.ColorGroups = DirectCast(((Syncfusion.Windows.Forms.ColorUIGroups.CustomColors Or
                                                  Syncfusion.Windows.Forms.ColorUIGroups.StandardColors)), Syncfusion.Windows.Forms.ColorUIGroups)
        Me.Controls.Add(colorUIControl1)
    End Sub
End Class
```

## Cross References

- See also: [ColorUIControl Documentation](#coloruicontrol-documentation)
- [CustomColors and StandardColors Examples](#customcolors-and-standardcolors-examples)

<!-- tags: [Syncfusion Winforms, ColorUIControl, ColorGroups, C#, VB.NET, version: 11.4.0.26] keywords: [WinForms, color selection, custom colors, standard colors, properties, tool, example] -->
```
