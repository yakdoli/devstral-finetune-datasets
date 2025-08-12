```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_350.jpeg
document_name: grid
page_number: 350
page_id: grid#page_350
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:10:55Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes mathematical functions available in the Windows Forms environment.
- Includes SIGN, SIN, SINH, and SKEW functions.

## Content

### SIGN(number)
- **Description**: Returns the sign of a number.
- **Syntax**: `SIGN(number)`, where:
  - `number` is any real number.

### 4.1.4.6.6.213 SIN
- **Description**: Returns the sine of the given angle.
- **Syntax**: `SIN(number)`, where:
  - `number` is the angle in radians for which you want the sine.

### 4.1.4.6.6.214 SINH
- **Description**: Returns the hyperbolic sine of a number.
- **Syntax**: `SINH(number)`, where:
  - `number` is any real number.

#### Remarks
- The formula for the hyperbolic sine is:
  \[
  \sinh(z) = \frac{\mathrm{e}^z - \mathrm{e}^{-z}}{2}
  \]

### 4.1.4.6.6.215 SKEW
- Placeholder for additional content related to the SKEW function.

## Code Examples

### Example: Using the SIN Function
```csharp
double angleInRadians = 1.0;
double sineValue = Math.Sin(angleInRadians);
Console.WriteLine($"The sine of {angleInRadians} radians is {sineValue}.");
```

### Example: Using the SINH Function
```csharp
double number = 1.0;
double hyperbolicSineValue = Math.Sinh(number);
Console.WriteLine($"The hyperbolic sine of {number} is {hyperbolicSineValue} using the formula \sinh(z) = (e^z - e^{-z}) / 2.");
```

## Page-level Navigation/TOC (if applicable)
- This section provides a brief list of the key topics covered on this page.

## Cross References
- Reference to other functions or documentation within the Windows Forms framework can be found here.
- External resources or related pages may also be listed for further exploration.

<!-- tags: [mathematical functions, windows forms, sine, hyperbolic sine, skew] keywords: [SIGN, SIN, SINH, SKEW, Windows Forms, mathematical computations, documentation] -->
```