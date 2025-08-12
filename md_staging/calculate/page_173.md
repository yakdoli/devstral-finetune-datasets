```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_173.jpeg
document_name: calculate
page_number: 173
page_id: calculate#page_173
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:19Z
fidelity: lossless
-->

## Overview

- X must be >= 0.
- Alpha and beta must be > 0.
- The equation for the gamma probability density function is:
  \[
  f(x; \alpha, \beta) = \frac{1}{\beta^\alpha \Gamma(\alpha)} x^{\alpha-1} e^{-\frac{x}{\beta}}
  \]
- The standard gamma probability density function is:
  \[
  f(x; \alpha) = \frac{x^{\alpha-1} e^{-x}}{\Gamma(\alpha)}
  \]
- When alpha = 1, GAMMADIST returns the exponential distribution with:
  \[
  \lambda = \frac{1}{\beta}
  \]

## Content

### 4.7.59 Gammainv

The Gammainv function returns the inverse function for the GAMMADIST function.

#### Syntax:
```plaintext
Gammainv(p, alpha, beta)
```

**where,**
- \( p \) is the probability associated with the gamma distribution.
- \( \alpha \) is a parameter of the distribution.
- \( \beta \) is a parameter of the distribution.

### 4.7.60 GAMMALN

### 4.7.60.1 GAMMAINV

**Returns the inverse of the gamma cumulative distribution. If \( p = \text{GAMMADIST}(x,\dots) \), then \(\text{GAMMAINV}(p,\dots) = x\).**

#### Syntax
```plaintext
GAMMAINV(p,...)
```

## RAG Annotations
<!-- tags: [syncfusion sdk, gammadist, gammainv, api documentation, gamma distribution, exponential distribution] keywords: [gammainv, gammainv syntax, gammadist, gamma probability density function, exponential distribution, inverse gamma distribution] -->
```