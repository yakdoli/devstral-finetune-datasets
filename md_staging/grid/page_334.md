```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_334.jpeg
document_name: grid
page_number: 334
page_id: grid#page_334
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:09:50Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This page explains the usage of the PERCENTRANK and PERMUT functions in windows forms.
- Includes details about the syntax, parameters, and remarks for each function.

## Content

### PERCENTRANK
- **array**: The range of data with numeric values that defines relative standing.
- **x**: The value for which you want to know the rank.
- **significance**: An optional value that identifies the number of significant digits for the returned percentage value. If omitted, PERCENTRANK uses three digits (0.xxx).

#### Remarks
- Significance must be >= 1.
- If x does not match one of the values in the array, PERCENTRANK interpolates to return the correct percentage rank.

### 4.1.4.6.6.182 PERCENTRANK.EXC
- The PERCENTRANK.EXC function returns the rank of a value in a data set as a percentage (0 to 1, exclusively) of the data set.
- **Syntax**: PERCENTRANK.EXC(array, x, significance)
  - **array**: The range of data that defines relative standing.
  - **x**: The value for which you want to know the rank.
  - **significance**: An optional value that identifies the number of significant digits for the returned percentage value.

#### Remarks:
- \#NUM! - occurs if this argument is empty.
- \#NUM! - occurs if the argument is less than one.

### 4.1.4.6.6.183 PERMUT
- **Returns**: The number of permutations for a given number of objects that can be selected from a number of objects.
- **Syntax**: PERMUT(number, number_chosen)
  - **number**: An integer that describes the number of objects.
  - **number_chosen**: An integer that describes the number of objects in each permutation.

## API Reference
- **PERCENTRANK**: Returns the rank of a value in a data set as a percentage (0 to 1, inclusive) of the data set.
- **PERCENTRANK.EXC**: Returns the rank of a value in a data set as a percentage (0 to 1, exclusively) of the data set.
- **PERMUT**: Returns the number of permutations for a given number of objects that can be selected from a number of objects.

## Code Examples

```csharp
// Example of using PERCENTRANK
double percentile = PERCENTRANK(new double[] {10, 20, 30, 40, 50}, 25, 2);

// Example of using PERCENTRANK.EXC
double percentileEx = PERCENTRANK.EXC(new double[] {10, 20, 30, 40, 50}, 25, 2);

// Example of using PERMUT
int permutations = PERMUT(4, 2);
```

<!-- tags: [winforms, function, PERCENTRANK, PERCENTRANK.EXC, PERMUT, array, significance] keywords: [rank, percentage, permutations, value, objects, data set, significant digits, numeric values] -->
```