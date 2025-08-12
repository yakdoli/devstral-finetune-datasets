```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_404.jpeg
document_name: chart
page_number: 404
page_id: chart#page_404
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:36Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- Illustrates the process of adding custom labels to a chart in Windows Forms using the Syncfusion library.
- Demonstrates using formatted text for axis labels.
- Includes C# and VB.NET code examples for implementing custom labels.

## Content

### Chart with 'Q1 Mid Point' and 'Q2 Mid Point' Custom Labels

#### Figure: Chart with 'Q1 Mid Point' and 'Q2 Mid Point' Custom Labels

![Illustrates Adding Custom Labels](file:///path_to_image)

**Figure 259:** Chart with 'Q1 Mid Point' and 'Q2 Mid Point' Custom Labels

### 2. Using Formatted Text

#### C#

```csharp
// Setting drawing mode
this.chartControl1.PrimaryXAxis.TickLabelsDrawingMode =
    ChartAxisTickLabelDrawingMode.UserMode;

// Adding new labels
this.chartControl1.PrimaryXAxis.Labels.Add(new ChartAxisLabel("",
    Color.Maroon, new Font("Arial", 9F, System.Drawing.FontStyle.Bold),
    new DateTime(2007, 2, 15), "", "M", ChartValueType.DateTime));
this.chartControl1.PrimaryXAxis.Labels.Add(new ChartAxisLabel("",
    Color.Maroon, new Font("Arial", 9F, System.Drawing.FontStyle.Bold),
    new DateTime(2007, 5, 15), "", "M", ChartValueType.DateTime));
```

#### VB.NET

```vb
' Setting drawing mode
Me.chartControl1.PrimaryXAxis.TickLabelsDrawingMode =
    ChartAxisTickLabelDrawingMode.UserMode

' Clearing all the default labels
this.chartControl1.PrimaryXAxis.Labels.Clear()

' Adding new labels
Me.chartControl1.PrimaryXAxis.Labels.Add(New ChartAxisLabel("",
    Color.Maroon, New Font("Arial", 9F, System.Drawing.FontStyle.Bold),
    New DateTime(2007, 2, 15), "", "M", ChartValueType.DateTime))
```

## Copyright

© 2013 Syncfusion. All rights reserved. 404 | Page
```

<!-- tags: [Syncfusion, Windows Forms, Chart Control, Custom Labels, Formatted Text, C#, VB.NET, Axis Labels, DateTime, Font Styling, User Mode Drawing] keywords: [syncfusion, windows forms, chart, custom labels, formatted text, axis labels, date time, font styling, user mode drawing, csharp, vbnet] -->