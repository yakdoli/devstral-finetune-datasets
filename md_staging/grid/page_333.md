```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_333.jpeg
document_name: grid
page_number: 333
page_id: grid#page_333
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:10:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Introduction

- PERCENTILE.EXC function returns the k-th percentile of values in a range.
- PERCENTILE.INC function returns the k-th percentile of values in a range.
- PERCENTRANK returns the rank of a value in a data set as a percentage of the data set.

---

### PERCENTILE.EXC

#### Overview
The PERCENTILE.EXC function returns the k-th percentile of values in a range, where k is in the range of 0 to 1, exclusively.

#### Syntax
PERCENTILE.EXC(array, k) where:
- `array` is the range of data that defines relative standing.
- `k` is the percentile value in the range of 0 to 1.

#### Remarks
- `#NUM!` - occurs if k is equal to or less than zero.
- `#NUM!` - occurs if the array is empty.
- `#NUM!` - occurs if k is equal to or greater than 1.
- `#VALUE!` - occurs if k is non-numeric.

---

### PERCENTILE.INC

#### Overview
The PERCENTILE.INC function returns the k-th percentile of values in a range, where k is in the range 0 to 1.

#### Syntax
PERCENTILE.INC(array,k) where:
- `array` is the range of data that defines relative standing.
- `k` is the percentile value in the range 0 to 1.

#### Remarks
- `#NUM!` - occurs if k is equal to or less than zero.
- `#NUM!` - occurs if array is empty.
- `#NUM!` - occurs if k is equal to or greater than 1.
- `#VALUE!` - occurs if k is non-numeric.

---

### PERCENTRANK

#### Overview
Returns the rank of a value in a data set as a percentage of the data set.

#### Syntax
PERCENTRANK(array, x, significance), where:
- `array` is the data set.
- `x` is the value for which you want to know the rank.
- `significance` is a parameter that specifies the number of significant digits that the returned percentage value is rounded to.

## API Reference

### Parameters
| Name | Description |
|------|-------------|
| array | The data set used to find the rank percentage. |
| x | The value to find the rank of. |
| significance | The number of significant digits for rounding the percentage value. |

## Code Examples

None provided in the image.

## Cross References

- See also: PERCENTILE.EXC, PERCENTILE.INC

<!-- tags: [percentile, percentrank, winforms, numeric functions, statistics] keywords: [percentile, inc, exc, rank, numeric, data set, k-th percentile] -->
```