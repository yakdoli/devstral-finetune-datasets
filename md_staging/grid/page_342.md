```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_342.jpeg
document_name: grid
page_number: 342
page_id: grid#page_342
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:10:23Z
fidelity: lossless
-->

## Overview
- Describes mathematical functions available in Syncfusion Winforms applications.
- Highlights the RADIANS, RAND, and RANDBETWEEN functions with their syntax and usage.

## Content

### Quotient Function Example
```csharp
= QUOTIENT (-20,6)
```

### RADIANS Function
#### Overview
Converts degrees to radians.

#### Syntax
```csharp
RADIANS(angle)
```
Where:
- `angle` is an angle in degrees that you want to convert.

### RAND Function
#### Overview
Returns an evenly distributed random number greater than or equal to 0 and less than 1.

#### Syntax
```csharp
RAND()
```

### RANDBETWEEN Function
#### Overview
Returns a random number that is between the given ranges. This function returns a new random number each time in recalculation.

#### Syntax
```csharp
RANDBETWEEN(start_num, end_num)
```
Where:
- `start_num` – Required. This is the smallest integer.
- `end_num` – Required. This is the largest integer.

#### Remarks
- **#NUM!** - Occurs if the `end_num` value is larger than the `start_num` value.
- **#VALUE!** - Occurs if any of the given arguments are non-numeric.

## API Reference
- **Namespace**: Syncfusion.Windows.Forms
- **Functions**:
  - `RADIANS`: Converts degrees to radians.
  - `RAND`: Returns a random number between 0 and 1.
  - `RANDBETWEEN`: Returns a random number within a specified range.

## Code Examples
```csharp
// Example of RADIANS function
double angleInDegrees = 90;
double angleInRadians = RADIANS(angleInDegrees);

// Example of RAND function
double randomNum = RAND();

// Example of RANDBETWEEN function
int randomNumber = RANDBETWEEN(1, 100);
```

### Cross References
- See also:
  - Document on mathematical functions in Syncfusion Winforms.
  - Usage examples of random number generation in applications.
  - Guidelines for handling numerical errors in programming.

<!-- tags: [winforms, syncfusion-sdk, math-functions, random-functions, numerical-functions] keywords: [RADIANS, RAND, RANDBETWEEN, degrees, radians, random number, angle conversion, error handling] -->
```