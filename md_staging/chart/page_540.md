```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_540.jpeg
document_name: chart
page_number: 540
page_id: chart#page_540
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:48:11Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Overview

- paired (where every data point in one series will have a relationship with a particular point of another series).

If the calculated t-statistic exceeds the chosen threshold value (usually 0.05), then the decision is to reject the null hypothesis, which states that the two sample means are equal, in favor of an alternate hypothesis, which typically specifies that the two samples differ.

### Content

Below are the different formulae to calculate the t-statistic:

1. **T-Test with Equal Variances**
   - This formula performs a T test for two groups of data and assumes equal variances between the two groups (i.e., series).

2. **T-Test Paired**
   - This formula performs a paired two-sample Student's t-test to determine whether a sample's means are distinct. This form of the t-test does not assume that the variances of both the populations are equal.
   - Use a paired test when there is a natural pairing of observations in the samples, such as a sample group that is tested twice (e.g., before and after an experiment).

3. **T-Test with Unequal Variances**
   - This formula performs a T-test for two groups of data and assumes unequal variances between the two groups (i.e., series).
   - This analysis tool is referred to as a heteroscedastic t-test and can be used when the groups that are under study are distinct. Use a paired test when there is one group before and after a treatment.

### Note: For programming example, refer to the following Browser Sample:

```
[Installed drive]:\Documents and Settings\[User name]\My
Documents\Syncfusion\EssentialStudio\[Installed
version]\Windows\Chart.Windows\Samples\2.0\Statistical Analysis\Chart Statistical Formulas
```

### 4.12.1.8.1 TTest with Equal Variances

This type of TTest can be performed on two random series that have no relationship with each other. But they should be of equal sizes, i.e., the number of data points of the two series should be the same.

### API Reference

Not explicitly provided in the given text.

### Code Examples

None provided in the given text.

### RAG Annotations

<!-- tags: [product, module, control, api, version?] keywords: [Essential Chart, Windows Forms, T-Test, paired, equal variances, unequal variances, heteroscedastic t-test, sample means, statistical analysis] -->
```