```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_543.jpeg
document_name: chart
page_number: 543
page_id: chart#page_543
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:47:07Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Null Hypothesis: The difference between the two means is zero.
- Alternate Hypothesis: The difference between the two means is not zero.

## Content

### Statistical Testing Procedure

1. **Calculate the means of the two input series** (\(\mu 1\) and \(\mu 2\)) and calculate their difference (\(Md\)).
   \[
   Md = \mu 1 - \mu 2
   \]
2. **Calculate the variances of the two input series** (\(s1\) and \(s2\)).
3. **Let \(n1\) and \(n2\) be the number of data points in the first and second series respectively.**
4. **Calculate the degrees of freedom**:
   \[
   df = \frac{\left(\frac{s_1}{n_1} + \frac{s_2}{n_2}\right)^2}{\frac{(s_1 / n_1)^2}{n_1 - 1} + \frac{(s_2 / n_2)^2}{n_2 - 1}}
   \]
5. **Calculate the T-statistic** as given below:
   \[
   t = (\mu 1 - \mu 2 - Md) / Sqrt(s1/n1 + s2/n2)
   \]
6. **Choose a level of significance (probability)**, say \(p = 0.05\) and read the tabulated value.
7. **If the calculated t-value exceeds the tabulated value**, we can say that the means are significantly different at that level of probability.

### Using the Formula

The TTest formula for unequal variances can be calculated by using the **TTestUnEqualVariances** method of the **BasicStatisticalFormulas** class. The following table presents the details of this method. This method returns an instance of **TTestResult** class that stores the resultant values of this test such as means of the two series, T value, degrees of freedom, number of points in every series, T critical value, and confidence level (probability).

#### Method Details

| Method Name                   | Parameters                                                                 | Return Value                                                                             |
| ----------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| TTestUnEqualVariances        | 1. HypothesizedMeanDifference: A double value that gives the difference between the means | A TTestResult object that has the following members:<br>- FirstSeriesMean |

<!-- tags: [chart, statistical testing, t-test, unequal variances] keywords: [winforms, statistic, means, variances, t-statistic, degrees of freedom, significance level, t-value, confidence level] -->
```