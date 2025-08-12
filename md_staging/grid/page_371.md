```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_371.jpeg
document_name: grid
page_number: 371
page_id: grid#page_371
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:13:04Z
fidelity: lossless
-->

## VARP and VARPA Functions

### Syntax

**VARP(number1, number2, ...)**, where:

- **number1, number2, ...** are number arguments corresponding to a population.

### Remarks

- **VARP** assumes that its arguments are the entire population. If your data represents a sample of the population, then compute the variance using **VAR**.
- The equation for **VARP** is:

  \[
  \frac{\sum (x - \bar{x})^2}{n}
  \]

  where \( \bar{x} \) is the sample mean \( \text{AVERAGE}( \text{number1}, \text{number2}, \dots ) \) and \( n \) is the sample size.

---

### 4.1.4.6.6.256 VARPA

Calculates variance based on the entire population. In addition to numbers and text, logical values such as **True** and **False** are also included in the calculation.

### Syntax

**VARPA(value1, value2, ...)**, where:

- **value1, value2, ...** are arguments corresponding to a population.

### Remarks

- **VARPA** assumes that its arguments are the entire population. If your data represents a sample of the population, you must compute the variance using **VARA**.
- Arguments that contain **True** evaluate as 1; arguments that contain text or **False** evaluate as 0 (zero). If the calculation does not include text or logical values, use the **VARP** worksheet function instead.
- The equation for **VARPA** is:

---

### RAG Annotations

<!-- tags: [variance, population, sample, var, varp, varpa, variance calculation, windows forms, sfcontrols] keywords: [variance, population, sample, var, varp, varpa, logical values, data population, average, sample mean, equation, windows forms, essential grid] -->
```