```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_356.jpeg
document_name: grid
page_number: 356
page_id: grid#page_356
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:12:09Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### number1, number2, ...

- **number1, number2, ...** are 1 to 30 number arguments corresponding to a population. You can also use a single array or a reference to an array instead of arguments separated by commas.

### Remarks

- STDEVP assumes that its arguments are the entire population. If your data represents a sample of the population, then compute the standard deviation using STDEV.
- STDEVP uses the following formula:

\[
\sqrt{\frac{\sum(x - \overline{x})^2}{n}}
\]

where **x** is the sample mean `AVERAGE(number1, number2,...)` and **n** is the sample size.

---

### 4.1.4.6.6.226 STDEVPA

This section calculates the standard deviation based on the entire population given as arguments, including text and logical values.

#### Syntax

- **STDEVPA(value1, value2, ...),** where:

- **value1, value2, ...** are values corresponding to a population. You can also use a single array or a reference to an array instead of arguments separated by commas.

#### Remarks

- Arguments that contain `True` evaluate as `1`; arguments that contain `text` or `False` evaluate as `0` (zero).
- STDEVPA uses the following formula:

\[
\sqrt{\frac{\sum(x - \overline{x})^2}{n}}
\]

where **x-bar** is the sample mean `AVERAGE(value1, value2,...)` and **n** is the sample size.
```