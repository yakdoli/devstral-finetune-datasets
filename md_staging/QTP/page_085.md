```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_085.jpeg
document_name: QTP
page_number: 085
page_id: QTP#page_085
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:07:15Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Demonstrates how to apply the GetXAxisText and GetYAxisText methods in QTP.
- Explains how to find the count of a series within a chart.
- Details the process to find the maximum Y-axis value in the specified region.

## Content

### Applying GetXAxisText and GetYAxisText Method in QTP

The following code examples illustrate how to get the displayed text.

```plaintext
MsgBox(SwfWindow("ChartDemo").SwfObject("chart1").GetXAxisText())
MsgBox(SwfWindow("ChartDemo").SwfObject("chart1").GetYAxisText())
```

#### 7.4.2 How to find the count of a series within the chart

##### Supported method to find the series count within the chart
The GetSeriesCount method is used to get the series count within the chart. This method returns the displayed text in integer format.

##### Use Case Scenarios
This feature enables you to get the count of a series within the chart in QTP testing.

##### Methods Table

| Method         | Description                   | Parameters                                        | Return Type |
|----------------|-------------------------------|---------------------------------------------------|-------------|
| GetSeriesCount | Gets the series count within the chart in Essential Chart. | public in GetSeriesCount() | Int         |

##### Applying GetSeriesCount in QTP
The following code example illustrates how to get the series count in the chart.

```plaintext
[For Chart Control]
MsgBox(SwfWindow("ChartDemo").SwfObject("chart1").GetSeriesCount())
```

#### 7.4.3 How to find the maximum Y-axis value in the specified region

##### Supported method to find the maximum Y-axis value in the specified region
The GetMaxYValue method is used to get the displayed maximum value in the Y-axis. This method returns the displayed value in double format.

---

<!-- tags: [product, module, control, api, version?] keywords: [GetXAxisText, GetYAxisText, GetSeriesCount, GetMaxYValue, QTP, chart, series count, maximum Y-axis value, WinForms] -->
```