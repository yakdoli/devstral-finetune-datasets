```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_085.jpeg
document_name: Olap Common
page_number: 085
page_id: Olap Common#page_085
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:39Z
fidelity: lossless
-->

## Overview

- Implements functionality to execute OLAP reports with various parameters.
- Closes the provider connection after report execution.
- Demonstrates both C# and VB.NET implementations.
- Utilizes `Syncfusion.OlapSilverlight.Common.SerializableDictionary` for returning results.
- Includes handling for levels and total count in reports.

## Content

### C#

```csharp
return resultSet;
}

/// <summary>
/// Executes the olap report with total count.
/// </summary>
/// <param name="report">The report.</param>
/// <returns></returns>
public Syncfusion.OlapSilverlight.Common.SerializableDictionary<string, object>
ExecuteOlapReportWithTotalCount(OlapReport report)
{
    Syncfusion.OlapSilverlight.Common.SerializableDictionary<string, object>
    dict = this._dataManager.ExecuteOlapReportWithTotalCount(report);
    // Closing the Provider Connection
    this._dataManager.DataProvider.CloseConnection();
    return dict;
}
}
#endregion
```

### VB.NET

```vb
[VB]

<AspNetCompatibilityRequirements(RequirementsMode := _ 
AspNetCompatibilityRequirementsMode.Allowed)> _
<ServiceBehavior(IncludeExceptionDetailInFaults := True)> _
Public Class OlapManager
    Implements IOlapDataProvider

#Region "Member"
    Private ReadOnly _dataManager As OlapDataProvider
#End Region

#Region "Constructor"
    Public Sub New()
        _dataManager = New OlapDataProvider("DataSource=localhost;Initial Catalog=Adventure Works DW")
    End Sub
#End Region

#Region "IOLapDataProvider Members"

    Public Function ExecuteOlapReportWithLevelsTypeAll(ByVal report As OlapReport, ByVal showLevelsTypeAll As Boolean) As CellSet
        Dim cellSet As CellSet = 
        _dataManager.ExecuteOlapReportWithLevelsTypeAll(report, showLevelsTypeAll)
        _dataManager.DataProvider.CloseConnection()
        Return cellSet
    End Function
```

### Explanation

- **C# Implementation**:
  - The `ExecuteOlapReportWithTotalCount` method executes an OLAP report with the specified report object and returns a dictionary containing the results.
  - It ensures that the provider connection is closed after the report execution.
  
- **VB.NET Implementation**:
  - The `OlapManager` class implements the `IOlapDataProvider` interface.
  - The constructor initializes the `_dataManager` with a connection to a data source.
  - The `ExecuteOlapReportWithLevelsTypeAll` method executes the report and returns a `CellSet` object, also closing the provider connection after execution.

## API Reference

### Class: `OlapManager`

#### Methods

- **`ExecuteOlapReportWithTotalCount(OlapReport report)`**
  - **Parameters**:
    - `report`: The report to execute.
    - Type: `OlapReport`
  - **Returns**:
    - A `SerializableDictionary<string, object>` containing the results of the OLAP report.
  - **Description**:
    - Executes the OLAP report with the specified total count and closes the provider connection after execution.

- **`ExecuteOlapReportWithLevelsTypeAll(OlapReport report, Boolean showLevelsTypeAll)`**
  - **Parameters**:
    - `report`: The report to execute.
    - Type: `OlapReport`
    - `showLevelsTypeAll`: A boolean indicating whether to show all levels.
    - Type: `Boolean`
  - **Returns**:
    - A `CellSet` containing the results of the OLAP report.
  - **Description**:
    - Executes the OLAP report with the specified parameters and closes the provider connection after execution.

### Namespace: `Syncfusion.OlapSilverlight.Common`

- **SerializableDictionary<TKey, TValue>**
  - A dictionary that can be serialized, used to store key-value pairs of results from OLAP reports.

## Code Examples

### C# Example

```csharp
// Example usage of ExecuteOlapReportWithTotalCount
OlapReport report = new OlapReport();
var result = olapManager.ExecuteOlapReportWithTotalCount(report);
// Handle the result dictionary
```

### VB.NET Example

```vb
' Example usage of ExecuteOlapReportWithLevelsTypeAll
Dim report As New OlapReport()
Dim cellSet As CellSet = olapManager.ExecuteOlapReportWithLevelsTypeAll(report, True)
' Handle the CellSet result
```

<!-- tags: [Syncfusion, OLAP, WinForms, Report, OLAP Silverlight, SerializableDictionary] keywords: [execute, report, total count, levels, provider connection, close, dictionary, cellset, data provider, data manager, olap report] -->
```