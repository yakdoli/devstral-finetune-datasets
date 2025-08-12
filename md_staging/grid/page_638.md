```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_638.jpeg
document_name: grid
page_number: 638
page_id: grid#page_638
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:30:40Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the implementation of a manual total summary for a grid in VB.NET.
- Explains the use of Group, FieldDescriptor, and RecordsDetails in a grid context.
- Highlights the calculation and retrieval of a total value based on specific fields in the grid.

## Content

### Implementation of ManualTotalSummary Class

The `ManualTotalSummary` class provides a mechanism to calculate and manage the total of a specific field within a Grid's grouped data. Below is the complete implementation in VB.NET.

```vb
Public Class ManualTotalSummary

    Private total_Renamed As Double
    Private dirty_Renamed As Boolean = True
    Private group_Renamed As Group
    Private fieldIndex_Renamed As Integer = -1

    Public Sub New(ByVal g As Group, ByVal field_Renamed As String)
        Me.New(g, g.ParentTableDescriptor.Fields(field_Renamed))
    End Sub

    Public Sub New(ByVal g As Group, ByVal field_Renamed As FieldDescriptor)
        Me.Field = field_Renamed
        Me.Group = g
    End Sub

    Public Property Total() As Double
        Get
            If dirty_Renamed Then
                CalculateTotal()
                Me.dirty_Renamed = False
            End If
            Return Me.total_Renamed
        End Get
        Set
            Me.total_Renamed = Value
        End Set
    End Property

    Private Sub CalculateTotal()
        total_Renamed = 0

        If TypeOf group_Renamed.Details Is RecordsDetails Then
            For Each r As Record In group_Renamed.Records
                Dim obj As Object = r.GetValue(field_Renamed)
                If Not obj Is Nothing AndAlso Not(TypeOf obj Is DBNull) Then
                    Dim d As Double = Convert.ToDouble(obj)
                    total_Renamed += d
                End If
            Next
        Else
            total_Renamed = -1
        End If
    End Sub
End Class
```

### Explanation of the Code

- **Fields**:
  - `total_Renamed`: Stores the calculated total of the field.
  - `dirty_Renamed`: A flag to indicate whether the total needs recalculation.
  - `group_Renamed`: The group in the grid for which the summary is being calculated.
  - `fieldIndex_Renamed`: The index of the field being summarized.

- **Constructors**:
  - The first constructor initializes the `ManualTotalSummary` by specifying the group and the field name.
  - The second constructor allows initializing with a `FieldDescriptor` instead of a field name.

- **Total Property**:
  - The getter method ensures that the total is recalculated if the `dirty_Renamed` flag is set.
  - The setter method allows updating the total value directly.

- **CalculateTotal Method**:
  - Iterates through the records in the group, retrieves the value of the specified field, and accumulates it in `total_Renamed`.
  - Ensures that `DBNull` values are ignored during the summation.

## API Reference

### Methods
- **CalculateTotal**:
  - **Returns**: `Void`
  - **Description**: Updates the `total_Renamed` field by summing up values of the specified field in the group.

### Properties
- **Total**:
  - **Type**: `Double`
  - **Description**: Gets or sets the total value of the specified field in the group.

## Code Examples

The above code snippet provides a complete implementation for calculating the total of a specific field within a grid's grouped data. It can be extended or modified to suit different summary requirements.

<!-- tags: [syncfusion-winforms, grid, summary, total, vb.net] keywords: [manual total summary, grouped data, records details, field descriptor, total calculation, grid summary] -->
```