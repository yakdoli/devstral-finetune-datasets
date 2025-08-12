```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_164.jpeg
document_name: chart
page_number: 164
page_id: chart#page_164
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:26:15Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates setting up a Sparkline in VB.NET.
- Explains the use of Sparkline types, specifically the WinLoss type.
- Highlights the support for markers to indicate specific data points in the Sparkline graph.

## Content

### Setting Sparkline Points in VB.NET

#### Code Example
```vb
' Set Sparkline points to source property
Me.sparkLine1.Source = New Double() {30, -20, 80, 20, 40, -50, -30, 70, -40, 50}

' Set line type sparkline
Me.sparkLine1.Type = SparkLine.SparkLineType.WinLoss
```

#### Visual Representation
![](https://i.imgur.com/uTTZZT.png)
**Figure 91: WinLoss SparkLine**

### Marker Support

The markers are visual indicators to represent the location of data points in the Sparkline graph. The markers can support three types of sparklines.

#### Marker Properties Table

| Marker Property | Description |
|-----------------|-------------|
| ShowMarker      | Indicates whether the marker should be displayed at every data point location in line sparkline. By default, it is set to False. |
| ShowHighPoint   | Enables markers to show the highest values in all types of sparklines. By default, it is set to False. |
| ShowLowPoint    | Enables markers to show the lowest values in all types of sparklines. By default, it is set to False. |
| ShowStartPoint  | Enables markers to show start values in all types of sparklines. By default, it is set to False. |
| ShowEndPoint    | Enables markers to show end values in all types of sparklines. By default, it is set to False. |

### API Reference

This section provides a brief overview of the relevant properties and methods used in the Sparkline control.

- **SparkLine.SparkLineType.WinLoss**: A property that sets the type of Sparkline to display win/loss data with alternating colors.

#### Properties
- **ShowMarker**: Boolean property to enable markers at every data point.
- **ShowHighPoint**: Boolean property to indicate the highest values.
- **ShowLowPoint**: Boolean property to indicate the lowest values.
- **ShowStartPoint**: Boolean property to indicate the start values.
- **ShowEndPoint**: Boolean property to indicate the end values.

## Code Examples

### Using ShowMarker Property
```vb
' Enable markers at every data point
Me.sparkLine1.ShowMarker = True
```

### Using ShowHighPoint Property
```vb
' Enable markers to show the highest values
Me.sparkLine1.ShowHighPoint = True
```

### Using ShowLowPoint Property
```vb
' Enable markers to show the lowest values
Me.sparkLine1.ShowLowPoint = True
```

## Page-level Navigation/TOC
- [Setting Sparkline Points in VB.NET](#setting-sparkline-points-in-vb.net)
- [Marker Support](#marker-support)
- [API Reference](#api-reference)

## Cross References
See also:
- [SparkLine Overview](#sparkline-overview)
- [Customizing SparkLine Appearance](#customizing-sparkline-appearance)

<!-- tags: [Syncfusion, WinForms, SparkLine, API, VB.NET, Chart] keywords: [Sparkline, ShowMarker, ShowHighPoint, ShowLowPoint, ShowStartPoint, ShowEndPoint, WinLoss, Chart, Windows Forms, VB.NET] -->
```