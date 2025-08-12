```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_162.jpeg
document_name: tools
page_number: 162
page_id: tools#page_162
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:03:17Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Setting the Auto Hide tab Font style in Windows Forms.
- Configuring the DockingManager's VisualStyle property to Default.
- Demonstrating code examples in both C# and VB.NET for setting the AutoHideTabFont property.

## Content

### Auto Hide Tab Font Style

#### Note: This setting will effect only with DockingManager.VisualStyle property set as Default.

```csharp
// [C#]
// Setting Auto hide tab Font style
this.dockingManager1.AutoHideTabFont = new System.Drawing.Font("Arial", 9.75F, 
    (System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic | 
    System.Drawing.FontStyle.Underline)), System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));
```

```vbnet
' [VB.NET]
' Setting Auto hide tab Font style
Me.DockingManager1.AutoHideTabFont = New System.Drawing.Font("Arial", 9.75!, CType(
    ((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic) _
    Or System.Drawing.FontStyle.Underline), System.Drawing.FontStyle), 
    System.Drawing.GraphicsUnit.Point, CType(0, Byte))
```

#### Figure 77: Docked Window with AutoHideTabFont Set
![Docked Window with AutoHideTabFont Set](image.png)

The height for the auto hidden tabs can be specified in the `AutoHideTabHeight` property.

| DockingManager Property       | Description                                      |
|-------------------------------|--------------------------------------------------|
| AutoHideTabHeight             | Gets or sets the height of the autohide tab control. |

## API Reference

- **AutoHideTabHeight**: 
  - **Type**: Property
  - **Description**: Gets or sets the height of the autohide tab control.

## Code Examples

The provided code examples illustrate how to set the `AutoHideTabFont` property in both C# and VB.NET for customizing the appearance of auto-hide tabs in a DockingManager control.

## Page-level Navigation/TOC
- [Setting AutoHideTabFont]
- [AutoHideTabHeight Property]
  
## Cross References

- See also: [DockingManager Documentation](URL)
- Related topics: [Visual Styles in Windows Forms](URL)

<!-- tags: [Syncfusion, WinForms, DockingManager, AutoHideTabFont, AutoHideTabHeight, C#, VB.NET, VisualStyle] keywords: [AutoHideTabFont, AutoHideTabHeight, DockingManager, Windows Forms, C#, VB.NET, Visual Style] -->
```