```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_108.jpeg
document_name: calculate
page_number: 108
page_id: calculate#page_108
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:27Z
fidelity: lossless
-->

## Overview

- Adds a method to accept an argument list and return the minimum value.
- Handles parsing and retrieving values from the argument list using `CalcEngine` methods.
- Discusses handling list separators based on cultural settings.
- Utilizes `CalcEngine.ParseArgumentSeparator`, `GetCellsFromArgs`, and `GetValueFromArg`.

## Content

### Implementing a Custom Min Function

Here's a method that accepts an argument list and computes the minimum value in the list. The list may contain cell references, cell ranges, or numbers. The `CalcEngine` methods are used to handle parsing and retrieving values.

#### Note on List Separators

**Note:** List separators can vary depending on the culture. While a comma is used as a list separator in en-US, it is used as a decimal separator in fr-FR. For this reason, `CalcEngine.ParseArgumentSeparator` is a static member that holds the list separator recognized by algorithms in `CalcEngine`.

```cs
[C#]

// This sample computes the minimum of an arbitrary range.
// Example: = Mymin(A1:C3)
// Example: = mymin(a1,c2,a4,b2,100)
public string ComputeMymin(string args)
{
    // Assumes that this.engine is the CalcEngine object.

    double min = double.MaxValue;
    double d;
    string s1;

    foreach (string r in args.Split(new char[] { CalcEngine.ParseArgumentSeparator }))
    {
        // Cell range
        if (r.IndexOf(':') > -1)
        {
            foreach (string s in engine.GetCellsFromArgs(r))
            {
                // s is a cell line a1, a21, or c3...
                try
                {
                    s1 = engine.GetValueFromArg(s);
                    if (s1 != ""
                        && double.TryParse(s1, System.Globalization.NumberStyles.Number, null, out d))
                    {
                        min = Math.Min(min, d);
                    }
                }
                catch
                {
                    continue;
                }
            }
        }
        else
        {
            // Single cell or number
            try
            {
                s1 = engine.GetValueFromArg(r);
                if (s1 != ""
                    && double.TryParse(s1, System.Globalization.NumberStyles.Number, null, out d))
                {
                    min = Math.Min(min, d);
                }
            }
            catch
            {
                continue;
            }
        }
    }

    return min.ToString();
}
```

### Explanation of Code

1. **Argument Parsing**: The `args.Split` method uses `CalcEngine.ParseArgumentSeparator` to handle list separators based on the current culture.
2. **Handling Cell Ranges**: If the argument contains a colon (`:`), it is treated as a cell range. The `GetCellsFromArgs` method splits the range into individual cell references.
3. **Value Retrieval**: The `GetValueFromArg` method retrieves the numerical value of each cell or number.
4. **Minimum Calculation**: The `Math.Min` function is used to compute the minimum value among all retrieved numbers.
5. **Error Handling**: `try-catch` blocks ensure that the method continues processing even if some cells or arguments are invalid.

#### Key Points

- **List Separators**: Uses the `ParseArgumentSeparator` to handle cultural variations in list separators.
- **Utility Methods**:
  - `GetCellsFromArgs`: Converts a range into individual cell references.
  - `GetValueFromArg`: Converts a cell reference, formula, or number into its numerical value.
- **Handling Exceptions**: Ensures robustness by handling invalid inputs gracefully.

## API Reference

### Methods Used

- **CalcEngine.ParseArgumentSeparator**: Returns the list separator recognized by the parsing algorithms.
- **CalcEngine.GetCellsFromArgs(string args)**: Converts a cell range into individual cell references.
- **CalcEngine.GetValueFromArg(string arg)**: Retrieves the numerical value of a cell, formula, or number.
- **System.Globalization.NumberStyles**: Specifies the number styles allowed for parsing.
- **double.TryParse(string, IFormatProvider, out double)**: Attempts to convert a string to a double, returning `true` on success.
- **Math.Min(double, double)**: Returns the smaller of two numbers.

### Parameters

| Name       | Type                | Description                                                                         |
|------------|---------------------|-------------------------------------------------------------------------------------|
| `args`     | `string`            | The input argument list containing cell references, ranges, or numbers.        |
| `ParseArgumentSeparator` | `char` | The separator character used to split arguments based on culture settings.     |

### Returns

- **Type**: `string`
- **Description**: The minimum value in the list, as a string.

### Exceptions

- Handled internally within `try-catch` blocks to ensure the method is robust.

## Code Examples

### Example 1: Using Cell Ranges

```cs
// Computes the minimum value in the range A1:C3
public string ComputeMymin(string args)
{
    // Implementation as shown above
}
```

### Example 2: Using Individual Cells and Numbers

```cs
// Computes the minimum value among a1, c2, a4, b2, and 100
public string ComputeMymin(string args)
{
    // Implementation as shown above
}
```

## Cross References

- See also:
  - [CalcEngine Methods](#calcengine-methods)
  - [Handling Cultural Variations](#handling-cultural-variations)

<!-- tags: [syncfusion, winforms, calcengine, range parsing, culture-dependent, min function] keywords: [CalcEngine, ParseArgumentSeparator, GetCellsFromArgs, GetValueFromArg, TryParse, Math.Min, cultural settings, list separator, cell range, minimum value, argument list, robustness, try-catch, utility methods] -->
```