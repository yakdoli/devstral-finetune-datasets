```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_100.jpeg
document_name: grid
page_number: 100
page_id: grid#page_100
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:22:37Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to access and manipulate grid data using properties like `RowCount` and `ColCount`.
- Provides examples in both C# and VB.NET for setting up a data structure and populating it with sample data.

## Content

### Accessing Grid Data Properties

The following C# code snippet demonstrates how to access the number of rows and columns in a grid.

```csharp
public virtual int RowCount
{
    get { return _rowCount; }
}

public virtual int ColCount
{
    get { return _colCount; }
}
```

#### VB.NET Implementation

Below is the VB.NET implementation of a similar class to handle grid data.

```vb
Public Class ExternalData
    Private _rowCount As Integer
    Private _colCount As Integer
    Private _data(,) As Int32

    Public Sub New(ByVal rows As Integer, ByVal cols As Integer)
        MyBase.New()

        ' Set number of rows and number of columns.
        _rowCount = rows
        _colCount = cols

        ' Allocate memory to store data values.
        _data = New Integer(_rowCount - 1, _colCount - 1) {}

        ' Just set data.
        Dim i As Integer
        i = 0
        Do While (i < RowCount)
            Dim j As Integer
            j = 0
            Do While (j < ColCount)
                _data(i, j) = ((100 * i) + j)
                j = (j + 1)
            Loop
            i = (i + 1)
        Loop
    End Sub

    ' Set Properties.
    Public Overridable ReadOnly Property RowCount() As Integer
        Get
```

## API Reference

### Properties
- **RowCount**: Gets the number of rows in the grid.
  - **Returns**: `int` - The number of rows.
- **ColCount**: Gets the number of columns in the grid.
  - **Returns**: `int` - The number of columns.

## Code Examples

### C# Example

The C# example demonstrates how to define virtual properties to access the row and column counts.

```csharp
public virtual int RowCount
{
    get { return _rowCount; }
}

public virtual int ColCount
{
    get { return _colCount; }
}
```

### VB.NET Example

The VB.NET example demonstrates how to create a class to handle grid data, including setting up the dimensions and populating the grid with sample data.

```vb
Public Class ExternalData
    Private _rowCount As Integer
    Private _colCount As Integer
    Private _data(,) As Int32

    Public Sub New(ByVal rows As Integer, ByVal cols As Integer)
        MyBase.New()

        ' Set number of rows and number of columns.
        _rowCount = rows
        _colCount = cols

        ' Allocate memory to store data values.
        _data = New Integer(_rowCount - 1, _colCount - 1) {}

        ' Just set data.
        Dim i As Integer
        i = 0
        Do While (i < RowCount)
            Dim j As Integer
            j = 0
            Do While (j < ColCount)
                _data(i, j) = ((100 * i) + j)
                j = (j + 1)
            Loop
            i = (i + 1)
        Loop
    End Sub

    ' Set Properties.
    Public Overridable ReadOnly Property RowCount() As Integer
        Get
```

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Grid, Data Access, RowCount, ColCount] keywords: [Essential Grid, Windows Forms, Properties, C#, VB.NET, Data Manipulation, Grid Data, Sample Data, Memory Allocation] -->
```