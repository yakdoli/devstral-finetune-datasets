```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_532.jpeg
document_name: chart
page_number: 532
page_id: chart#page_532
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:47:41Z
fidelity: lossless
-->

### Essential Chart for Windows Forms

#### Overview
- Explains the concept of correlation between two variables.
- Describes positive and negative correlations.
- Provides the formula for calculating the correlation coefficient.
- Details the use of the `Correlation` method in the BasicStatisticalFormulas class to calculate correlation.

---

## Content

### Understanding Correlation

A relationship generally refers to the correspondence between two variables. For instance, consider two variables representing 'Work Experience' and 'Salary Expectation'. If the 'Work Experience' is high, the 'Salary Expectation' will also be high. Similarly, if 'Work Experience' is low, the 'Salary Expectation' tends to be low. These two variables are thus correlated.

The relationships can be classified into two types: **Positive** and **Negative**.
- In a **positive** relationship, high values on one variable are associated with high values on the other, and low values on one variable are associated with low values on the other.
- In a **negative** relationship, high values on one variable are associated with low values on the other.

When the measured correlation coefficient is positive, the series values would be positively correlated. Conversely, if the correlation coefficient is negative, the series values would be negatively correlated.

### Formula for Calculating Correlation Coefficient

The formula for calculating the correlation coefficient is:

\[
r = \frac{N \Sigma x y - (\Sigma x)(\Sigma y)}
{\sqrt{\left[ N \Sigma x^2 - (\Sigma x)^2 \right] \left[ N \Sigma y^2 - (\Sigma y)^2 \right]}}
\]

Where:
- \( x \) is the y value of the first series.
- \( y \) is the y value of the second series.

### Using the Formula

The Correlation Coefficient can easily be calculated using the Correlation method available with the BasicStatisticalFormulas class. The following table describes the details of this method. This method returns the covariance of the datasets divided by the product of their standard deviations.

---

## API Reference

### Correlation Method

| Method Name           | Parameters                                               | Return Value                                                                 |
|-----------------------|----------------------------------------------------------|------------------------------------------------------------------------------|
| Correlation            | 1. FirstInputSeries: A ChartSeries object that stores the first group's data.<br>2. SecondInputSeries: A ChartSeries object that stores the second group's data. An exception will be raised if the input series does not have the same number of data points. | A double that represents the correlation value between the two groups of data. The value always ranges from -1 to 1. |

---

## Code Examples

The document does not provide explicit code examples. However, the method `Correlation` from the BasicStatisticalFormulas class can be used to calculate the correlation coefficient between two sets of data points.

## Page-level Navigation/TOC
- Correlation Coefficient Introduction
- Types of Correlation Relationships
- Correlation Coefficient Formula
- Correlation Method in BasicStatisticalFormulas Class

## Cross References
- See also: Correlation Coefficient Calculation, BasicStatisticalFormulas Class, ChartSeries

---

<!-- tags: [syncfusion, windows forms, correlation coefficient, statistical formulas, winforms] keywords: [correlation, variable relationship, correlation coefficient, positive correlation, negative correlation, formula, correlation method, basic statistical formulas, chart series] -->
```