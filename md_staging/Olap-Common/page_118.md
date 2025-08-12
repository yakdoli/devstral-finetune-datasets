```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_118.jpeg
document_name: Olap Common
page_number: 118
page_id: Olap Common#page_118
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:52Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Describes the instantiation and usage of the `OlapDataProvider` in a WinForms application.
- Details executing `OlapReport` and `MDX Query` to retrieve CellSet data.
- Demonstrates connection management and closing the provider connection.

## Content

### WinForms-specific conventions
This section focuses on the instantiation and methods to execute reports and MDX queries using the `OlapDataProvider`.

```vb
Public Sub New()
    Dim connectionString As String = "DataSource=localhost;Initial Catalog=Adventure Works DW"
    ' Instantiating the OlapDataProvider with connection string
    dataManager = New OlapDataProvider(connectionString)
End Sub
```

#### Region "OlapDataProvider Members"

##### Executing the CellSet by passing OlapReport
```vb
''' <summary>
''' Executing the CellSet by passing OlapReport
''' </summary>
''' <param name="report">The report.</param>
''' <returns></returns>
Public Function ExecuteOlapReport(ByVal report As Syncfusion.OlapSilverlight.Reports.OlapReport) As Syncfusion.OlapSilverlight.Data.CellSet
    Dim cellSet As Syncfusion.OlapSilverlight.Data.CellSet = Me.dataManager.ExecuteOlapReport(report)
    ' Closing the provider connection
    Me.dataManager.DataProvider.CloseConnection()
    Return cellSet
End Function
```

##### Executing the CellSet by passing MDX Query
```vb
''' <summary>
''' Executing the CellSet by passing MDX Query
''' </summary>
''' <param name="mdxQuery">The MDX query.</param>
''' <returns> The CellSet </returns>
Public Function ExecuteMdxQuery(ByVal mdxQuery As String) As Syncfusion.OlapSilverlight.Data.CellSet
    Dim cellSet As Syncfusion.OlapSilverlight.Data.CellSet = Me.dataManager.ExecuteMdxQuery(mdxQuery)
    'Closing the provider connection.
    Me.dataManager.DataProvider.CloseConnection()
    Return cellSet
End Function
```

## API Reference

### Namespace: `Syncfusion.OlapSilverlight`

#### Class: `OlapDataProvider`

##### Methods
- **ExecuteOlapReport**:
  - **Parameters**:
    - `report` (Type: `OlapReport`): The report to execute.
  - **Returns**: `CellSet`
  - **Description**: Executes the given `OlapReport` and returns the CellSet data.

- **ExecuteMdxQuery**:
  - **Parameters**:
    - `mdxQuery` (Type: `String`): The MDX query to execute.
  - **Returns**: `CellSet`
  - **Description**: Executes the given MDX query and returns the CellSet data.

## Code Examples (multi-language supported)
The provided code examples illustrate how to:
- Instantiate the `OlapDataProvider` with a connection string.
- Execute an `OlapReport` or an `MDX Query` to retrieve data.
- Properly manage the connection and close it after execution.

## Page-level Navigation/TOC (if applicable)
- [title/heading not visible - replace with actual TOC content if applicable]

## Cross References
See also:
- [Cross-references to related sections or pages if present]

## RAG Annotations
<!-- tags: [Syncfusion Winforms, OlapDataProvider, OlapReport, MDX Query, CellSet] keywords: [connectionString, OlapDataProvider, OlapReport, ExecuteOlapReport, ExecuteMdxQuery, CellSet, CloseConnection] -->
```
