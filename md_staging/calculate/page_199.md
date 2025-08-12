```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_199.jpeg
document_name: calculate
page_number: 199
page_id: calculate#page_199
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:44Z
fidelity: lossless
-->

## Normal Distribution Functions in Syncfusion Winforms

### Overview
- Describes the `NORMDIST` function, which returns the normal distribution for the specified mean and standard deviation.
- Explains the `NORMINV` function, which returns the inverse of the normal cumulative distribution for the specified mean and standard deviation.

### Content

#### NORMDIST
>Returns the normal distribution for the specified mean and standard deviation.

**Syntax**

```plaintext
NORMDIST(x, mean, standard_dev, cumulative)
```

**Parameters**

- `x`: The value for which you want the distribution.
- `mean`: The arithmetic mean of the distribution.
- `standard_dev`: The standard deviation of the distribution.
- `cumulative`: A logical value that determines the form of the function. If `cumulative` is `True`, `NORMDIST` returns the cumulative distribution function. If `False`, it returns the probability mass function.

**Remarks**
- `Standard_dev` must be greater than 0.
- The equation for the normal density function (when `cumulative = False`) is:

\[
f(x, \mu, \sigma) = \frac{e^{-\frac{(x-\mu)^2}{2\sigma^2}}}{\sqrt{2\pi}\sigma}
\]

- When `cumulative = True`, the formula is the integral from negative infinity to \(x\) of the given formula.

#### 4.7.109 NORMINV
>Returns the inverse of the normal cumulative distribution for the specified mean and standard deviation.

**Syntax**

```plaintext
NORMINV(probability, mean, standard_dev)
```

## API Reference

### NORMDIST

- **Parameters**:
  - `x`: Value for which you want the distribution.
  - `mean`: Arithmetic mean of the distribution.
  - `standard_dev`: Standard deviation of the distribution.
  - `cumulative`: Logical value that determines the form of the function.

### NORMINV

- **Parameters**:
  - `probability`: The probability corresponding to the normal distribution.
  - `mean`: Arithmetic mean of the distribution.
  - `standard_dev`: Standard deviation of the distribution.

<!-- tags: [syncfusion, winforms, normal distribution, normdist, norminv] keywords: [normal distribution, cumulative, probability mass function, standard deviation, mean, probability, inverse, normal distribution function] -->
```