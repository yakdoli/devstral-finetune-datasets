```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_185.jpeg
document_name: calculate
page_number: 185
page_id: calculate#page_185
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:09Z
fidelity: lossless
-->

## Remarks

- Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at an annual interest rate of 12 percent, use \( \frac{12\%}{12} \) for rate and \( 4 \times 12 \) for nper. If you make annual payments on the same loan, use 12% for rate and 4 for nper.

### 4.7.83 IsText

The `IsText` function returns a boolean value after determining that the provided value is a string.

#### Syntax:

```plaintext
IsText(text)
```

where  
- `text` is the value you want to test to check if it is a string or not.

### 4.7.84 KURT

Returns the kurtosis of a data set. Kurtosis characterizes the relative peakedness or flatness of a distribution compared with the normal distribution. Positive kurtosis indicates a relatively peaked distribution. Negative kurtosis indicates a relatively flat distribution.

#### Syntax

```plaintext
KURT(number1, number2, ...)
```

where:  
- `number1, number2, ...` are arguments for which you want to calculate kurtosis. You can also use a single array or a reference to an array instead of arguments separated by commas.

### Remarks

- The arguments must be either numbers or names, arrays or references that contain numbers.
- If an array or reference argument contains text, logical values, or empty cells, those values are ignored; however, cells with the value zero are included.

## Code Examples

No code examples provided in this section.

## Page-level Navigation/TOC (if applicable)

No local Table of Contents present.

## Cross References

No cross-references provided in this section.

## RAG Annotations

<!-- tags: [essential-calculate, remarks, isText, kurt, syntax, remarks, kurtosis] keywords: [units, consistency, rate, nper, boolean, string, peakedness, flatness, distribution, normal distribution, positive kurtosis, negative kurtosis, arguments, references] -->
```