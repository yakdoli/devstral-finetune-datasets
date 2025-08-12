```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_052.jpeg
document_name: calculate
page_number: 052
page_id: calculate#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:14Z
fidelity: lossless
-->

## Implementing the ICalcData Interface

### Overview
- Demonstrates how to implement the `ICalcData` interface in C# and VB.NET.
- Explains the process of adding interface stubs using the drop-down lists in Visual Studio for VB.NET.

### Content

#### Implementing the ICalcData Interface in C#
The following C# code snippet illustrates how to implement the `ICalcData` interface:

```csharp
using System;
using Syncfusion.Calculate;

namespace Calculate_ICalcData
{
    /// <summary>
    /// Wrapper class for a double array.
    /// </summary>
    /// <remarks>
    /// Wrapper class for a double array that adds an extra column
    /// to hold the sum of each row, and also adds an extra row
    /// to hold the sum of the columns.
    /// </remarks>
    public class ArrayCalcData : ICalcData
    {
        /// <summary>
        /// original double array
        /// </summary>
        private double[,] dValues;
    }
}
```

- **Figure 24**: Implementing the ICalcData Interface in C#

#### Implementing the ICalcData Interface in VB.NET
If you are using VB.NET, you can add the `ICalcData` stubs using the drop-down lists at the top of the edit window in Visual Studio. In the left drop-down, select the `ICalcData` interface as shown below:

```vb
Public Class ArrayCalcData
    Implements ICalcData

    ' <summary>
    ' original double array
    ' </summary>
    Private dValues(,) As Double
End Class
```

- **Figure 25**: Implementing the ICalcData Interface in VB, Choosing the Interface

### API Reference
The following APIs are relevant in this context:
- **Namespace**: `Syncfusion.Calculate`
- **Class**: `ArrayCalcData`
- **Interface**: `ICalcData`
- **Properties**:
  - `private double[,] dValues;`

### Code Examples

#### C#
```csharp
using System;
using Syncfusion.Calculate;

namespace Calculate_ICalcData
{
    public class ArrayCalcData : ICalcData
    {
        private double[,] dValues;

        // Add necessary method implementations here
    }
}
```

#### VB
```vb
Public Class ArrayCalcData
    Implements ICalcData

    Private dValues(,) As Double

    ' Add necessary method implementations here
End Class
```

### Cross References
See also:
- [Syncfusion.Calculate Namespace Documentation](#)
- [Instructions on Implementing Interfaces in Visual Studio](#)

<!-- tags: [Syncfusion Winforms, ICalcData, interface implementation, C#, VB.NET] keywords: [ICalcData, Visual Studio, drop-down lists, wrapper class, array, double array, extra column, extra row] -->
```