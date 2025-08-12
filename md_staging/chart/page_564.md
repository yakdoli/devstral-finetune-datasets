```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_564.jpeg
document_name: chart
page_number: 564
page_id: chart#page_564
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:49:56Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### Overview
- Explanation of normal density curves and their properties.
- Description of the Empirical Rule and the distribution percentages within standard deviations.

#### Normal Density Function

![Figure 348: Normal Density Function](img/figure_348)

Different values of \(\mu\) and \(\sigma\) yield different normal density curves and hence different normal distributions. All normal density curves satisfy the following property, which is often referred to as the Empirical Rule:

- 68% of the observations fall within 1 standard deviation of the mean, that is, between \(\mu - \sigma\) and \(\mu + \sigma\).
- 95% of the observations fall within 2 standard deviations of the mean, that is, between \(\mu - 2\sigma\) and \(\mu + 2\sigma\).
- 99.7% of the observations fall within 3 standard deviations of the mean, that is, between \(\mu - 3\sigma\) and \(\mu + 3\sigma\).

Thus, for a normal distribution, almost all values lie within three standard deviations of the mean.

#### Using the Formula

NormalDistribution is calculated using the `Statistics.UtilityFunctions` class. The following table describes this formula's parameters and its values:

| Method Name       | Parameters                         | Return Value                              |
|-------------------|------------------------------------|-------------------------------------------|
| NormalDistribution | zValue: The value for which the distribution is required. | A double that represents the standard normal cumulative distribution value. |

#### Example

Here is a code snippet that shows a sample usage.

---

## Code Examples

```csharp
// Sample usage of NormalDistribution
using Syncfusion.Windows.Forms.Chart.Utilities;

double zValue = 1.96; // Example z-value
double cumulativeValue = Statistics.UtilityFunctions.NormalDistribution(zValue);
```

## API Reference

### Methods

#### NormalDistribution
- **Parameters**:
  - `zValue`: The value for which the distribution is required.
- **Return Value**:
  - A double that represents the standard normal cumulative distribution value.

## Page-level Navigation/TOC
- [Overview](#overview)
  - [Normal Density Function](#normal-density-function)
  - [Using the Formula](#using-the-formula)
  - [Example](#example)

## Cross References
- Refer to the [Statistics.UtilityFunctions](#statistics-utilityfunctions) class for more details on normal distribution calculations.

## RAG Annotations
<!-- tags: [normal-distribution, statistics, utility-functions, windows-forms, chart, sdk] keywords: [mu, sigma, empirical-rule, standard-deviation, cumulative-distribution] -->
```