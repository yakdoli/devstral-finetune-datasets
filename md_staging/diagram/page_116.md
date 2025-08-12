```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_116.jpeg
document_name: diagram
page_number: 116
page_id: diagram#page_116
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:13:57Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Modifies the appearance of connectors (Orthogonal, Org line, Polyline) by adding rounded corners.
- Uses `EnableRoundedCorner` to enable rounded corners and `CurveRadius` to set the radius for the rounded corner curve.
- Useful for customizing the visual style of connectors.

## Content

### 4.3.1 Rounded Corner

You can now change the look of connectors (Orthogonal, Org line, Polyline) by providing rounded corners to connectors.

The `EnableRoundedCorner` is used to enable rounded corner for a connector, and the `CurveRadius` connector property is used and set the radius for the rounded corner curve respectively.

#### Use Case Scenario

This is used to change the visual style of connectors.

#### Properties

| Property                | Description                                                 | Data Type |
|-------------------------|-------------------------------------------------------------|-----------|
| EnableRoundedCorner     | Enables or disables rounded corner for a connector.         | bool      |
| CurveRadius             | Gets or sets the radius for the rounded corner curve of a connector. | float     |

The following code illustrates how to change the look of a connector by using the `EnableRoundedCorner` and `CurveRadius` properties.

```csharp
[C#]
OrthogonalConnector orthogonal = new OrthogonalConnector(new PointF(100, 100), new PointF(300, 300));
// Enables rounded corner for the connector.
orthogonal.EnableRoundedCorner = true;
// Sets the radius of the rounded corner curve.
orthogonal.CurveRadius = 10;
diagram1.Model.AppendChild(orthogonal);
```

```vb
[VB]
Dim orthogonal As New OrthogonalConnector(New PointF(100, 100), New Point(300, 300))
'Enables rounded corner for the connector.
orthogonal.EnableRoundedCorner = True
'Sets the radius of the rounded corner curve.
orthogonal.CurveRadius = 10
diagram1.Model.AppendChild(orthogonal)
```

## Page-level Navigation/TOC (if applicable)

- 4.3.1 Rounded Corner

### WinForms-specific conventions
- Uses `OrthogonalConnector` class to illustrate the addition of rounded corners.
- Demonstrates use of `EnableRoundedCorner` and `CurveRadius` properties to modify the appearance of connectors.

<!-- tags: [Syncfusion Winforms, Diagram, Connector, Rounded Corner, OrthogonalConnector, EnableRoundedCorner, CurveRadius] keywords: [rounded corners, visual style, OrthogonalConnector, EnableRoundedCorner, CurveRadius] -->
```