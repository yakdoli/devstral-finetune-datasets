```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_165.jpeg
document_name: chart
page_number: 165
page_id: chart#page_165
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:25:40Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Includes properties related to marker display and styling in sparklines.
- Describes enabling and customizing markers for sparkline data points.

## Content

### Sparkline Marker Properties

| Property                    | Description                                                                                                                                                                                                 |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ShowNegativePoint            | Enables markers to show negative values in all types of sparklines. By default, it is set to `False`.                                                                                                       |
| MarkerColor                  | Gets or sets the marker color for line type sparkline. This property color is set to sparkline marker when enabling the `ShowMarker` property.                                                           |
| HighPointColor               | Gets or sets the high point color for line type sparkline. This property color is set to sparkline marker when enabling the `ShowHighPoint` property.                                                    |
| LowPointColor                | Gets or sets the low point color to line type sparkline. This property color is set to sparkline marker when enabling the `ShowLowPoint` property.                                                        |
| StartPointColor              | Gets or sets the start point color for line type sparkline. This property color is set to sparkline marker when enabling the `ShowStartPoint` property.                                                   |
| EndPointColor                | Gets or sets the end point color to line type sparkline. This property color is set to sparkline marker when enabling the `ShowEndPoint` property.                                                          |
| NegativePointColor           | Gets or sets the negative point color to line type sparkline. This property color is set to sparkline marker when enabling the `ShowNegativePoint` property.                                                |

### Markers Support for Line

#### Overview
The marker feature supports data points of line sparkline. You can choose the marker color for data points.

#### Code Snippets for Enabling Markers in Line Sparkline

- **[C#.NET]**
  ```csharp
  // To enable marker to sparkline for all data points
  this.sparkLine1.Markers.ShowMarker = true;
  ```

- **[VB.NET]**
  ```vb
  ' To enable marker to sparkline for all data points
  Me.sparkLine1.Markers.ShowMarker = True
  ```

### Cross References
- Refer to documentation on enabling other properties related to sparklines for additional configurations.

<!-- tags: [Syncfusion, Winforms, Sparkline, Markers, Properties, C#, VB] keywords: [ShowNegativePoint, MarkerColor, HighPointColor, LowPointColor, StartPointColor, EndPointColor, NegativePointColor, ShowMarker] -->
```