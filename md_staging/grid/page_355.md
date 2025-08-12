```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_355.jpeg
document_name: grid
page_number: 355
page_id: grid#page_355
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:12:08Z
fidelity: lossless
-->

## Overview

This section explains the use of functions in Windows Forms that calculate standard deviation. It covers the syntax and usage of functions like STDEVA and STDEV.

## Content

### 4.1.4.6.6.224 STDEVA

Estimates standard deviation based on a sample. The standard deviation is a measure of how widely values are dispersed from the average value (the mean). Text and logical values such as True and False are also included in the calculation.

#### Syntax

STDEVA(value1, value2, ...), where:

- **value1, value2, ...** are values corresponding to a sample of a population. You can also use a single array or a reference to an array instead of arguments separated by commas.

#### Remarks

- Arguments that contain True evaluate as 1; arguments that contain text or False evaluate as 0 (zero).
- STDEVA uses the following formula:

\[
\sqrt{\frac{\sum (x - \bar{x})^2}{(n-1)}}
\]

where x-bar is the sample mean AVERAGE(value1, value2, ...) and **n** is the sample size.

### 4.1.4.6.6.225 STDEV

Calculates standard deviation based on the entire population given as arguments.

#### Syntax

STDEV(number1, number2, ...), where:

  

## Code Examples (multi-language supported)

<!-- tags: [product, module, control, api, version?] keywords: [standard deviation, STDEVA, STDEV, sample, population, Windows Forms] -->
```