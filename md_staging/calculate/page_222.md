```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_222.jpeg
document_name: calculate
page_number: 222
page_id: calculate#page_222
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:08Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Number must be >= 0.

## Content

### 4.7.151 STANDARDIZE

**Returns a normalized value from a distribution characterized by mean and standard_dev.**

#### Syntax
STANDARDIZE(x, mean, standard_dev)

**where:**
- **x**: is the value that you want to normalize.
- **mean**: is the arithmetic mean of the distribution.
- **standard_dev**: is the standard deviation of the distribution.

#### Remarks
- standard_dev must be > 0.
- The equation for the normalized value is:

\[
Z = \frac{X - \mu}{\sigma}
\]

### 4.7.152 STDEV

**Estimates the standard deviation based on a sample. The standard deviation is a measure of how widely values are dispersed from the average value (the mean).**

#### Syntax
STDEV(number1, number2, ...)

**where:**
- **number1, number2, ...**: are number arguments corresponding to a sample of a population.

<!-- tags: [syncfusion, calculate, standardize, stdev, standard deviation, arithmetic mean] 
keywords: [normalized value, mean, standard_dev, standard deviation, sample, distribution] -->
```