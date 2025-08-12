```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_527.jpeg
document_name: chart
page_number: 527
page_id: chart#page_527
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:45:45Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- Explains statistical tests and formulas used in data analysis for Windows Forms.
- Provides details on T Test, Variance, and Z Test.
- Discusses the Anova Test method and its steps for comparing group means.

## Content

| **Statistical Method** | **Description** |
|-------------------------|------------------|
| **T Test with unequal variances** | Perform a T Test using Student's distribution (T distribution) with unequal variances. |
| **Variance** | This formula returns the variance within a group of data. |
| **Z Test** | This formula performs a Z Test using Normal distribution. |

### 4.12.1.1 Anova Test

#### Overview of Anova

Anova stands for **Analysis Of Variance**. It is a technique to test the hypothesis that the means among two or more groups of data are equal and thereby, testing the differences between their variances, under the assumption that the sampled groups are normally distributed.

The test actually compares the variation between the groups with the variation within the groups and produces the results based on the values of these variations. If the between variation is larger than the within variation, the means of the groups will not be equal. If both these variations are of approximately the same size, then there will not be any significant difference between the means.

#### Steps to perform an Anova test

The null hypothesis is that there is no difference between the means, and the alternative hypothesis is that at least one mean is different.

The following assumptions must be satisfied before performing the test:

- The groups from which the samples were obtained must be normally distributed.
- The groups are sampled randomly.
- The samples must be independent.
- The variances of the groups must be equal.
- The null hypothesis.

#### Procedure

1. **Calculate the Sum of Squares for total, between and within variations.**

##### Total Variation

\[
SS_{\text{total}} = \left( \sum y_{1}^{2} + \sum y_{2}^{2} + \ldots \sum y_{r}^{2} \right) - \frac{\left( \sum y_{1} + \sum y_{2} + \ldots \sum y_{r} \right)^{2}}{N}
\]

## API Reference

This section does not contain any specific API references.

### Remarks

<!-- tags: [winforms, anova test, variance, t test, z test, statistical methods] keywords: [anova, anova test, variation, statistical test, variance, t test, z test] -->
```