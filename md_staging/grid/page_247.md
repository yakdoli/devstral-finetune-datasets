```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_247.jpeg
document_name: grid
page_number: 247
page_id: grid#page_247
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:05:14Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
{
    // s is a cell line a21 or c3...
    try
    {
        s1 = engine.GetValueFromArg(s);
    }
    catch (Exception ex)
    {
        return ex.Message;
    }
    if (s1 != "")
    {
        // Add only if positive.
        if (double.TryParse(s1, NumberStyles.Number, null, out double d) && d > 0)
        {
            sum += d;
        }
    }
    else
    {
        try
        {
            s1 = engine.GetValueFromArg(r);
        }
        catch (Exception ex)
        {
            return ex.Message;
        }
        if (s1 != "")
        {
            if (double.TryParse(s1, NumberStyles.Number, null, out double d) && d > 0)
            {
                sum += d;
            }
        }
    }
    return sum.ToString();
}
return "";
}
```

## API Reference

### Methods
- `GetValueFromArg`: Retrieves the value from an argument.
- `TryParse`: Attempts to convert the specified string representation of a number to its `double` equivalent.

### Parameters
- `s`: The string input representing the cell.
- `r`: The string input representing the row.
- `s1`: The string value retrieved from the argument.
- `ex`: The exception object in case of an error.
- `d`: The parsed `double` value from the string.

### Returns
- The sum of positive numbers as a string, or an empty string if no valid numbers are found.

### Exceptions
- `Exception`: Thrown when an error occurs during value retrieval or parsing.

## Code Examples

The provided code snippet demonstrates how to process cell values in a grid and calculate the sum of positive numbers. It ensures that only valid numerical values are added to the sum and handles exceptions gracefully.

## Cross References

See also:
- [GetValueFromArg](#GetValueFromArg)
- [TryParse](#TryParse)
- [Handling Exceptions in Essential Grid](#Handling-Exceptions-in-Essential-Grid)

<!-- tags: [winforms, essential-grid, grid, cell-values, exception-handling, numeric-parsing] keywords: [cell value, positive number, error handling, sum calculation, double parsing] -->
```