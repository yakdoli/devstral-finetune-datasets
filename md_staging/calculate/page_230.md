```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_230.jpeg
document_name: calculate
page_number: 230
page_id: calculate#page_230
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:31Z
fidelity: lossless
-->

## Summary of Functions: SUMX2PY2 and SYD

### Overview
This page introduces two functions, `SUMX2PY2` and `SYD`, commonly used in financial and mathematical calculations in Excel-like environments, with a focus on their syntax and application.

### SUMX2PY2 Function

#### Syntax
```markdown
SUMX2PY2(array_x, array_y)
```

#### Parameters
- **array_x**: The first array or range of values.
- **array_y**: The second array or range of values.

#### Remarks
- If an array or reference argument contains text, logical values, or empty cells, those values are ignored; however, cells with the value zero are included.
- The equation for the sum of the sum of squares is:
  \[
  SUMX2PY2 = \sum (x^2 + y^2)
  \]

### SYD Function

#### Syntax
```markdown
SYD(cost, salvage, life, per)
```

#### Parameters
- **cost**: The initial cost of the asset.
- **salvage**: The value at the end of the depreciation (sometimes called the salvage value of the asset).
- **life**: The number of periods over which the asset is depreciated (sometimes called the useful life of the asset).
- **per**: The period and must use the same units as `life`.

#### Remarks
- **SYD** is calculated as follows:
  <!-- Placeholder for SYD calculation formula -->

---

## API Reference

### `SUMX2PY2`

**Namespace**: `System`

**Class**: `Math`

- **Parameters**:
  - `array_x`: Array or range of numerical values.
  - `array_y`: Array or range of numerical values.
- **Returns**: A numerical value representing the sum of the sum of squares of the two arrays.

### `SYD`

**Namespace**: `System`

**Class**: `Financial`

- **Parameters**:
  - `cost`: The initial cost of the asset (numerical value).
  - `salvage`: The salvage value of the asset at the end of depreciation (numerical value).
  - `life`: The total useful life of the asset in periods (numerical value).
  - `per`: The specific period over which depreciation is to be calculated (numerical value).
- **Returns**: A numerical value representing the depreciation of the asset for the specified period.

---

## Code Examples

### Using SUMX2PY2
```csharp
using System;

class Program
{
    static void Main()
    {
        double[] array_x = {1, 2, 3};
        double[] array_y = {4, 5, 6};
        double sumX2PY2 = SUMX2PY2(array_x, array_y);
        Console.WriteLine("SUMX2PY2: " + sumX2PY2);
    }

    static double SUMX2PY2(double[] x, double[] y)
    {
        double sum = 0;
        for (int i = 0; i < x.Length; i++)
        {
            sum += Math.Pow(x[i], 2) + Math.Pow(y[i], 2);
        }
        return sum;
    }
}
```

### Using SYD
```csharp
using System;

class Program
{
    static void Main()
    {
        double cost = 10000;
        double salvage = 500;
        double life = 5;
        double per = 2;
        double depreciation = SYD(cost, salvage, life, per);
        Console.WriteLine("Depreciation for period " + per + ": " + depreciation);
    }

    static double SYD(double cost, double salvage, double life, double per)
    {
        double numerator = (life - per + 1);
        double denominator = (life * (life + 1)) / 2;
        return (cost - salvage) * (numerator / denominator);
    }
}
```

---

## Tags and Keywords

<!-- tags: [Syncfusion Winforms, Math, Financial, SUMX2PY2, SYD, Functions, Arithmetic, Depreciation, Arrays] keywords: [SUMX2PY2, SYD, array, cost, salvage, life, per, depreciation, sum of squares, useful life, formula, mathematical function, financial function] -->
```