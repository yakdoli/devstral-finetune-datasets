```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_266.jpeg
document_name: grid
page_number: 266
page_id: grid#page_266
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:05:11Z
fidelity: lossless
-->

## Content

### CONCATENATE (text1, text2, ...)

**CONCATENATE (text1, text2, ...)**, where:

- **text1, text2, ...** are text items to be joined into a single text item. The text items can be text strings, numbers, or single-cell references.

#### Remarks

- The "&" operator can be used instead of CONCATENATE to join text items.

---

### 4.1.4.6.6.36 CONFIDENCE

#### Overview
Returns a value that you can use to construct a confidence interval about a population mean. The confidence interval is a range of values. In your sample, mean x is at the center of this range and the range is \( x \pm \text{CONFIDENCE} \). For example, if \( x \) is the sample mean of delivery times for products ordered through the mail, \( x \pm \text{CONFIDENCE} \) is a range of population means.

#### Syntax
**CONFIDENCE(alpha, standard_dev, size)**, where:

- **alpha** is the significance level used to compute the confidence level. The confidence level equals \( 100 \times (1 - \text{alpha})\%\), or in other words, an alpha of 0.05 indicates a 95 percent confidence level.
- **standard_dev** is the population standard deviation for the data range and is assumed to be known.
- **size** is the sample size.

#### Remarks

- All arguments must be non-numeric.
- **Alpha** must be \( > 0 \) and \( < 1 \).
- **Standard_dev** must be \( > 0 \).
- **Size** must be \( \geq 1 \).

---

### 4.1.4.6.6.37 CONFIDENCE.T

#### Overview
Using a student's distribution, this function retrieves the confidence interval for a population mean.

#### Syntax
**CONFIDENCE.T(alpha, standard_dev, size)** where:

- **alpha** is the significance level used to compute the confidence level.

---

## API Reference (if applicable)

Not applicable for this section.

## Code Examples (multi-language supported)

Not applicable for this section.

## Page-level Navigation/TOC (if applicable)

Not applicable for this section.

## Cross References

Not applicable for this section.

## RAG Annotations

<!-- tags: [Syncfusion Winforms, CONCATENATE, CONFIDENCE, CONFIDENCE.T] keywords: [concatenate text, confidence interval, sample mean, significance level, sample size, student's distribution] -->
```