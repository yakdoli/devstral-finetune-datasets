```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_641.jpeg
document_name: grid
page_number: 641
page_id: grid#page_641
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:29:20Z
fidelity: lossless
-->

## Content

### [VB.NET]

#### ManualTotalSummaryTable Class

```vb
Public Class ManualTotalSummaryTable : Inherits GridTable

    Public Sub New(ByVal tableDescriptor As TableDescriptor, ByVal parentRelationTable As Table)
        MyBase.New(CType(tableDescriptor, GridTableDescriptor), CType(parentRelationTable, GridTable))
    End Sub

    Private totalSummaries_Renamed As ArrayList = New ArrayList()
    Public Property TotalSummaries() As ArrayList
        Get
            Return Me.totalSummaries_Renamed
        End Get
        Set
            Me.totalSummaries_Renamed = Value
        End Set
    End Property
    '..............'
    '..............'

    Protected Overrides Sub OnRecordChanged(ByVal r As Element, ByVal isObsoleteRecord As Boolean, ByVal isAddedRecord As Boolean)
        Dim td As TableDescriptor = TableDescriptor
        Dim g As Group = r.ParentGroup
        Do While TypeOf g Is IManualTotalSummaryArraySource
            OnGroupSummaryInvalidated(New GroupEventArgs(g))

            Dim tsa As IManualTotalSummaryArraySource = CType(IIf(TypeOf g Is IManualTotalSummaryArraySource, g, Nothing), IManualTotalSummaryArraySource)
            For Each ci As ChangedFieldInfo In Me.ChangedFieldsArray
                Dim mt As ManualTotalSummary = tsa.GetManualTotalSummaryArray()(ci.FieldIndex)
                If Not mt Is Nothing Then
                    mt.ApplyDelta(r, isObsoleteRecord, isAddedRecord, ci)
                End If
                Next ci
                g = g.ParentGroup
            Loop
        End If
    End Sub
End Class
```

## API Reference

### Properties

- **TotalSummaries**  
  Type: `ArrayList`  
  Represents the collection of total summaries.

### Methods

- **OnRecordChanged**  
  Parameters:  
  - `r` (Element): The Element that has been changed.  
  - `isObsoleteRecord` (Boolean): Indicates whether the record is obsolete.  
  - `isAddedRecord` (Boolean): Indicates whether the record is added.

  Description:  
  This method is overridden to handle changes to the records and update the total summaries accordingly.

- **ApplyDelta**  
  Parameters:  
  - `r` (Element): The Element that has been changed.  
  - `isObsoleteRecord` (Boolean): Indicates whether the record is obsolete.  
  - `isAddedRecord` (Boolean): Indicates whether the record is added.  
  - `ci` (ChangedFieldInfo): The ChangedFieldInfo.

  Description:  
  Applies the delta changes to the total summary.

## Code Examples

### Example: Using ManualTotalSummaryTable

```vb
Dim tableDescriptor As New TableDescriptor()
Dim parentRelationTable As New Table()
Dim manualTable As New ManualTotalSummaryTable(tableDescriptor, parentRelationTable)

' Add records and handle changes
' Example of handling record changes
manualTable.OnRecordChanged(record, isObsolete, isAdded)
```

## Additional Notes

- The `ManualTotalSummaryTable` class inherits from `GridTable` and provides functionality for managing and updating total summaries for Grid records.

## Cross References

- Refer to the documentation on `GridTable` for more information on grid-related functionalities.

<!-- tags: [inner grid, .NET, Total Summary, ManualTotalSummaryTable, GridTable] keywords: [totalSummaries, OnRecordChanged, ApplyDelta, ManualTotalSummary, GridTable] -->
```