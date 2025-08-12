```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_049.jpeg
document_name: calculate
page_number: 049
page_id: calculate#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:41Z
fidelity: lossless
-->

## Overview

There is a simple calculation engine being built. The class includes variable declarations such as `colSums`, `rowCount`, and `colCount`. Below is a portion of the class design in both C# and VB.NET showing essential details for handling double arrays and calculating sums for rows and columns.

### Essential Calculate

```csharp
private object[] colSums;

int rowCount;
int colCount;

//...
}
```

#### VB.NET Implementation

```vb
Imports System
Imports Syncfusion.Calculate

Public Class ArrayCalcData

    ''' <summary>
    ''' Original double array.
    ''' </summary>
    Private dValues(,) As Double

    ''' <summary>
    ''' Vector holding the sum of the rows.
    ''' </summary>
    ''' <remarks>
    ''' Serves as the last column.
    ''' </remarks>
    Private rowSums() As Object

    ''' <summary>
    ''' Vector holding the sum of the columns.
    ''' </summary>
    ''' <remarks>
    ''' Serves as the last row.
    ''' </remarks>
    Private colSums() As Object

    Dim rowCount As Integer
    Dim colCount As Integer

End Class
```

### Constructor Implementation

5. Here, you are making a constructor that accepts a double array as an argument. In the constructor code, you must save the reference that is to be passed in a double array, initialize two `RowCount` and `ColCount` fields and allocate the two additional arrays that are needed to hold the added sums you want.

## Page-Level Navigation/TOC (if applicable)

- Essential Calculate
  - Overview of the calculation engine
  - Detailed class structure in both C# and VB.NET

## Cross References

- Refer to relevant sections on array handling and calculation methods in earlier or later pages of the document.

<!-- 
tags: [Essential Calculate, Array Calculation Engine, Double Array, RowSum, ColSum, VB.NET, C#] 
keywords: [calculate, array, row sum, column sum, constructor, doubles, Syncfusion, WinForms] 
-->
```