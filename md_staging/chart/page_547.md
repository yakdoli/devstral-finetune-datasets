```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_547.jpeg
document_name: chart
page_number: 547
page_id: chart#page_547
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:47:23Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Variance Method

### Method Information

| Method Name  | Parameters                                                                                               | Return Value                             |
|--------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------|
| **Variance** | 1. **InputSeries**: A `ChartSeries` object that represents the input series.<br>2. **SampleVariance**: A boolean value; `<br>true` if the data is a sample of a population, `false` if it is the entire population. | A `double` that represents the variance within the group of data. |

### Example

Variance is the square of the standard deviation for the given data.

#### C#

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;

double Variance1 = BasicStatisticalFormulas.Variance(series1, false);
```

#### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics

Dim Variance1 As Double
Variance1 = BasicStatisticalFormulas.Variance(series1, false)
```

## 4.12.1.10 Z-Test

### Overview

- **Z-test**: A statistical formula used to determine if the difference between a sample mean and the population mean is large enough to be statistically significant. This test is primarily used to determine if the test scores of the samples are either within or outside the standard scores.

### Steps to perform ZTest

This test requires the sample to be random and is taken from a population that is distributed normally. In order to perform this test, the following quantities should be known:

- **s**: The standard deviation of the population
- **μ**: The mean of the population
- **x**: The mean of the sample
- **n**: The size of the sample

## Related Information

See also:
- BasicStatisticalFormulas
- ChartSeries
- SampleVariance
- Variance

<!-- tags: [Syncfusion, Chart, Variance, Z-Test, Windows Forms] keywords: [chart, variance, z-test, windows forms, statistical analysis, sample variance, population mean, sample mean, standard deviation] -->
```