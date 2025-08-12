```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_541.jpeg
document_name: chart
page_number: 541
page_id: chart#page_541
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:48:27Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Steps to perform the test

### Overview

This section outlines the procedure to perform a t-test for comparing the means of two independent samples with equal variances.

### Content

1. **Specify the null hypothesis and alternate hypothesis.**

   - Null Hypothesis - Difference between the two means is **zero**.
   - Alternate Hypothesis - Difference between the two means is not **zero**.

2. **Calculate the means of the two input series (µ1 and µ2) and calculate their difference (Md).**

   \[
   Md = \mu 1 - \mu 2
   \]

3. **Calculate the variances of the two input series (s1 and s2).**

4. **Let n1 and n2 be the number of data points in the first and second series, respectively.**

5. **Calculate the degrees of freedom.**

   \[
   D = n1 + n2 - 2
   \]

6. **As a next step, Calculate the Pooled Estimator as below.**

   \[
   Sp = (n1 - 1) * s1 + (n2 - 1) * s2
   \]

7. **Calculate the T-statistic as given below.**

   \[
   t = (\mu 1 - \mu 2 - Md) / Sqrt(Sp/n1 + Sp/n2)
   \]

8. **Construct a t-table at (n1+n2-2) degrees of freedom.**

9. **Choose a level of significance (probability), say p = 0.05 and read the tabulated value.**

10. **If the calculated t-value exceeds the tabulated value, we can say that the means are significantly different at that level of probability.**

## Using the Formula

The TTest formula for equal variances can be calculated by using the `TTestEqualVariances` method of the `BasicStatisticalFormulas` class. The following table presents the details of this method. This method returns an instance of `TTestResult` class that stores the resultant values of this test, such as means of the two series, T value, degrees of freedom, number of points in every series, T critical value, and confidence level (probability).

### Method Details

| Method Name            | Parameters                                                  | Return Value                                                |
|-------------------------|-------------------------------------------------------------|--------------------------------------------------------------|
| `TTestEqualVariances` | 1. HypothesizedMeanDifference: A double value specifying the difference between two population means. | A `TTestResult` object that has the following members: |

## API Reference

### `TTestEqualVariances` Method

- **Parameters:**
  - `HypothesizedMeanDifference`: A double value specifying the difference between two population means.
- **Returns:**  
  - A `TTestResult` object containing the following members:
    - Means of the two series.
    - T value.
    - Degrees of freedom.
    - Number of points in every series.
    - T critical value.
    - Confidence level (probability).

## Code Examples

### C# Example

```csharp
// Example usage of TTestEqualVariances method
BasicStatisticalFormulas formulas = new BasicStatisticalFormulas();
TTestResult result = formulas.TTestEqualVariances(series1, series2, 0);
MessageBox.Show("T-Value: " + result.TValue);
```

## Page-level Navigation/TOC

- Steps to perform the test
  - Specify hypotheses
  - Calculate means and differences
  - Calculate degrees of freedom
  - Calculate pooled estimator
  - Compute T-statistic
  - Interpret results using t-table
- Using the Formula
  - Method details and API reference
  - Example code

## RAG Annotations

<!-- tags: [winforms, statistical analysis, t-test, equal variances] keywords: [t-test, mean comparison, degrees of freedom, pooled variance, hypothesis testing, statistical significance, confidence level] -->
```