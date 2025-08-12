```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_537.jpeg
document_name: chart
page_number: 537
page_id: chart#page_537
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:48:14Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```vb
Dim calculatedMean As Double
calculatedMean = BasicStatisticalFormulas.Mean(series1)
```

**Note:** For further details, refer to this Browser Sample:  
[Installed drive]:\\Documents and Settings\[User name]\\My Documents\\Syncfusion\\EssentialStudio\\Installed version]\\Windows\\Chart.Windows\\Samples\\2.0\\Statistical Analysis\\Chart Statistical Formulas

## 4.12.1.6 Median

**Median** is a statistical formula that is used to find the median of *y* values of a series. Median can be calculated by arranging the values from the lowest to the highest and picking up the middle one. If the total number of values is even, then pick up the two middle values after sorting the values in ascending order. The mean of these two middle values will give you the median. Hence half of the series points have values less than the median and the values of the other half will be greater than the median.

Median can be found out for any series by using the **Median** method of **BasicStatisticalFormulas** class. The below table shows the details of this method.

| **Method Name**    | **Parameter**                            | **Return value**                       |
|--------------------|------------------------------------------|----------------------------------------|
| Median             | InputSeries: A ChartSeries type object for whose *X* values an average is required. | A double that represents the Median value of all the *X* values in the given series. |

### Example

Here is a code snippet that shows a sample usage.

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
double calculatedMedian = Statistics.BasicStatisticalFormulas.Median(series1);
```

<!-- tags: [Syncfusion, Winforms, Chart, Median, Statistical Formulas] keywords: [Essential Chart, Windows Forms, Statistical Analysis, Median, BasicStatisticalFormulas, ChartSeries, languages] -->
```