```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_169.jpeg
document_name: tools
page_number: 169
page_id: tools#page_169
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:08:10Z
fidelity: lossless
-->

## Border for the Docked Control

The border color of the docked controls can be specified in the `BorderColor` property.

### Overview
- explains how to set the border color for docked controls using the `BorderColor` property.
- emphasizes the requirement to enable the `PaintBorders` property to apply the border color setting.
- provides examples in C# and VB.NET for setting the `BorderColor` and `PaintBorders` properties.

### Content

The border color of the docked controls can be specified in the `BorderColor` property.

**Note:** You will have to enable the `PaintBorders` property to effect this setting.

#### DockingManager Property Details

| DockingManager Property | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| BorderColor            | Used to set the border color for the docked control.                       |
| Paint Borders          | Determines whether to paint the docked control's borders.                 |

#### Code Examples

##### C#

```csharp
//Setting Border color
this.dockingManager1.BorderColor = System.Drawing.Color.Blue;
this.DockingManager1.PaintBorders = true;
```

##### VB.NET

```vb
' Setting border color
Me.DockingManager1.BorderColor = System.Drawing.Color.Blue
Me.DockingManager1.PaintBorders = True
```

#### Visual Example

![Docked Window with BorderColor Set](attachment:image.png)

**Figure 82: Docked Window with BorderColor Set**

### Page-level Navigation/TOC (if applicable)
- No local Table of Contents present on this page.
  
### Cross References
- No explicit cross references on this page.

### RAG Annotations
<!-- tags: Windows Forms, DockingManager, BorderColor, PaintBorders, C#, VB.NET keywords: Windows Forms, BorderColor, PaintBorders, DockingManager, C# code, VB.NET code -->
```