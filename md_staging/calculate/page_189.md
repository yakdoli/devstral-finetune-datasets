```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_189.jpeg
document_name: calculate
page_number: 189
page_id: calculate#page_189
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:23Z
fidelity: lossless
-->

## Essential Calculate

This feature enables you to calculate predicted exponential growth using existing data. This calculates and returns an array of values used for the regression analysis. Logest calculates and returns an array of values that is used in regression analysis.

### Method Table

| Method   | Description                                                  | Parameters               | Type    | Return Type | Reference links |
|----------|--------------------------------------------------------------|--------------------------|---------|--------------|-----------------|
| Logest() | Calculates Logest for an array of cells.                     | known_y's, known_x's, const, stats | Method | String        | N/A             |

### Calculating Logest for an Array of Cells in a Column

The following is the formula to calculate Logest for an array of cells in a column:

#### Syntax

```
=LOGEST([known_y's], [known_x's], [const], [stats])
```

- **Known_y's**: A set of y-values you already know in a relationship, where \( y = b * m^x \).
- **Known_x's**: An optional set of x-values that you may already know in a relationship, where \( y = b * m^x \).
- **Const**: A logical value specifying whether to force the constant \( b \) to equal 1.
- **Stats**: A logical value specifying whether to return additional regression statistics.

#### Code

```
= Logest(B2:B7,A2:A7,TRUE,FALSE)
```

### 4.7.92 LOGINV

**Returns the inverse of the lognormal cumulative distribution function of \( x \)**, where \( \ln(x) \) is normally distributed with parameters mean and standard_dev\. If \( p = \text{LOGNORMDIST}(x, ...) \), then \( \text{LOGINV}(p, ...) = x \).

<!-- tags: [syncfusion, winforms, regression, logest, loginv, exponential growth, lognormal distribution] keywords: [logest, exponential growth, regression analysis, lognormal, inverse, calculate, known_y's, known_x's, const, stats] -->
```