```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_109.jpeg
document_name: calculate
page_number: 109
page_id: calculate#page_109
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:35Z
fidelity: lossless
-->

# Essential Calculate

```csharp
}
catch (Exception ex)
{
    return ex.Message;
}
}
else
{
    try
    {
        s1 = engine.GetValueFromArg(r);
        if (s1 != ""
            && double.TryParse(s1, System.Globalization.NumberStyles.Number,
            null, out d))
        {
            min = Math.Min(min, d);
        }
    }
    catch (Exception ex)
    {
        return ex.Message;
    }
}
if (min != double.MaxValue)
    return min.ToString();
return "";
}
```

### [VB]

```vb
' This sample computes the minimum of an arbitrary range.
' Example:    = Mymin(A1:C3)
' Example:    = mymin(a1,c2,a4,b2,100)
Public Function ComputeMymin(ByVal args As String) As String

    ' Assumes that this.engine is the CalcEngine object.
    Dim min As Double = Double.MaxValue
    Dim d As Double
    Dim s1 As String

    Dim r As String
    For Each r In args.Split(New Char())
```

```markdown
## Overview
- Computes the minimum value from a given range of arguments.
- Handles both numeric and string inputs, converting strings to numbers when possible.
- Implements error handling for invalid inputs.

## Content
The provided code snippet demonstrates how to compute the minimum value from a set of arguments, whether they are provided as a range (e.g., cells in a spreadsheet) or individual values. The function `ComputeMymin` processes each argument, attempting to parse it into a numeric value and updating the minimum value accordingly. Error handling ensures that any exceptions are caught and returned as a message.

## Code Examples

### C# Example
```csharp
catch (Exception ex)
{
    return ex.Message;
}
```

### VB Example
```vb
' Example:    = Mymin(A1:C3)
Public Function ComputeMymin(ByVal args As String) As String
    ' ... (continues as shown in the image)
```

## Exceptions
- `Exception` - General exception for any errors during execution.

## RAG Annotations
<!-- tags: [Syncfusion, WinForms, Calculation, Range, Min, Exception Handling] keywords: [Mymin, TryParse, Math.Min, Split, ComputeMymin, tokenize arguments, error handling, minimum calculation, numeric parsing] -->
```