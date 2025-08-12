```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_374.jpeg
document_name: chart
page_number: 374
page_id: chart#page_374
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:19Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- Demonstrates how to create custom points with multiple axes using `ChartCustomPointType.ChartCoordinates`.
- Assigns series index for ChartCoordinates to achieve custom points on the Secondary axis.
- Provides code examples in both C# and VB for configuring and adding custom points.

## Content

### 4.5.3.1 Custom Point in Multiple Axes

The custom points for the Secondary axis can be achieved by assigning the Series Index for the `ChartCoordinates` type. The following code snippet illustrates this:

#### C# Code Example

```csharp
ChartCustomPoint cp = new ChartCustomPoint();
cp.CustomType = ChartCustomPointType.ChartCoordinates;
// Set the series index if the Customtype is ChartCoordinates in multiple axis
cp.SeriesIndex = 0;
cp.XValue = 10;
cp.YValue = 60;
cp.Symbol.Shape = ChartSymbolShape.Circle;
cp.Alignment = ChartTextOrientation.Left;
cp.Color = Color.Black;
cp.Font.Facename = "Verdana";
cp.Font.Size = 8.0F;
cp.Symbol.Color = Color.Yellow;
cp.Text = cp.XValue + "," + cp.YValue;
this.ChartWebControl1.CustomPoints.Add(cp);
```

#### VB Code Example

```vb
Dim cp As ChartCustomPoint = New ChartCustomPoint()
cp.CustomType = ChartCustomPointType.ChartCoordinates
' Set the series index if the Customtype is ChartCoordinates in multiple axis
cp.SeriesIndex = 0
cp.XValue = 10
cp.YValue = 60
cp.Symbol.Shape = ChartSymbolShape.Circle
cp.Alignment = ChartTextOrientation.Left
cp.Color = Color.Black
cp.Font.Facename = "Verdana"
cp.Font.Size = 8.0F
cp.Symbol.Color = Color.Yellow
cp.Text = cp.XValue & "," & cp.YValue
Me.ChartWebControl1.CustomPoints.Add(cp)
```

## API Reference

- **Namespace:** `Syncfusion.Windows.Forms.Chart`
- **Class:** `ChartCustomPoint`
- **Properties:**
  - `CustomType`: Specifies the type of custom point.
  - `SeriesIndex`: Index of the series for which the custom point is defined.
  - `XValue`: X-coordinate value of the custom point.
  - `YValue`: Y-coordinate value of the custom point.
  - `Symbol.Shape`: Shape of the symbol for the custom point.
  - `Alignment`: Alignment of the text associated with the custom point.
  - `Color`: Color of the custom point.
  - `Font`: Font properties for the text associated with the custom point.
  - `Symbol.Color`: Color of the symbol.
  - `Text`: Text displayed at the custom point.

## Code Examples (multi-language supported)
- Provided in both C# and VB.NET for configuring and adding custom points with multiple axes.

## Page-level Navigation/TOC (if applicable)
- **Section:** 4.5.3.1 Custom Point in Multiple Axes
- **Heading:** Demonstrates setting custom points for secondary axes using `ChartCoordinates`.

## Cross References
- See also:
  - [General Chart Concepts](#general-chart-concepts)
  - [Customizing Chart Elements](#customizing-chart-elements)

<!-- tags: [chart, custom points, multiple axes, windows forms, secondary axis, chart-web-control] keywords: [ChartCustomPoint, SeriesIndex, ChartCoordinates, XValue, YValue, ChartSymbolShape, ChartTextOrientation, Color, Font, Symbol, Text] -->
```