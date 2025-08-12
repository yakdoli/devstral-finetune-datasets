```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_328.jpeg
document_name: grid
page_number: 328
page_id: grid#page_328
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:10:09Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains the use of standard deviation and probability functions in statistical calculations.
- Introduces functions such as NORMINV, NormsInv, NORM.S.DIST, and NORM.S.INV.
- Focuses on the implementation of standard normal distribution and its inverse in programming.

## Content

Given a value for probability, NORMINV seeks value x such that NORMDIST(x, mean, standard_dev, True) = probability. NORMINV uses an iterative search technique.

### NormsInv

The NormsInv function returns the standard normal random variable that has Mean 0 and Standard Deviation 1.

**Syntax:**
```
NormsDist(value)
```

where:
- `value` is the probability of the standard deviation.

### NORM.S.DIST

The NORM.S.DIST function returns the standard normal distribution.

**Syntax:**
```
NORM.S.DIST(z, cumulative)
```
where:
- `z` is the value for which you want the distribution.
- `cumulative` is a logical value that determines the form of the function.

**Remarks:**
The equation for the standard normal density function is:
\[ f(z) = \frac{1}{\sqrt{2 \pi}} e^{-\frac{z^2}{2}} \]

### NORM.S.INV

The NORM.S.INV function returns the inverse of the standard normal cumulative distribution.

**Syntax:**
```
NORM.S.INV(probability)
```
where:
- `probability` is the cumulative probability.

## Page-level Navigation/TOC (if applicable)
- **4.1.4.6.6.168 NormsInv**
- **4.1.4.6.6.169 NORM.S.DIST**
- **4.1.4.6.6.170 NORM.S.INV**

## Cross References
See also:
- NORMDIST
- Standard deviation calculation
- Iterative search techniques
- Cumulative distribution functions

<!-- tags: [winforms, statistical-functions, normal-distribution, iterative-search, cumulative-distribution, norminv, normsinv, normsdist, normsinv] keywords: [probability, standard-deviation, iterative-technique, cumulative-function, norm-inv, norm-dist, normal-density] -->
```
