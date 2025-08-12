```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_354.jpeg
document_name: grid
page_number: 354
page_id: grid#page_354
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:11:10Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

The essential features of the `STANDARDIZE` and `STDEV` functions are described in detail below:

## Content

### 4.1.4.6.6.222 STANDARDIZE

#### Description

Returns a normalized value from a distribution characterized by mean and standard_dev.

#### Syntax

```plaintext
STANDARDIZE(x, mean, standard_dev)
```

Where:

- **x** is the value that you want to normalize.
- **mean** is the arithmetic mean of the distribution.
- **standard_dev** is the standard deviation of the distribution.

#### Remarks

- **standard_dev** must be > 0.
- The equation for the normalized value is:

$$
Z = \frac{X - \mu}{\sigma}
$$

### 4.1.4.6.6.223 STDEV

#### Description

Estimates the standard deviation based on a sample. The standard deviation is a measure of how widely values are dispersed from the average value (the mean).

#### Syntax

```plaintext
STDEV(number1, number2, ...)
```

Where:

- **number1, number2, ...** are number arguments corresponding to a sample of a population.

#### Remarks

- **STDEV** assumes that its arguments are a sample of the population. If your data represents the entire population, then compute the standard deviation using STDEVP.
- **STDEV** uses the following formula:

---

## Code Examples

```csharp
// Example Usage of STANDARDIZE
double x = 5.0;
double mean = 3.0;
double standard_dev = 1.0;
double normalizedValue = STANDARDIZE(x, mean, standard_dev);

// Example Usage of STDEV
double[] sampleData = {1.0, 2.0, 3.0, 4.0, 5.0};
double standardDeviation = STDEV(sampleData);
```

### Notes

- Ensure that the standard deviation (`standard_dev`) is greater than 0 when using `STANDARDIZE` to avoid errors.
- Be mindful of whether your data represents a sample or the entire population when choosing between `STDEV` and `STDEVP`.

## RAG Annotations

<!-- tags: [standardize, stdev, standard deviation, mean, sample, population] keywords: [normalize, distribution, dispersion, arithmetic mean, standard_dev] -->
```