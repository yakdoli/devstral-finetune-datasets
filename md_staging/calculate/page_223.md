```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_223.jpeg
document_name: calculate
page_number: 223
page_id: calculate#page_223
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:12Z
fidelity: lossless
-->

# Essential Calculate

## Remarks

- STDEV assumes that its arguments are a sample of the population. If your data represents the entire population, then compute the standard deviation using STDEVP.
- STDEV uses the following formula:

\[
\sqrt{\frac{\sum(x - \bar{x})^2}{(n-1)}}
\]

where:
- **x-bar** is the sample mean AVERAGE(number1, number2,...).
- **n** is the sample size.

### 4.7.153 STDEVA

#### Overview
- Estimates standard deviation based on a sample. The standard deviation is a measure of how widely values are dispersed from the average value (the mean). Text and logical values such as True and False are also included in the calculation.

#### Syntax
- **STDEVA(value1, value2, ...)**

where:
- **value1, value2,...** are values corresponding to a sample of a population. You can also use a single array or a reference to an array instead of arguments separated by commas.

#### Remarks

- Arguments that contain True evaluate as 1; arguments that contain text or False evaluate as 0 (zero).
- STDEVA uses the following formula:

\[
\sqrt{\frac{\sum(x - \bar{x})^2}{(n-1)}}
\]
```