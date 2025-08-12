```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_369.jpeg
document_name: chart
page_number: 369
page_id: chart#page_369
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:37:28Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the use of "OrangeRed InvertedTriangle" symbols in the series points.
- Explains the concept of Custom Points in Essential Chart.
- Details the properties and methods to customize the appearance and formatting of Custom Points.

## Content
### Figure 237: "OrangeRed InvertedTriangle" Symbols in the Series Points
![Figure 237: "OrangeRed InvertedTriangle" Symbols in the Series Points](https://chart_data_point_symbols.png)

#### 4.5.3 Custom Points
Essential Chart supports plotting of points on the Chart Area even if they don't belong to a series. These are stored in the `ChartControl.CustomPoints` collection. They can be set at custom coordinates of the Chart Area or be made to follow a certain point or percentage coordinates. A custom point displays a text, background, border, symbol and marker, which is a line that connects the CustomPoint with the point on the chart area when it is offset from it.

**Through Designer, the Custom Points can be set using the CustomPoints property. Clicking this property will popup ChartCustomPoint Collection Editor window where you can add your custom points.**

You can set the co-ordinates (XValue and the YValue property), symbols and their customization, using the Symbols property, text, using the Text property, alignment of the text, using the Alignment property and so on.
```