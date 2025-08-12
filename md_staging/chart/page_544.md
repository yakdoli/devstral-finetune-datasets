```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_544.jpeg
document_name: chart
page_number: 544
page_id: chart#page_544
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:48:26Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Lists parameters for statistical test computation.
- Details on Confidence Level, Probability, and data series objects.
- Example usage in C# and VB.NET.
- Explanation of TTest Paired and its application in dependent samples.

## Content

The table below lists the parameters and results associated with the statistical test computation:

| Parameters | Results |
|-----------|---------|
| 1. FirstSeries: A ChartSeries object that stores the first group<br>of the two input series. | • SecondSeriesMean |
| 2. Probability: A double value<br>that denotes the probability that<br>gives the confidence level. | • FirstSeriesVariance |
| 3. FirstSeries: A ChartSeries<br>object that stores the first group<br>of data. | • SecondSeriesVariance |
| 4. SecondSeries: A<br>ChartSeries object that stores<br>the second group of data. | • Tvalue |
|           | • DegreeOfFreedom |
|           | • ProbabilityTOneTail |
|           | • TCriticalValueOneTail |
|           | • ProbabilityTTwoTail |
|           | • TCriticalValueTwoTail |

### Example

Here is a code snippet that shows a sample usage.

#### Example in C#
```csharp
TTestResult ttr = BasicStatisticalFormulas.TTestUnEqualVariances(0.2, 0.05, series1, series2);
```

#### Example in VB.NET
```vb
Dim ttr As TTestResult = BasicStatisticalFormulas.TTestUnEqualVariances(0.2, 0.05, series1, series2)
```

### 4.12.1.8.3 TTest Paired

This formula is used when there is a dependency between the samples. The two possible scenarios could be when there is a single sample that is tested twice (before and after an experiment), or when there are two samples whose values can be matched. This test assumes that there is some difference between the means of two input series populations. Input series are regarded as samples from normally distributed populations. The population variances are assumed to be unequal. This test is otherwise called as **Robust TTest**.

#### Steps to perform the test

1. Specify the null hypothesis and alternate hypothesis.
   - Null Hypothesis: Difference between the two means is zero.
   - Alternate Hypothesis: Difference between the two means is not zero.

--- 
© 2013 Syncfusion. All rights reserved.
```

## API Reference (if applicable)

### Methods
- **TTestUnEqualVariances**
  - Parameters:
    - TestPurpose: Defines the purpose of the test.
    - Probability: A double value denoting the probability.
    - FirstSeries: A ChartSeries object representing the first group of data.
    - SecondSeries: A ChartSeries object representing the second group of data.

## Code Examples (multi-language supported)

### C#
```csharp
TTestResult ttr = BasicStatisticalFormulas.TTestUnEqualVariances(0.2, 0.05, series1, series2);
```

### VB.NET
```vb
Dim ttr As TTestResult = BasicStatisticalFormulas.TTestUnEqualVariances(0.2, 0.05, series1, series2)
```

## Page-level Navigation/TOC (if applicable)

- Essential Chart for Windows Forms
  - Example
  - 4.12.1.8.3 TTest Paired

## Cross References

- **See also:**
  - Related documentation on statistical tests.
  - Details on handling dependent samples in experiments.

## RAG Annotations

<!-- tags: [syncfusion, winforms, chart, statistical test, ttest, paired test, robust ttest] keywords: [confidence level, probability, chartseries, dependent samples, normally distributed populations, unequal variances, null hypothesis, alternate hypothesis] -->
```