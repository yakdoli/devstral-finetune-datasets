```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_196.jpeg
document_name: diagram
page_number: 196
page_id: diagram#page_196
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:18:31Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### Overview
- Demonstrates the essential diagram functionality for Windows Forms.
- Explains how to set the ZoomType property to 'Center' and 'TopLeft'.
- Includes code examples in C# and VB.NET to adjust the ZoomType.

## Content

### Setting ZoomType to 'Center'

In this section, we show how to set the `ZoomType` to 'center', which will zoom the diagram to the center of the viewport.

#### C#
```csharp
// Sets the ZoomType as 'center'.
this.diagram1.View.ZoomType = ZoomType.Center;
```

#### VB.NET
```vb
'Sets the ZoomType as 'center'.
Me.diagram1.View.ZoomType = ZoomType.Center
```

#### Center-Based Zoom
![Figure 120: Center-Based Zoom](image.png)
*Figure 120: Center-Based Zoom*

### Zooming to the Top-Left of the Diagram

#### Section: 4.6.7.2.3 Zooming to the Top-Left of the Diagram
The diagram document can be zoomed to the top-left corner of the viewport by setting the `ZoomType` as `TopLeft`.

The following code shows how to use the zoom to top-left feature:

#### C#
```csharp
// Sets the ZoomType as TopLeft.
```

### API Reference

#### Namespace: Syncfusion.Windows.Forms.Diagram
- **Class**: Diagram
- **Property**: View
  - **Property**: ZoomType (ZoomType)

#### Enum: ZoomType
- **Members**: Center, TopLeft

### Code Examples

#### Setting Zoom Type to 'TopLeft'

```csharp
// C#
// Sets the ZoomType as TopLeft.
this.diagram1.View.ZoomType = ZoomType.TopLeft;
```

#### Setting Zoom Type to 'TopLeft'

```vb
' VB.NET
'Sets the ZoomType as TopLeft.
Me.diagram1.View.ZoomType = ZoomType.TopLeft
```

### Cross References
See also:
- [Usage of Enhanced Line Routing with Diagram](#enhanced-line-routing-usage)

### Notes
- The `ZoomType` property determines the zoom behavior based on the specified mode.

<!-- tags: [Syncfusion, WinForms, Diagram, ZoomType, Center, TopLeft, C#, VB.NET] keywords: [diagram, zoomtype, center, topleft, enhanced line routing, zoom behavior] -->
```