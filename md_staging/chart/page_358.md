```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_358.jpeg
document_name: chart
page_number: 358
page_id: chart#page_358
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:20Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains the `Visible` property in the Chart control.
- Demonstrates how to turn the visibility of series on or off using sample code snippets in both C# and VB.NET.

## Content

### 4.5.1.89 Visible

It turns on / off the visibility of the series.

#### Details

| Possible Values                             |                                                                 |
|---------------------------------------------|-----------------------------------------------------------------|
| - True - Unhides the associated series.    |                                                                 |
| - False - Hides the associated series.     |                                                                 |
| Default Value                               | True                                                          |
| 2D / 3D Limitations                        | No                                                             |
| Applies to Chart Element                    | All series                                                    |
| Applies to Chart Types                      | All chart types                                               |

Here is sample code snippet using `Visible` property in Bar Chart.

#### C#

```csharp
// Hides Series[0] and shows Series[1]
this.chartControl1.Series[0].Visible = false;
this.chartControl1.Series[1].Visible = true;
```

#### VB.NET

```vb
' Hides Series[0] and shows Series[1]
Private Me.chartControl1.Series(0).Visible = False
Private Me.chartControl1.Series(1).Visible = True
```

## Footer
© 2013 Syncfusion. All rights reserved.
```