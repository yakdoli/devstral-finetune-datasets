```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_212.jpeg
document_name: calculate
page_number: 212
page_id: calculate#page_212
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:32Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Explains essential calculations involving the formula for financial calculations.
- Details how to handle cases where the rate is 0 in the formula.
- Provides information on returning the quartile of a data set using the QUARTILE function.
- Explains the conversion of degrees to radians using the RADIANS function.

## Content

### Financial Formula
The formula is as follows:

\[ pv \cdot (1 + rate)^{nperi} + pmt \cdot (1 + rate \cdot type) \cdot \left( \frac{(1 + rate)^{nperi} - 1}{rate} \right) + fv = 0 \]

If the rate is 0:

\[ (pmt \cdot nperi) + pv + fv = 0 \]

### 4.7.132 QUARTILE

#### Overview
Returns the quartile of a data set.

#### Syntax

**QUARTILE(array, quart)**

#### Parameters
- **array**: The array or cell range of numeric values for which you want the quartile value.
- **quart**: Indicates which value to return.

#### Value Returned
- **quart = 0**: Minimum value
- **quart = 1**: First quartile (25th percentile)
- **quart = 2**: Median value (50th percentile)
- **quart = 3**: Third quartile (75th percentile)
- **quart = 4**: Maximum value

### 4.7.133 RADIANS

#### Overview
Converts degrees to radians.

#### Syntax
- Not explicitly shown, but explained that this function converts degrees to radians.

## API Reference

### QUARTILE
- **Parameters**:
  - `array`: Array or cell range of numeric values.
  - `quart`: Integer value indicating which quartile to return (0 to 4).
- **Returns**: The quartile value based on the specified quartile (minimum, first quartile, median, third quartile, or maximum).

### RADIANS
- **Parameters**: Angle in degrees.
- **Returns**: The equivalent value in radians.

## Code Examples (Not explicitly shown in the image, but suggested examples)

### Example of Using QUARTILE Function
```csharp
var values = new double[] { 10, 20, 30, 40, 50 };
var quartile = Syncfusion.Math.Quartile(values, 2);
// quartile will contain the median value
```

### Example of Using RADIANS Function
```csharp
var degrees = 180;
var radians = Syncfusion.Conversion.Radians(degrees);
// radians will be π (approximately 3.14159)
```

## Page-level Navigation/TOC (if applicable)
- 4.7.132 QUARTILE
- 4.7.133 RADIANS

## Cross References
- Possible references to:
  - Other functions in the documentation related to mathematical or statistical calculations.

<!-- tags: [syncfusion, winforms, financial calculations, quartiles, radians] keywords: [quartile, radians, calculate, array, quart, quartile values, degrees, radians conversion] -->
```