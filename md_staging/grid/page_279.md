```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_279.jpeg
document_name: grid
page_number: 279
page_id: grid#page_279
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:07:07Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- The page provides detailed information about the `DDB` (Declining Balance Depreciation) calculation and two mathematical functions: `DECIMAL` and `DEGREES`.

## Content

### Depreciation Calculation: `DDB`

**Parameters:**
- **period**: The period for which you want to calculate the depreciation. This period must use the same units as the life of the asset.
- **factor**: The rate at which the balance declines. If factor is omitted, it is assumed to be 2 (the double-declining balance method).

**Note:** All five arguments must be positive numbers.

**Remarks:**
- The double-declining balance method computes the depreciation at an accelerated rate.
- Depreciation is highest in the first period and decreases in successive periods.
- DDB uses the following formula to calculate depreciation for a period:
  \[
  ((\text{cost} - \text{salvage}) - \text{total depreciation from prior periods}) * \left(\frac{\text{factor}}{\text{life}}\right)
  \]

### `DECIMAL` Function

**Description:**  
A text representation of a number in a given base has been converted into a decimal number.

**Syntax:**  
`DECIMAL(text, radix)`  
where:
- `text` is a string.
- `radix` is an integer.

**Remarks:**  
- `#NUM!` or `#VALUE!` - occurs if `text` or `radix` is outside the constraints.

### `DEGREES` Function

**Description:**  
Converts radians into degrees.

**Syntax:**  
`DEGREES(angle)`  
where:
- `angle` is the angle in radians that you want to convert.

## API Reference (if applicable)
- **`DDB` Function:** Used for calculating depreciation using the double-declining balance method.
- **`DECIMAL` Function:** Converts a text representation of a number in a given base to a decimal number.
- **`DEGREES` Function:** Converts an angle from radians to degrees.

## Code Examples (multi-language supported)
```csharp
// Example of using the DDB function
double cost = 10000; // Initial cost of the asset
double salvage = 1000; // Salvage value of the asset
double life = 5; // Useful life of the asset in years
double factor = 2; // Double-declining balance factor
int period = 1; // First period

double depreciation = DDB(cost, salvage, life, period, factor);

// Example of using the DECIMAL function
string numberText = "1A";
int radix = 16;
double decimalNumber = DECIMAL(numberText, radix);

// Example of using the DEGREES function
double radians = Math.PI / 4;
double degrees = DEGREES(radians);
```

## Page-level Navigation/TOC (if applicable)
- Depreciation Calculation: `DDB`
- `DECIMAL` Function
- `DEGREES` Function

## Cross References
- See also: Depreciation methods, mathematical conversions, and angle measurements.

<!-- tags: [Syncfusion Winforms, DDB, DECIMAL, DEGREES, depreciation, conversion, angle] keywords: [DDB, DECIMAL, DEGREES, depreciation, radians, degrees, mathematical functions, conversion] -->
```