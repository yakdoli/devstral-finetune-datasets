```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_536.jpeg
document_name: chart
page_number: 536
page_id: chart#page_536
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:48:00Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

```csharp
t(confidenceLevel, series1, series2);
```

```vb
[VB.NET]

Dim ttr As FTestResult =
Syncfusion.Windows.Forms.Chart.Statistics.BasicStatisticalFormulas.FTest(confidenceLevel, series1, series2)
```

> **Note:** For further details, refer to this Browser Sample:

```
[Installed drive]:\Documents and Settings\[User name]\My
Documents\Syncfusion\EssentialStudio\Installed
version]\Windows\Chart.Windows\Samples\2.0\Statistical Analysis\Chart Statistical
Formulas
```

### 4.12.1.5 Mean

**Mean is statistical formula that returns the arithmetic average of series y values where the arithmetic average is the sum of all y values of a series divided by the total number of y values present in that series.** The arithmetic mean can be calculated for any chart series by using **Mean** method of the **BasicStatisticalFormulas** class. Below table shows the method details.

| Method Name    | Parameter                     | Return value                          |
|----------------|-------------------------------|----------------------------------------|
| Mean           | `InputSeries`: A ChartSeries type<br> object for whose y values an<br> average is required. | A `double` that represents the average<br> of all the y values in the given series. |

#### Example

Here is a code snippet that shows a sample usage.

```csharp
[C#]

using Syncfusion.Windows.Forms.Chart.Statistics;
...
double calculatedMean = BasicStatisticalFormulas.Mean(series1);
```

```vb
[VB.NET]

Imports Syncfusion.Windows.Forms.Chart.Statistics
```
```