```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_174.jpeg
document_name: calculate
page_number: 174
page_id: calculate#page_174
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:23Z
fidelity: lossless
-->

# Essential Calculate

## Content

### GAMMAINV(probability, alpha, beta)

**where:**

- **probability** is the probability associated with the gamma distribution.
- **alpha** is a parameter to the distribution.
- **beta** is a parameter to the distribution.

#### Remarks

- Probability must be >= 0 and <= 1.
- Alpha and beta must be positive.

**Explanation:** Given a value for probability, GAMMAINV seeks value \( x \) such that \( \text{GAMMADIST}(x, \text{alpha}, \text{beta}, \text{True}) = \text{probability} \). Thus, the precision of GAMMAINV depends on the precision of GAMMADIST. GAMMAINV uses an iterative search technique.

### 4.7.61 GEOMEAN

**Returns the geometric mean of an array or range of positive data.**

#### Syntax

**GEOMEAN(number1, number2,...)**

**where:**

- number1, number2, ... are arguments for which you want to calculate the mean.

#### Remarks

- The arguments must be either numbers or names, arrays, or references that contain numbers.
- All values must be positive.
- The equation for the geometric mean is:

## API Reference

### GAMMAINV

**Description:** This function returns the inverse of the gamma cumulative distribution. It finds the value \( x \) for which the cumulative distribution function (CDF) equals a given probability.

**Syntax:**
```csharp
public static double GAMMAINV(double probability, double alpha, double beta);
```

**Parameters:**

- **probability:** The probability associated with the gamma distribution.
- **alpha:** Parameter to the distribution.
- **beta:** Parameter to the distribution.

**Returns:** The value \( x \) such that \( \text{GAMMADIST}(x, \text{alpha}, \text{beta}, \text{True}) = \text{probability} \).

### GEOMEAN

**Description:** Returns the geometric mean of an array or range of positive data.

**Syntax:**
```csharp
public static double GEOMEAN(params double[] values);
```

**Parameters:**

- **values:** An array of positive numbers.

**Returns:** The geometric mean of the input values.

**Example:**
```csharp
double[] numbers = { 1, 2, 3, 4 };
double geometricMean = GEOMEAN(numbers);
// This will calculate and return the geometric mean of the numbers array.
```

## Code Examples

### Example Using GAMMAINV
```csharp
// Example to find the inverse of the gamma cumulative distribution
double probability = 0.5;
double alpha = 2;
double beta = 3;
double x = GAMMAINV(probability, alpha, beta);
// x will be the value such that GAMMADIST(x, alpha, beta, True) = probability
```

### Example Using GEOMEAN
```csharp
// Example to calculate the geometric mean of a set of numbers
double[] data = { 2, 4, 8 };
double geometricMean = GEOMEAN(data);
// geometricMean will be the geometric mean of the given data array
```

## Page-level Navigation/TOC (if applicable)

- GAMMAINV(probability, alpha, beta)
  - Remarks
- 4.7.61 GEOMEAN
  - Syntax
  - Remarks

## Cross References

- See also: GAMMADIST, Statistical Functions, Probability Distributions

<!-- tags: [gammainv, geomean, statistical functions, gamma distribution, syncfusion sdk] keywords: [inverse, cumulative distribution, probability, mean, geometric mean, api] -->
```