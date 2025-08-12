```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_289.jpeg
document_name: grid
page_number: 289
page_id: grid#page_289
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:08:01Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Introduces the F.Inv.Rt function and its parameters.
- Explains the FISHER transformation and its application.
- Provides syntax, remarks, and mathematical equations related to these functions.

## Content

### F.Inv.Rt

The F.Inv.Rt function returns the inverse of the F probability distribution.

#### Syntax
F.INV.RT(probability, deg_freedom1, deg_freedom2) where:
- probability is a probability that corresponds to the normal distribution.
- deg_freedom1 is the numerator degrees of freedom.
- deg_freedom2 is the denominator degrees of freedom.

#### Remarks
- #NUM! - occurs if probability is equal to or less than zero.
- #NUM! - occurs if probability is equal to or greater than 1.
- #VALUE! - occurs if probability is non-numeric.
- #NUM! - occurs if deg_freedom1 is less than one.
- #VALUE! - occurs if deg_freedom1 is non-numeric.
- #NUM! - occurs if deg_freedom2 is less than one.
- #VALUE! - occurs if deg_freedom2 is non-numeric.

### FISHER

Returns the Fisher transformation at x. This transformation produces a function that is normally distributed rather than skewed.

#### Syntax
FISHER(x), where:
- x is a numeric value for which you want the transformation.

#### Remarks
- X must be > -1 and < 1.
- The equation for the Fisher transformation is,

\[
z' = \frac{1}{2} \ln \left( \frac{1+x}{1-x} \right)
\]

## Code Examples

- No code examples provided in this section.

## RAG Annotations
<!-- tags: [function, probability distribution, Fisher transformation, degrees of freedom, normal distribution, mathematical equations] keywords: [F.Inv.Rt, FISHER, probability, deg_freedom1, deg_freedom2, x, transformation, skewed, normally distributed, equation, ln, log-normal distribution] -->
```