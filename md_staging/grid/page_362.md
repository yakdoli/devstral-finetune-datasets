```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_362.jpeg
document_name: grid
page_number: 362
page_id: grid#page_362
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:11:39Z
fidelity: lossless
-->

## Content

### Overview
- Describes functions for calculating the sum of squares and differences of squares of corresponding values in two arrays.
- Explains the syntax and usage of `SUMX2MY2` and `SUMX2PY2` functions in the context of numerical data analysis.

## WINFORMS-Specific Overview

### SUMX2MY2
Returns the sum of the difference of squares of corresponding values in two arrays.

### Syntax

```markdown
SUMX2MY2(array_x, array_y), where:
- `array_x` is the first array or range of values.
- `array_y` is the second array or range of values.
```

#### Remarks
- If an array or reference argument contains text, logical values, or empty cells, those values are ignored; however, cells with the value zero are included.
- The equation for the sum of the difference of squares is:

\[
\text{SUMX2MY2} = \sum (x^2 - y^2)
\]

### SUMX2PY2
Returns the sum of the sum of squares of corresponding values in two arrays. This sum is a common term in many statistical calculations.

### Syntax

```markdown
SUMX2PY2(array_x, array_y), where:
- `array_x` is the first array or range of values.
- `array_y` is the second array or range of values.
```

## API Reference

### Namespace: Syncfusion.Windows.Forms

#### Methods

- **SUMX2MY2(array_x, array_y)**
  - **Parameters**
    - `array_x`: array or range of values
    - `array_y`: array or range of values
  - **Returns**
    - The sum of the difference of squares of corresponding values.

- **SUMX2PY2(array_x, array_y)**
  - **Parameters**
    - `array_x`: array or range of values
    - `array_y`: array or range of values
  - **Returns**
    - The sum of the sum of squares of corresponding values.

## Code Examples

#### Example: Using SUMX2MY2

```csharp
double[] array1 = {1, 2, 3};
double[] array2 = {4, 5, 6};
double result = SUMX2MY2(array1, array2);
// result = (1^2 - 4^2) + (2^2 - 5^2) + (3^2 - 6^2)
Console.WriteLine(result); // Output: -105
```

#### Example: Using SUMX2PY2

```csharp
double[] array1 = {1, 2, 3};
double[] array2 = {4, 5, 6};
double result = SUMX2PY2(array1, array2);
// result = (1^2 + 4^2) + (2^2 + 5^2) + (3^2 + 6^2)
Console.WriteLine(result); // Output: 91
```

## Page-level Navigation/TOC
- 4.1.4.6.6.236 SUMX2MY2
- 4.1.4.6.6.237 SUMX2PY2

## Cross References
- Refer to documentation on [array handling in Windows Forms] for more details on using arrays as arguments.
- See also: [Mathematical Functions in Windows Forms] for a complete list of mathematical operations.

<!-- tags: [Syncfusion Winforms, SUMX2MY2, SUMX2PY2, array handling, mathematical functions, version 11.4.0.26] keywords: [sum of squares, difference of squares, array operations, statistical calculations, Windows Forms, C#] -->
```