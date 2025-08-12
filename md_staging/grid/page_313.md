```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_313.jpeg
document_name: grid
page_number: 313
page_id: grid#page_313
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:09:23Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Provides a formula to calculate Logest for an array of cells in a column.
- Describes the syntax and parameters of the Logest function.
- Includes code examples for using the Logest function.
- Explains the IsLogical function and its syntax.
- Details the LOGINV function and its relationship with LOGNORMDIST.

## Content

### Logest Function

**Syntax**

```plaintext
=LOGEST(known_y's, [known_x's], [const], [stats])
```

- `Known_y's`: A set of y-values you already know in a relationship, where \( y = b \cdot m^x \).
- `Known_x's`: An optional set of x-values that you may already know in a relationship, where \( y = b \cdot m^x \).
- `Const`: A logical value specifying whether to force the constant \( b \) to equal 1.
- `Stats`: A logical value specifying whether to return additional regression statistics.

**Code**

```plaintext
=LOGEST(B2:B7, A2:A7, TRUE, FALSE)
```

### IsLogical Function

**Syntax**

```plaintext
IsLogical(value)
```

- `value`: The value that you want to check whether it is logical. If the value is TRUE or FALSE, this function will return TRUE. Otherwise, it will return FALSE.

**Description**

The IsLogical function checks whether a value is a logical value and returns TRUE or FALSE.

### LOGINV Function

**Description**

Returns the inverse of the lognormal cumulative distribution function of \( x \), where \( \ln(x) \) is normally distributed with parameters mean and standard_dev. If \( p = \text{LOGNORMDIST}(x, ...) \), then \( \text{LOGINV}(p, ...) = x \).

<!-- tags: [logest, islogical, loginv, grid, winforms, regression, synchronization, statistics, logical, distribution, parameters, function, syntcaxy, code, example] keywords: [logest, islogical, loginv, grid, winforms, regression, synchronization, statistics, logical, distribution, parameters, function, syntax, code, example] -->
```