```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_267.jpeg
document_name: grid
page_number: 267
page_id: grid#page_267
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:06:23Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- standard_dev is the population standard deviation for the data range and is assumed to be known.
- size is the sample size.

## Remarks:

- **#VALUE!** - occurs if any argument is non-numeric.
- **#NUM!** - occurs if alpha is less than or equal to zero or if alpha is greater than or equal to zero.
- **#NUM!** - occurs if standard_dev is less than or equal to zero.
- **#DIV/0!** - occurs if the size is equal to one.

### 4.1.4.6.6.38 CORREL

**Returns the correlation coefficient of the array1 and array2 cell ranges.**

#### Syntax
**CORREL(array1, array2)**, where:

- **array1** is a cell range of values.
- **array2** is the second cell range of values.

#### Remarks
- **array1** and **array2** must have the same number of data points.
- The equation for the correlation coefficient is,

\[
Correl(X,Y) = \frac{\sum (x - \overline{x})(y - \overline{y})}{\sqrt{\sum (x - \overline{x})^2 \sum (y - \overline{y})^2}}
\]

where **x-bar** and **y-bar** are the sample means **AVERAGE(array1)** and **AVERAGE(array2)**.

### 4.1.4.6.6.39 COS

**Returns the cosine of the given angle.**
```