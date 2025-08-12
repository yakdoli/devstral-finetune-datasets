```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_272.jpeg
document_name: grid
page_number: 272
page_id: grid#page_272
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:06:46Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes functions related to data analysis in WinForms applications, such as covariance and binomial distribution analysis.

## Content

### Covariance Function
#### Remarks:
- **#N/A** - occurs if arguments have a different number of data points.
#### The covariance is:
\[
Cov(X, Y) = \frac{\sum (x - \bar{x})(y - \bar{y})}{n}
\]
- where \( x \) and \( y \) are the sample means, AVERAGE(array1) and AVERAGE(array2), and \( n \) is the sample size.

### 4.1.4.6.6.49 COVARIANCE.S
#### Description:
The COVARIANCE.S function returns the sample covariance, the average of the products of deviations for each data point pair in two data sets.

#### Syntax:
COVARIANCE.S(array1, array2) where:
- **array1** is the first cell range of integers.
- **array2** is the second cell range of integers.

#### Remarks:
- **#N/A** - occurs when values are different numbers of data points.
- **#DIV/0!** - occurs if either array1 or array2 is empty or contains only one data point each.

### 4.1.4.6.6.50 CRITBINOM
#### Description:
Returns the smallest value for which the cumulative binomial distribution is greater than or equal to a criterion value.

#### Syntax:
CRITBINOM(trials, probability_s, alpha), where:
- **trials** is the number of Bernoulli trials.
- **probability_s** is the probability of a success on each trial.
- **alpha** is the criterion value.

#### Remarks

## References
- These functions are part of the statistical analysis tools in WinForms applications, providing methods for assessing data relationships and distributions.

<!-- tags: [winforms, covariance, critbinom, statistical functions] keywords: [covariance, covariance.s, critbinom, binomial distribution] -->
```