```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_171.jpeg
document_name: chart
page_number: 171
page_id: chart#page_171
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:25:26Z
fidelity: lossless
--> 

## Essential Chart for Windows Forms

### Note
To display the text right next to the data points, the `DisplayText` property of the data point's style should be set.

The Chart Series features are elaborated in more detail in the following sub-topics.

### 4.5.1 Series Customization

**Series Customization**

Essential Chart offers numerous appearance and behavior customization capabilities at the series level and on individual points.

Some of these options are applicable only for the whole series while the rest could be applied on the specific data points. Similarly, some of these options are specific to certain chart types.

Note that styles set at the series level automatically propagate to the points in the series.

Interestingly, the Chart control lets the user to edit the styles of a series by double clicking on it during run-time. This feature can be turned on by setting the `AllowUserEditStyles` property to true.

The table below lists the customization options available in ChartSeries and their restrictions.

| Customization Option | Applies to Series or DataPoints* | Applies to Chart Type |
|-----------------------|----------------------------------|------------------------|
| **AngleOffset**      | Series                           | Pie Chart              |
| **Border**           | Series and points                | Pyramid, Funnel, Area, Bar, Bubble, Column Chart, Candle Chart, Renko chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Polar and Radar Chart and Pie Chart. |
| **BubbleType**       | Series                           | Bubble chart.         |
| **ColumnDrawMode**   |                                  | Column Chart, ColumnRange Chart, Bar Chart, |

### Summary
- Essential Chart provides extensive customization options for appearance and behavior.
- Some options apply to the entire series, while others can be applied to individual data points.
- Styles set at the series level propagate to the points in the series automatically.
- Users can edit series styles at runtime if the `AllowUserEditStyles` property is set to true.
- Customization options vary by chart type and are listed in the table provided.

<!-- tags: [syncfusion sdk, winforms, chart, customization, version 11.4.0.26] keywords: [customization options, data points, series styles, series editing, angle offset, border, bubble type, column draw mode] -->
```