```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_538.jpeg
document_name: chart
page_number: 538
page_id: chart#page_538
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:50:08Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Implements statistical computations in a Windows Forms application using Syncfusion libraries.
- Focuses on calculating statistical formulas such as Median and Standard Deviation.
- Provides examples and method descriptions for using the BasicStatisticalFormulas class.

---

## Content

### Calculating Median

```vbnet
Imports Syncfusion.Windows.Forms.Chart.Statistics

Dim Median1 As Double
calculatedMedian = BasicStatisticalFormulas.Median(series1)
```

**Note:** For further details, refer to this Browser Sample:

```
[Installed drive]:\Documents and Settings\[User name]\My Documents\Syncfusion\EssentialStudio\[Installed version]\Windows\Chart.Windows\Samples\2.0\Statistical Analysis\Chart Statistical Formulas
```

---

#### 4.12.1.7 Standard Deviation

**StandardDeviation** is the statistical formula that is basically used to measure the variability. That is, it can be used to measure how spread out your data are. It can be defined as the square root of the variance where a variance is the average of the squared differences between the data points and the mean. In other words, it is named as the 'root-mean-square' of the data values.

It can be used to check how tightly the data values are clustered around the mean. If the data points are close to the mean, then the standard deviation will be small; if the points are far from the mean, then the standard deviation is large; or if all the data values are equal, then the standard deviation is zero.

The Standard Deviation can be calculated for any series by using the **StandardDeviation** method of the **BasicStatisticalFormulas** class. Below is the detailed description of this method.

##### Method Description

| **Method Name** | **Parameters** | **Return Value** |
|------------------|----------------|-------------------|
| StandardDeviation | 1. **InputSeries**: A ChartSeries type object for on whose Y values this formula should be applied. <br> 2. **SampleVariance**: true if the data is a sample of a population, false if it is the entire population. | A double that represents the standard deviation within the group of data. |

---

### Example

Here is a code snippet that shows a sample usage.

```vbnet
Imports Syncfusion.Windows.Forms.Chart.Statistics

Dim standardDeviation As Double
standardDeviation = BasicStatisticalFormulas.StandardDeviation(series1, True)
```

---

## Related Information

For more details on other statistical formulas and their implementations, refer to the Browser Sample provided in the documentation.

---

## Tags and Keywords

<!-- tags: [syncfusion, windows forms, statistical formulas, median, standard deviation, basic statistical formulas, chart, windows forms chart] keywords: [calculate, example, reference, sample, statistical analysis, variance, mean, square root] -->
```