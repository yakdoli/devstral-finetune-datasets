```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_290.jpeg
document_name: grid
page_number: 290
page_id: grid#page_290
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:06:54Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explanation of FISHERINV function and its purpose.
- Description of the Fixed function and its usage.
- Explanation of the FLOOR function and its application.

## Content

### 4.1.4.6.6.92 FISHERINV

#### Overview
Returns the inverse of the Fisher transformation. If \( y = \text{FISHER}(x) \), then \( \text{FISHERINV}(y) = x \).

#### Syntax
```csharp
FISHERINV(y)
```
where:
- \( y \) is the value for which you want to perform the inverse of the transformation.

#### Remarks
- The equation for the inverse of the Fisher transformation is:
\[ x = \frac{e^{2y} - 1}{e^{2y} + 1} \]

### 4.1.4.6.6.93 Fixed

#### Overview
The Fixed function rounds off the given value to a specified number of decimal places and returns the value in text format.

#### Syntax
```csharp
Fixed(number, decimal_places, no_commas)
```
where:
- `number` is the number you want to round off.
- `decimal_places` is the number of decimal places you want to display in the result.
- `no_commas` is a logical value. It will display commas when it is set to FALSE and does not display commas when it is set to TRUE.

### 4.1.4.6.6.94 FLOOR

#### Overview
Rounds off the given number down, toward zero, to the nearest multiple of significance.

#### Syntax
```csharp
FLOOR(number, significance)
```
where:
- `number` is the number to be rounded.
- `significance` is the multiple to which the number should be rounded down.

## API Reference

### FISHERINV
- **Namespace**: Syncfusion.Windows.Forms
- **Method**: FISHERINV(y)
- **Parameters**:
  - `y`: The value for the inverse Fisher transformation.
- **Returns**: The original value \( x \) before the Fisher transformation.
- **Remarks**: The inverse Fisher transformation equation is \( x = \frac{e^{2y} - 1}{e^{2y} + 1} \).

### Fixed
- **Namespace**: Syncfusion.Windows.Forms
- **Method**: Fixed(number, decimal_places, no_commas)
- **Parameters**:
  - `number`: The number to be rounded.
  - `decimal_places`: The number of decimal places to display in the result.
  - `no_commas`: A logical value determining whether commas are displayed.
- **Returns**: The rounded value in text format.

### FLOOR
- **Namespace**: Syncfusion.Windows.Forms
- **Method**: FLOOR(number, significance)
- **Parameters**:
  - `number`: The number to be rounded down.
  - `significance`: The multiple to which the number should be rounded.
- **Returns**: The rounded down value.

## Code Examples

### Example 1: FISHERINV
```csharp
double y = 1.0;
double x = FISHERINV(y);
// x will be the value before Fisher transformation
```

### Example 2: Fixed
```csharp
string result = Fixed(12345.6789, 2, true);
// result will be "12345.68"
```

### Example 3: FLOOR
```csharp
double result = FLOOR(2.5, 1);
// result will be 2.0
```

## Cross References
- See also: Other mathematical and rounding functions in the Essential Grid for Windows Forms documentation.

<!-- tags: [syncfusion, windows forms, fisher transform, fixed function, floor function, mathematical functions, rounding, api reference, grid, user guide, syncfusion winforms] keywords: [fisherinv, fixed, floor, fisher transformation, rounding, decimal places, significance, inverse transformation, text format, numerical operations] -->
```