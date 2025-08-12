<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_639.jpeg
document_name: grid
page_number: 639
page_id: grid#page_639
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:30:14Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
End If
Next r
Else
    For Each g As Group In group_Renamed.Groups
        Dim tsa As IManualTotalSummaryArraySource =
            CType(IIf(TypeOf g Is IManualTotalSummaryArraySource, g,
                      Nothing), IManualTotalSummaryArraySource)
        Dim mt As ManualTotalSummary =
            tsa.GetManualTotalSummaryArray()(Me.FieldIndex)
        If mt Is Nothing Then
            mt = New ManualTotalSummary(g, field_Renamed)
        End If
        Dim d As Double = mt.Total
        total_Renamed += d
    Next g
End If
End Sub

Public Sub ApplyDelta(ByVal r As Element, ByVal isObsoleteRecord As Boolean,
                      ByVal isAddedRecord As Boolean, ByVal ci As ChangedFieldInfo)
    If Dirty Then
        Return
    End If
    Dim mt As ManualTotalSummary = Me
    If isObsoleteRecord Then
        If Not ci.OldValue Is Nothing AndAlso Not (TypeOf ci.OldValue Is DBNull) Then
            mt.Total -= Convert.ToDouble(ci.OldValue)
        End If
    Else If isAddedRecord Then
        If Not ci.NewValue Is Nothing AndAlso Not (TypeOf ci.NewValue Is DBNull) Then
            mt.Total += Convert.ToDouble(ci.NewValue)
        End If
    Else
        mt.Total += ci.Delta
        End If
    End If
End Sub
End Class
```

## Overview
- The `ManualTotalSummary` class is introduced to calculate a new total dynamically based on record changes.
- It uses the `ManualTotalSummaryTable` class, which inherits from `GridTable` and overrides the `OnRecordChanged` event to track changes to individual records.

## Content

### ManualTotalSummary Overview
- **Purpose**: The `ManualTotalSummary` class calculates the new total when there are changes to records in a grid.
- **Calculation Method**:
  - Implements a mechanism to apply deltas (`ApplyDelta`) to the total based on whether a record is obsolete, added, or modified.
  - Utilizes the `Dirty` flag to determine if the total needs to be recalculated.
  - Ensures proper handling of `DBNull` values and numeric conversions.

### ManualTotalSummaryTable
- **Class Hierarchy**: The `ManualTotalSummaryTable` class derives from `GridTable` and overrides the `OnRecordChanged` event.
- **Responsibilities**:
  - Tracks changes to records and keeps track of the old and new values of the ChangedField.
  - For each entry in `ManualTotalSummaryTable.TotalSummaries`, a `ManualTotalSummary` instance is created.
  - Ensures accurate calculation of the total by maintaining a list of summaries associated with the table.

### Usage Flow
1. **Record Changes**: When changes occur in the grid, the `OnRecordChanged` event is triggered.
2. **Delta Calculation**: For each summary, the `ApplyDelta` method is invoked to adjust the total based on the change.
   - For obsolete records, the old value is subtracted from the total.
   - For added records, the new value is added to the total.
   - For modified records, the delta value is applied.
3. **Total Update**: The total is updated only if the `Dirty` flag is not set, ensuring efficient recalculations.

### Code Example
The provided code snippet illustrates the implementation of the `ApplyDelta` method, which handles the addition or subtraction of values based on the type of record change (obsolete, added, or modified). It also demonstrates how `ManualTotalSummary` instances are associated with groups and utilized to calculate the total.

### Key Features
- **Dynamic Total Calculation**: The class dynamically recalculates the total based on record modifications.
- **Handling Null Values**: Proper handling of `DBNull` values ensures robustness in data operations.
- **Granular Control**: Provides fine-grained control over total summarization through summary management.

## API Reference
### Methods
- **ApplyDelta**:
  - **Parameters**:
    - `r`: The `Element` representing the record.
    - `isObsoleteRecord`: A boolean indicating if the record is obsolete.
    - `isAddedRecord`: A boolean indicating if the record is newly added.
    - `ci`: The `ChangedFieldInfo` containing details about the change.
  - **Behavior**: Adjusts the total based on the type of change (obsolete, added, or modified).

### Classes
- **ManualTotalSummary**
  - **Purpose**: Maintains the state and logic for calculating the total for a specific group.
- **ManualTotalSummaryTable**
  - **Purpose**: Manages the collection of summaries and tracks record changes to calculate the total dynamically.

## Code Examples

The provided code demonstrates the integration of `ManualTotalSummary` and `ManualTotalSummaryTable` in calculating the total for grouped records. The `ApplyDelta` method ensures that totals are updated efficiently based on the changes made to the grid records.

### Example Usage
```vb
' Example of using ManualTotalSummary
Dim table As New ManualTotalSummaryTable()
Dim summary As New ManualTotalSummary(table)
summary.ApplyDelta(record, isObsolete, isAdded, fieldInfo)
```

## Conclusion
The `ManualTotalSummary` class, paired with the `ManualTotalSummaryTable` class, provides a powerful mechanism for maintaining accurate totals in a grid. By dynamically recalculating totals based on record changes, it ensures data integrity and efficiency in summary calculations.

<!-- tags: [syncfusion, winforms, grid, manual total summary, summary table, dynamic total calculation, record change event] keywords: [ManualTotalSummary, ManualTotalSummaryTable, OnRecordChanged, ApplyDelta, dBNull, Delta, total calculation, grid table, windows forms] -->