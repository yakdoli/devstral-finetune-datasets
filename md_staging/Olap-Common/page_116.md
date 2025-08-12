```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_116.jpeg
document_name: Olap Common
page_number: 116
page_id: Olap Common#page_116
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:39Z
fidelity: lossless
-->

# Essential `OlapCommon`

## Overview
- This class provides methods to execute OLAP reports and MDX queries for retrieving data from a data source.
- It includes handling connection management and executing queries or reports to obtain `CellSet` results.

## Content

### `OlapManager` Constructor

```csharp
/// <summary>
/// Initializes a new instance of the <see cref="OlapManager"/> class.
/// </summary>
public OlapManager()
{
    string connectionString = "DataSource=localhost;Initial Catalog=Adventure Works DW";

    // Instantiating the OlapDataProvider with connection string.
    dataManager = new OlapDataProvider(connectionString);
}
```

### `ExecuteOlapReport` Method

```csharp
/// <summary>
/// Executes the CellSet by passing an OlapReport.
/// </summary>
/// <param name="report">The report.</param>
/// <returns>The CellSet</returns>
public Syncfusion.OlapSilverlight.Data.CellSet ExecuteOlapReport(Syncfusion.OlapSilverlight.Reports.OlapReport report)
{
    Syncfusion.OlapSilverlight.Data.CellSet cellSet = this.dataManager.ExecuteOlapReport(report);

    // Closing the provider connection.
    this.dataManager.DataProvider.CloseConnection();

    return cellSet;
}
```

### `ExecuteMdxQuery` Method

```csharp
/// <summary>
/// Executes the CellSet by passing an MDX Query.
/// </summary>
/// <param name="mdxQuery">The MDX query.</param>
/// <returns>The CellSet</returns>
public Syncfusion.OlapSilverlight.Data.CellSet ExecuteMdxQuery(string mdxQuery)
{
    Syncfusion.OlapSilverlight.Data.CellSet cellSet = this.dataManager.ExecuteMdxQuery(mdxQuery);
}
```

## API Reference

### `OlapManager`
- **Methods:**
  - `ExecuteOlapReport(Syncfusion.OlapSilverlight.Reports.OlapReport report)`: Executes a report and returns a `CellSet`.
  - `ExecuteMdxQuery(string mdxQuery)`: Executes an MDX query and returns a `CellSet`.

### Parameters
- `report`: The `OlapReport` object used for executing the report.
- `mdxQuery`: The MDX query as a string.

### Returns
- `CellSet`: A structured collection of data representing the result of the report or query.

## Code Examples

### Example: Executing an OLAP Report
```csharp
OlapManager manager = new OlapManager();
OlapReport report = new OlapReport();
// Configure report parameters here...
CellSet result = manager.ExecuteOlapReport(report);
// Process the result...
```

### Example: Executing an MDX Query
```csharp
OlapManager manager = new OlapManager();
string mdxQuery = "SELECT ..."; // Define your MDX query here
CellSet result = manager.ExecuteMdxQuery(mdxQuery);
// Process the result...
```

## Cross References
- Refer to the `OlapDataProvider` and `OlapReport` classes for more information on how they work with `OlapManager`.

<!-- tags: [product, module, control, api, version?] keywords: [Olap, MDX, Query, CellSet, OlapReport, Data, WinForms] -->
```