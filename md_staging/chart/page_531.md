```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_531.jpeg
document_name: chart
page_number: 531
page_id: chart#page_531
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:46:01Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the use of ANOVA (Analysis of Variance) Test in a chart to compare sample means.
- Explains the components of an ANOVA test, including F Ratio, F Critical Value, and Degrees of Freedom.
- Introduces the concept of correlation, also known as the Correlation Coefficient.

## Content

### Anova Test

![Anova Test Sample](image)
*Figure 346: Anova Test*

#### Chart Description:
- **Title:** "Anova Test Sample"
- **Samples:** Sample 1 (orange), Sample 2 (blue), Sample 3 (brown).

#### ANOVA Test Results:
- **FRatio:** 7.04707270231207
- **FCriticalValue:** 3.35413082853029
- **DegreeOfFreedomBetweenGroups:** 2
- **DegreeOfFreedomWithinGroups:** 27
- **DegreeOfFreedomTotal:** 29
- **MeanSquareVarianceBetweenGroups:** 472.988147103484
- **MeanSquareVarianceWithinGroups:** 67.1183861844226
- **SumOfSquaresBetweenGroups:** 945.976294206968
- **SumOfSquaresWithinGroups:** 1812.19642697941
- **SumOfSquaresTotal:** 2758.17272118638

#### Conclusion:
- "ANOVA succeeds to prove (with probability 0.95) that there is inequality between sample means."
- "Because FRatio is bigger than FCriticalValue, we can deduce that there is at least one inequality between means."

### 4.12.1.2 Correlation

**Correlation**, which is otherwise called as **Correlation Coefficient**, is a statistical formula that determines the degree of relationship between the y values of two series representing two variables. This calculation will then be used to measure the depth of synchronization between those two variables.

## Page-level Navigation/TOC (if applicable)
- This page focuses on statistical charting and analysis using essential Winforms controls.

## Cross References
- See also: ANOVA test implementation, Correlation coefficient usage, and chart-related components.

<!-- tags: [ANOVA, correlation, statistical analysis, Winforms, charting] keywords: [anova test, correlation coefficient, statistical formula, synchronization, chart sample, F Ratio, F CriticalValue] -->
```
```