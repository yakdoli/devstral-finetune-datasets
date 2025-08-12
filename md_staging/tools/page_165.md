```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_165.jpeg
document_name: tools
page_number: 165
page_id: tools#page_165
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:05:39Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- Configures the font and color of the inactive caption in a DockingManager.
- Demonstrates how to set these properties in both C# and VB.NET.
- Emphasizes that these settings are effective only when DockingManager.VisualStyle is set to Default.

### Content

#### DockingManager Property Table

| DockingManager Property                  | Description                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------|
| InactiveCaptionFont                      | Gets or sets the font of the inactive caption.                          |
| InactiveCaptionForeGround                | Indicates the color of the caption text in inactive state.             |

#### Note
- These settings will effect only with DockingManager.VisualStyle property set as Default.

#### Code Examples

**[C#]**

```csharp
this.dockingManager1.InActiveCaptionFont = new
System.Drawing.Font("Arial", 11.25F, System.Drawing.FontStyle.Bold,
System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));

this.dockingManager1.InActiveCaptionForeGround = 
System.Drawing.Color.Blue;
```

**[VB.NET]**

```vb
Me.DockingManager1.InActiveCaptionFont = New
System.Drawing.Font("Arial", 11.25!, System.Drawing.FontStyle.Bold,
System.Drawing.GraphicsUnit.Point, CType(0, Byte))

Me.DockingManager1.InActiveCaptionForeGround =
System.Drawing.Color.MediumSlateBlue
```

### Figure: Docked Window with Inactive Captions

![Docked Window with Inactive Captions](https://i.imgur.com/UjYx34f.png)

**Figure 80: Docked Window with Inactive Captions**

<!-- tags: [DockingManager, InactiveCaption, WindowsForms, C#, VB.NET, Font, Color] keywords: [DockingManager property, InactiveCaptionFont, InactiveCaptionForeGround, VisualStyle, Default, Windows Forms, C# code, VB.NET code] -->
```