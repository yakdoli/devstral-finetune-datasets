```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_293.jpeg
document_name: grid
page_number: 293
page_id: grid#page_293
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:08:15Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- The page describes the syntax and usage of financial functions such as `FVSchedule` and `GAMMADIST`.
- Examples include function parameters, return types, and specific mathematical equations for the gamma probability density function.

## Content

### FVSchedule
**Syntax:**
- `FVSchedule(arg1, arg2)` where:
  - `Arg1` is the present value.
  - `Arg2` is an array of interest rates to apply.

**Remarks:**
- `#VALUE!` – occurs any other than numbers or blank cells.

---

### GAMMADIST
**4.1.4.6.6.98 GAMMADIST**

#### Overview
- Returns the gamma distribution.

#### Syntax
- `GAMMADIST(x, alpha, beta, cumulative)`, where:

  - **x** is the value at which you want to evaluate the distribution.
  - **alpha** is a parameter to the distribution.
  - **beta** is a parameter to the distribution. If `beta = 1`, `GAMMADIST` returns the standard gamma distribution.
  - **cumulative** is a logical value that determines the form of the function. If `cumulative` is `True`, `GAMMADIST` returns the cumulative distribution function; if `False`, it returns the probability density function.

#### Remarks
- **X must be >= 0.**
- **Alpha and beta must be > 0.**
- **The equation for the gamma probability density function is:**
  \[
  f(x; \alpha, \beta) = \frac{1}{\beta^{\alpha} \Gamma(\alpha)} x^{\alpha-1} e^{\frac{-x}{\beta}}
  \]

- **The standard gamma probability density function is:**
  \[
  f(x; \alpha) = \frac{x^{\alpha-1} e^{-x}}{\Gamma(\alpha)}
  \]

## API Reference (if applicable)
- None provided in the text.

## Code Examples (multi-language supported)
- None provided in the text.

## Page-level Navigation/TOC (if applicable)
- None provided in the text.

## Cross References
- None provided in the text.

## RAG Annotations
<!-- tags: [winforms, essentialgrid, financialfunctions, gammadist, fvschedule] keywords: [gamma distribution, cumulative distribution function, probability density function, financial calculations, present value, interest rates] -->
```