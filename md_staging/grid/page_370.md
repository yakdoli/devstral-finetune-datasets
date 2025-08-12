```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_370.jpeg
document_name: grid
page_number: 370
page_id: grid#page_370
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:12:16Z
fidelity: lossless
-->

## Overview

- Logical values such as True, False and text are ignored. If logical values and text must not be ignored, use the VARA worksheet function.
- VAR uses the following formula,

\[
\frac{\sum (x - \bar{x})^2}{(n-1)}
\]

where \( \bar{x} \) is the sample mean AVERAGE(number1, number2, ...) and \( n \) is the sample size.

## Content

### 4.1.4.6.6.254 VARA

Estimates variance based on a sample. In addition to numbers and text, logical values such as True and False are included in the calculation.

#### Syntax

VARA(value1, value2, ...), where:

- value1, value2, ... are value arguments corresponding to a sample of a population.

#### Remarks

- VARA assumes that its arguments are a sample of the population. If your data represents the entire population, you must compute the variance using VARPA.
- Arguments that contain True evaluate as 1; arguments that contain text or False evaluate as 0 (zero). If the calculation must not include text or logical values, use the VAR worksheet function instead.
- VARA uses the following formula,

\[
\frac{\sum (x - \bar{x})^2}{(n-1)}
\]

where \( \bar{x} \) is the sample mean AVERAGE(value1, value2, ...) and \( n \) is the sample size.

### 4.1.4.6.6.255 VARP

Calculates variance based on the entire population.

## Page-level Navigation/TOC (if applicable)

- If the page contains a local Table of Contents, include it here as a hierarchical list.

## Cross References

See also:
- Relevant links or references from the page content

## RAG Annotations

<!-- tags: [essential-grid, windows-forms, var-function, vara-function, varp-function, statistical-functions, sample-size, population, variance] keywords: [true, false, logical values, text, ignored values, sample mean, x-bar, sample size, sample variance, population variance, variance formula] -->
```