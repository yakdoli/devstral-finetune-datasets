```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_169.jpeg
document_name: calculate
page_number: 169
page_id: calculate#page_169
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:06Z
fidelity: lossless
-->

# Essential Calculate

## Content

The FINV function syntax has the following three arguments (Argument is a value that provides information to an action, an event, a method, a property, a function, or a procedure):

- **Probability** is a probability associated with the F cumulative distribution.
- **Deg_freedom1** is the numerator degrees of freedom.
- **Deg_freedom2** is the denominator degrees of freedom.

### 4.7.52 FISHER

Returns the Fisher transformation at \( x \). This transformation produces a function that is normally distributed rather than skewed.

#### Syntax

FISHER(x)

where:

- \( x \) is a numeric value for which you want the transformation.

#### Remarks

- \( x \) must be \( > -1 \) and \( < 1 \).
- The equation for the Fisher transformation is:

\[
z' = \frac{1}{2} \ln \left( \frac{1 + x}{1 - x} \right)
\]

### 4.7.53 FISHERINV

Returns the inverse of the Fisher transformation. If \( y = \text{FISHER}(x) \), then \( \text{FISHERINV}(y) = x \).

#### Syntax

FISHERINV(y)

### Page-level Navigation/TOC

- FINV function syntax and arguments
- FISHER transformation overview
- FISHERINV inverse transformation description

### Cross References

See also:
- FINV function
- F cumulative distribution
- Fisher transformation
- Inverse Fisher transformation

<!-- tags: [Syncfusion, Winforms, FINV, FISHER, FISHERINV, Fisher transformation] keywords: [FINV, FISHER, FISHERINV, Fisher transformation, inverse Fisher transformation, degrees of freedom, probability, transformation equation, PDF OCR] -->
```