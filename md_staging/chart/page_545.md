```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_545.jpeg
document_name: chart
page_number: 545
page_id: chart#page_545
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:48:50Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Provides a step-by-step guide on calculating and interpreting the t-statistic for dependent samples.
- Explains how to use the `TTestPaired` method in the `BasicStatisticalFormulas` class for statistical analysis.
- Outlines the procedure for determining whether the means of two series are significantly different.

## Content

1. **Calculate the difference between two series on each pair of values.**
   - Calculate the mean difference (\( Mdiff \)), i.e., the mean of the new series values.
2. **Calculate the Standard Deviation of the differences (\( Sd \)).**
3. **Get the degrees of freedom.**
   - \[ df = n_1 - 1 \]
4. **Compute the t-statistic as given below.**
   - \[ t = (Mdiff - Md) / [Sd * Sqrt(1/n1)] \]
5. **Construct a t-table at \((n1 - 1)\) degrees of freedom and get the tabulated value for a given level of significance (probability).**
6. **If the calculated t-value exceeds the tabulated value, we can say that the means are significantly different at that level of probability.**

### Using the Formula

- The TTest formula for dependent samples can be calculated by using the `TTestPaired` method of the `BasicStatisticalFormulas` class.
- The following table presents the details of this method:

#### Method Name: TTestPaired

| Parameters                     | Description                                                                        |
|---------------------------------|------------------------------------------------------------------------------------|
| 1. HypothesizedMeanDifference  | A double value specifying the difference between two population means.           |
| 2. Probability                  | A double value that denotes the probability that gives the confidence level.    |
| 3. FirstSeries                   | A `ChartSeries` object that stores the first group of data.                     |
| 4. SecondSeries                  | A `ChartSeries` object that stores the second group of data.                    |

**Return Value:**  
- A `TTestResult` object that has the following members:  
  - FirstSeriesMean  
  - SecondSeriesMean  
  - FirstSeriesVariance  
  - SecondSeriesVariance  
  - Tvalue  
  - DegreeOfFreedom  

## API Reference

### Method: TTestPaired

- **Namespace:** BasicStatisticalFormulas
- **Parameters:**
  - Name | Type | Description
  - --- | --- | ---
  - HypothesizedMeanDifference | double | Specifies the difference between two population means.
  - Probability | double | Denotes the probability that gives the confidence level.
  - FirstSeries | ChartSeries | Stores the first group of data.
  - SecondSeries | ChartSeries | Stores the second group of data.

- **Returns:**  
  - `TTestResult` object containing:  
    - FirstSeriesMean  
    - SecondSeriesMean  
    - FirstSeriesVariance  
    - SecondSeriesVariance  
    - Tvalue  
    - DegreeOfFreedom  

## Code Examples

### C#
```csharp
using Syncfusion.Chart;

// Example usage of TTestPaired method
double hypothesizedMeanDifference = 0.0;
double probability = 0.95;

ChartSeries firstSeries = new ChartSeries();
ChartSeries secondSeries = new ChartSeries();

// Populate the series with data...

BasicStatisticalFormulas ttestFormulas = new BasicStatisticalFormulas();
TTestResult result = ttestFormulas.TTestPaired(hypothesizedMeanDifference, probability, firstSeries, secondSeries);

// Access the results
double tValue = result.Tvalue;
int degreeOfFreedom = result.DegreeOfFreedom;
```

## Cross References

- **See also:** 
  - BasicStatisticalFormulas class
  - TTestResult class
  - ChartSeries

<!-- tags: [TTestPaired, ChartSeries, TTestResult, BasicStatisticalFormulas, Probability, DegreesOfFreedom, TValue] keywords: [t-test, dependent samples, statistical analysis, C# examples, Syncfusion WinForms] -->
```