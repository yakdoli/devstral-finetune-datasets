```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_192.jpeg
document_name: calculate
page_number: 192
page_id: calculate#page_192
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:06Z
fidelity: lossless
-->

## Content

### Overview
- The Match function is case-insensitive when searching.
- If the Match function cannot find a match, it returns a #N/A error.
- The match_type parameter is optional, defaulting to 1 if omitted.
- When match_type is set to 0 and used with a text value, wildcards can be applied.

### Where
- `*` - matches any sequence of characters.
- `?` - matches any single character.

#### 4.7.96 MAX
Returns the largest value in a set of values.

**Syntax**
```
MAX(number1, number2, ...)
```

**Parameters**
- `number1, number2, ...` are numbers for which you want to find the maximum value.

#### 4.7.97 MAXA
Returns the largest value in a list of arguments, including text and logical values such as `True` and `False` along with numbers.

**Syntax**
```
MAXA(value1, value2, ...)
```

## API Reference (if applicable)
- **MAX Function**
  - **Parameters:**
    - `number1, number2, ...` - Numbers or cell references to find the maximum value.
  - **Returns:** The largest numeric value.
  - **Example Usage:**
    ```csharp
    double max_value = MAX(10, 20, 30); // Returns 30
    ```
- **MAXA Function**
  - **Parameters:**
    - `value1, value2, ...` - Values or cell references to find the maximum value.
  - **Returns:** The largest value, considering text and logical values.
  - **Example Usage:**
    ```csharp
    double maxa_value = MAXA(10, "20", true); // Returns 20
    ```

## Code Examples
```csharp
using System;

class Program
{
    static void Main()
    {
        double[] numbers = { 10, 20, 30 };
        Console.WriteLine("MAX: " + MAX(numbers));
        
        object[] values = { 10, "20", true };
        Console.WriteLine("MAXA: " + MAXA(values));
    }

    static double MAX(params double[] numbers)
    {
        return numbers.Max();
    }

    static object MAXA(params object[] values)
    {
        double max = Double.MinValue;
        foreach (var value in values)
        {
            if (value is double d)
            {
                if (d > max) max = d;
            }
            else if (value is bool b)
            {
                if (b)
                {
                    if (1 > max) max = 1;
                }
            }
            else if (value is string s)
            {
                if (double.TryParse(s, out double num))
                {
                    if (num > max) max = num;
                }
            }
        }
        return max;
    }
}
```

## Cross References
- Refer to the section on the Match function for more details on text matching operations.
- See also: MIN, MINA, MAXIF, MINIF for related functions.

<!-- tags: [product, module, control, api, version?] keywords: [Match function, MAX, MAXA, MAXIF, MIN, MINA, Match type, Case insensitivity, Wildcards, Logical values, Text values] -->
```