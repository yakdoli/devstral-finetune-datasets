```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_167.jpeg
document_name: tools
page_number: 167
page_id: tools#page_167
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:06:44Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

This section will discuss the background settings for the caption area of the docked controls.

## Overview
- Discusses the background settings for the caption area of docked controls.
- Focuses on the ActiveCaptionBackground and InactiveCaptionBackground properties.
- Provides examples in C# and VB.NET for setting the ActiveCaptionBackground.

## Content

### 3.4.3.5.2.1 Active and Inactive caption

#### Active Caption Settings

Caption background appearance for the active docked control can be controlled through the ActiveCaptionBackground property.

| DockingManager Property           | Description                                                                                                   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------|
| ActiveCaptionBackground           | Sets background for the caption area using a BrushInfo object.                                             |

**Note:** This setting will effect only with DockingManager.VisualStyle property set as Default.

#### Code Examples

##### [C#]

```csharp
this.dockingManager1.ActiveCaptionBackground = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.PatternStyle.Percent20, System.Drawing.SystemColors.InactiveCaptionText, System.Drawing.Color.FromArgb(((System.Byte)(255)), ((System.Byte)(224)), ((System.Byte)(192))));;
```

##### [VB.NET]

```vb
Me.DockingManager1.ActiveCaptionBackground = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.PatternStyle.Percent20, System.Drawing.SystemColors.InactiveCaptionText, System.Drawing.Color.FromArgb(CType(255, Byte), CType(224, Byte), CType(192, Byte)))
```

<!-- tags: [Syncfusion, WinForms, ActiveCaptionBackground, InactiveCaptionBackground, DockingManager, Brushes, Color, C#, VB.NET, version:11.4.0.26] keywords: [DockingManager, ActiveCaptionBackground, InactiveCaptionBackground, Brushes, Color, C#, VB.NET, Syncfusion.Drawing.BrushInfo, System.Drawing.SystemColors, System.Drawing.Color] -->
```