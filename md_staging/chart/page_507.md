```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_507.jpeg
document_name: chart
page_number: 507
page_id: chart#page_507
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:44:49Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Provides guidance on managing chart titles using the ChartTitle Collection Editor.
- Explains how to add more titles via code for chart controls.

## Content

### ChartTitle Collection Editor

![ChartTitle Collection Editor](#)
*Figure 325: ChartTitle Collection Editor*

In code, you can add more titles to this list as follows.

#### C#

```csharp
// Default title (the first entry in the Titles list)
chartControl1.Title.Text = "Essential Chart";

// Add the title to the Chart control's Titles collection.
ChartTitle title = new Syncfusion.Windows.Forms.Chart.ChartTitle();
title.Text = "Custom Chart Title";
this.chartControl1.Titles.Add(title);
```

#### VB.NET

```vb
' Default title (the first entry in the Titles list)
chartControl1.Title.Text = "Essential Chart"

' Add the title to the Chart control's Titles collection.
Dim title As New Syncfusion.Windows.Forms.Chart.ChartTitle
title.Text = "Custom Chart Title"
```

### See also:
- Charting API documentation
- Syncfusion.Windows.Forms.Chart namespace

<!-- tags: [chart, windows forms, title, collection editor, SYNCFUSION, winforms] keywords: [charttitle, collection editor, essential chart, syncfusion, windows forms, title, add, code] -->
```