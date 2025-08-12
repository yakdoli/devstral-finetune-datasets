```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_200.jpeg
document_name: calculate
page_number: 200
page_id: calculate#page_200
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:42Z
fidelity: lossless
-->

## Essential Calculate

### Overview
- The document describes the `NORMINV` and `NormsDist` functions related to the normal distribution, focusing on their parameters, constraints, and functionality.
- Highlights include the iterative search technique used by `NORMINV` and the probability calculations handled by `NormsDist`.

### Content

#### Probability and Parameters Definition

**Where:**
- `probability` is a probability corresponding to the normal distribution.
- `mean` is the arithmetic mean of the distribution.
- `standard_dev` is the standard deviation of the distribution.

**Remarks:**
- Probability must be >= 0 and <= 1.
- `standard_dev` must be > 0.

Given a value for probability, `NORMINV` seeks value \( x \) such that \( \text{NORMDIST}(x, \text{mean}, \text{standard\_dev}, \text{True}) = \text{probability} \). `NORMINV` uses an iterative search technique.

---

### 4.7.110 NormsDist

#### Function Definition
**NormsDist** returns the probability that the observed value of a standard normal random variable will be less than or equal to the parameter.

**Syntax:**
```csharp
NormsDist(value)
```

**Where:**
- `value` is a numeric value that checks with the random variable.

---

### 4.7.111 NormsInv

#### Function Definition
**NormsInv** returns the standard normal random variable that has Mean 0 and Standard Deviation 1.

**Syntax:**
```csharp
NormsDist(value)
```

**Where:**
- `value` is probability of the standard deviation.

---

## API Reference

### NormsDist
#### Parameters:
- **value** | Numeric | The numeric value to check the random variable.

#### Returns:
- Probability of the standard normal distribution related to the input value.

### NormsInv
#### Parameters:
- **value** | Numeric | Probability of the standard deviation.

#### Returns:
- Standard normal random variable with Mean 0 and Standard Deviation 1.

---

## Code Examples

### Example: Using NormsDist
```csharp
double value = 1.96; // Example value
double probability = NormsDist(value);
// probability contains the cumulative probability for the standard normal distribution.
```

### Example: Using NormsInv
```csharp
double probability = 0.975; // Example probability
double value = NormsInv(probability);
// value contains the standard normal random variable corresponding to the probability.
```

---

### Cross References
- See also: [NORMDIST](#section-id-for-normdist), [Standard Normal Distribution](#section-id-for-normal-distribution)

<!-- tags: [normsdist, normsinv, normal-distribution, syncfusion, winforms, probability, standard-deviation, statistics] keywords: [probability, normsdist, normsinv, iterative-search, standard-normal, normal-distribution, mean, standard-deviation] -->
```