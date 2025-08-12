```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_119.jpeg
document_name: calculate
page_number: 119
page_id: calculate#page_119
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:08Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Demonstrates the use of mathematical functions in a spreadsheet.
- Explains the syntax and usage of the ISEVEN and ISODD functions.
- Provides examples and results for the MULTINOMIAL, ISEVEN, and ISODD functions.

## Content

### MULTINOMIAL Example

#### Formula and Result
| FORMULA     | RESULT |
|-------------|--------|
| =MULTINOMIAL(2, 3, 4) | 1260 |

### 4.5.6.2 ISEVEN

The ISEVEN function returns TRUE if the given number is an even number, and returns FALSE if the given number is odd.

#### Syntax:
The syntax of the ISEVEN function is  
`=ISEVEN(value)`

**The given value must be a numeric value. If it is a non-integer value, the value is rounded down.**

**Note:** If the given value is nonnumeric, the ISEVEN function returns the `#VALUE!` error value.

#### Example:
| FORMULA    | RESULT |
|------------|--------|
| =ISEVEN(-1) | FALSE  |
| =ISEVEN(2.5) | TRUE   |
| =ISEVEN(5) | FALSE  |

### 4.5.6.3 ISODD

The ISODD function returns TRUE if the given number is an odd number, and returns FALSE if the given number is even.

#### Syntax:
The syntax of the ISODD function is  
`=ISODD(value)`

**The given value must be a numeric value. If it is a non-integer value, the value is rounded down.**

## API Reference (if applicable)
- **Namespace:** Syncfusion.Windows.Forms
- **Methods/Properties/Events**
  - `ISEVEN(value)`
  - `ISODD(value)`

## Code Examples (multi-language supported)

```csharp
// Example usage of ISEVEN and ISODD functions
using System;

class Program
{
    static void Main()
    {
        bool isEven = ISEVEN(-1);
        bool isOdd = ISODD(5);

        Console.WriteLine("ISEVEN(-1): " + isEven); // Output: FALSE
        Console.WriteLine("ISODD(5): " + isOdd);   // Output: TRUE
    }

    static bool ISEVEN(double value)
    {
        int intValue = (int)Math.Floor(value);
        return intValue % 2 == 0;
    }

    static bool ISODD(double value)
    {
        int intValue = (int)Math.Floor(value);
        return intValue % 2 != 0;
    }
}
```

## Cross References
- See also: Mathematical Functions, Number Validation Functions.

<!-- tags: Syncfusion Winforms, calculation, mathematical functions, number validation, ISEVEN, ISODD, MULTINOMIAL keywords: ISEVEN, ISODD, MULTINOMIAL, mathematical functions, number validation, syncfusion, winforms -->
```