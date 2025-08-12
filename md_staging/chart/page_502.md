```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_502.jpeg
document_name: chart
page_number: 502
page_id: chart#page_502
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:48:08Z
fidelity: lossless
-->

## 4.10.4 Foreground Settings

### Chart Title

The ChartControl provides properties to customize and align the text within the control. Below are the text properties.

Using the ChartControl.Text property, users can provide the title that appears at the top of the chart. TextPosition and TextAlignment further lets you control the relative positioning of this title.

Here are some properties that affect the title text in the chart.

| Chart control Property   | Description                                                                 |
|--------------------------|------------------------------------------------------------------------------|
| Text                     | Specifies the title for the chart.                                        |
| TextPosition             | Specifies the position of the chart. Possible values are,                 |
|                          | • Top (default setting)                                                    |
|                          | • Bottom                                                                   |
|                          | • Left                                                                     |
|                          | • Right                                                                    |
| TextAlignment            | Specifies the alignment of the title with respect to the chart borders. Possible values: |
|                          | • Near                                                                     |
|                          | • Center (default setting)                                                 |
|                          | • Far                                                                      |
| Font                     | Indicates the font style of the title.                                    |
| ForeColor                | Indicates the foreground color of the title.                              |

### Code Example

```csharp
this.chartControl1.Text = "Illustrates Foreground Settings";
```
```