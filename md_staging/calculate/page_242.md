```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_242.jpeg
document_name: calculate
page_number: 242
page_id: calculate#page_242
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:28Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- This page describes the mathematical formula and parameters for performing a Z-test using the `ZTEST` function in Syncfusion Winforms.

## Content

The Z-test formula is represented as follows:

\[ ZTEST(array, \mu_o) = 1 - NORMSDIST\left(\frac{(\overline{x} - \mu_o) \cdot \sqrt{n}}{s}\right) \]

### Formula Explanation
- **\( \overline{x} \)**: Represents the sample mean, calculated as AVERAGE(array).
- **\( s \)**: Represents the sample standard deviation, calculated as STDEV(array).
- **\( n \)**: Represents the number of observations in the sample, calculated as COUNT(array).

### Parameters
- **\( array \)**: The input data array used to calculate the sample mean and standard deviation.
- **\( \mu_o \)**: The hypothesized population mean against which the test is performed.

<!-- tags: [syncfusion, ztest, array, population mean, sample mean, standard deviation, number of observations] keywords: [ztest, array, sample mean, standard deviation, population mean, calculate] -->
```