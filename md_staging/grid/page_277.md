```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_277.jpeg
document_name: grid
page_number: 277
page_id: grid#page_277
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:07:04Z
fidelity: lossless
-->

## Overview

- Overview of the `DB` function, which calculates the depreciation of an asset using the fixed-declining balance method.
- Explanation of the `method` parameter used to specify the calculation method (U.S. NASD or European).
- Details on how the `DB` function handles dates for both methods.

## Content

### Method Selection

If method is:

- **False or omitted** – The calculation uses the U.S. (NASD) method.
  - If the starting date is the 31st of a month, it becomes equal to the 30th of the same month.
  - If the ending date is the 31st of a month and the starting date is earlier than the 30th of a month, the ending date becomes equal to the 1st of the next month; otherwise, the ending date becomes equal to the 30th of the same month.

- **True** – The calculation uses the European method.
  - Starting dates and ending dates that occur on the 31st of a month become equal to the 30th of the same month.

### DB Function

#### Section: 4.1.4.6.6.60 DB

**Returns**: The depreciation of an asset for a specified period using the fixed-declining balance method.

#### Syntax

`DB(cost, salvage, life, period, month)`, where:

- **cost**: The initial cost of the asset.
- **salvage**: The value at the end of the depreciation (sometimes called the salvage value of the asset).
- **life**: The number of periods over which the asset is being depreciated (sometimes called the useful life of the asset).
- **period**: The period for which you want to calculate the depreciation. Period must use the same units as life.
- **month**: The number of months in the first year. If month is omitted, it is assumed to be 12.

### Remarks

1. The fixed-declining balance method computes the depreciation at a fixed rate. `DB` uses the following formulas to calculate the depreciation for a period:
   - `(cost - total depreciation from prior periods) * rate`
   - `rate = 1 - ((salvage / cost) ^ (1 / life))`, rounded to three decimal places.
   
2. Depreciation for the first and last periods is a special case. For the first period, `DB` uses this formula:
   - `cost * rate * month / 12`

## API Reference

### Function Signature

```csharp
DB(cost, salvage, life, period, month)
```

#### Parameters

| Name       | Description                                                                 | Default  |
|------------|-----------------------------------------------------------------------------|----------|
| `cost`     | Initial cost of the asset                                                   | -        |
| `salvage`  | Salvage value of the asset at the end of the depreciation period            | -        |
| `life`     | Total number of periods over which the asset is being depreciated           | -        |
| `period`   | The specific period for which the depreciation is calculated                | -        |
| `month`    | Number of months in the first year (optional, defaults to 12 if omitted)    | 12       |

#### Returns

- The depreciation amount for the specified period.

#### Exceptions

- None explicitly mentioned in the provided content.

## Code Examples

### Example: Calculating Depreciation

```csharp
// Example usage of the DB function
double cost = 10000; // Initial cost of the asset
double salvage = 1000; // Salvage value
int life = 5; // Useful life in years
int period = 1; // Calculate depreciation for the first period
int month = 12; // Number of months in the first year

double depreciation = DB(cost, salvage, life, period, month);
Console.WriteLine($"Depreciation for the first period: {depreciation}");
```

## Page-level Navigation/TOC

- [ ] Overview
- [ ] Content
  - [ ] Method Selection
  - [ ] DB Function
    - [ ] Syntax
    - [ ] Remarks
- [ ] API Reference
- [ ] Code Examples

<!-- tags: [syncfusion, windows forms, CalculateDepreciation, fixed-declining-balance, DB-function] keywords: [depreciation, asset, salvage, life, period, month, fixed-rate, depreciation-calculation, first-period-depreciation] -->
```