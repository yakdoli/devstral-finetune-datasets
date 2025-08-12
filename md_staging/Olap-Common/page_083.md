```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_083.jpeg
document_name: Olap Common
page_number: 083
page_id: Olap Common#page_083
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:42Z
fidelity: lossless
-->

## Essential OlapCommon

### Overview
- Provides methods to retrieve MDX queries, execute OLAP reports, and manage cube information.
- Helper functions to work with cube schemas and execute MDX queries.
- Includes documentation and comment blocks for clarity.

### Content

#### Methods

##### Retrieve MDX Query
**Method**: `GetMdxQuery(Syncfusion.OlapSilverlight.Reports.OlapReport report)`
- **Parameters**:
  - `report`: The report object.
- **Returns**: `string` representing the MDX query.
- **Description**: Retrieves the MDX query for the specified report and closes the provider connection.

##### Execute OLAP Report
**Method**: `ExecuteOlapReport(OlapReport report)`
- **Parameters**:
  - `report`: The report object.
- **Returns**: `CellSet` representing the executed cell set.
- **Description**: Executes the OLAP report, retrieves the cell set, and closes the provider connection.

##### Execute MDX Query
**Method**: `ExecuteMdxQuery(string mdxQuery)`
- **Parameters**:
  - `mdxQuery`: The MDX query to execute.
- **Returns**: `CellSet` representing the executed cell set.
- **Description**: Executes the MDX query, retrieves the cell set, and closes the provider connection.

##### Get Cubes
**Method**: `GetCubes()`
- **Returns**: `CubeInfoCollection` containing the cubes.
- **Description**: Retrieves the cubes and closes the provider connection.

##### Get Cube Schema
**Method**: `GetCubeSchema(string cubeName)`
- **Parameters**:
  - `cubeName`: Name of the cube.
- **Returns**: Cube schema information for the specified cube.
- **Description**: Retrieves the schema for the specified cube.

### API Reference

#### `GetMdxQuery`
```csharp
public string GetMdxQuery(Syncfusion.OlapSilverlight.Reports.OlapReport report)
{
    string mdxReturned = this._dataManager.GetMdxQuery(report);
    // Closing the Provider Connection
    this._dataManager.DataProvider.CloseConnection();
    return mdxReturned;
}
```

##### ExecuteOlapReport
```csharp
public CellSet ExecuteOlapReport(OlapReport report)
{
    CellSet cellSet = _dataManager.ExecuteOlapReport(report);
    _dataManager.DataProvider.CloseConnection();
    return cellSet;
}
```

##### ExecuteMdxQuery
```csharp
public CellSet ExecuteMdxQuery(string mdxQuery)
{
    CellSet cellSet = _dataManager.ExecuteMdxQuery(mdxQuery);
    _dataManager.DataProvider.CloseConnection();
    return cellSet;
}
```

##### GetCubes
```csharp
public CubeInfoCollection GetCubes()
{
    CubeInfoCollection cubes = _dataManager.GetCubes();
    _dataManager.DataProvider.CloseConnection();
    return cubes;
}
```

##### GetCubeSchema
```csharp
/// <summary>
/// /// Gets the cube schema.
/// <summary>
/// /// </summary>
/// /// <param name="cubeName">Name of the cube.</param>
```

## Code Examples

### Example: Retrieving MDX Query
```csharp
string mdxQuery = GetMdxQuery(report);
```

### Example: Executing OLAP Report
```csharp
CellSet cellSet = ExecuteOlapReport(report);
```

### Example: Executing MDX Query
```csharp
CellSet cellSet = ExecuteMdxQuery(mdxQuery);
```

### Example: Getting Cubes
```csharp
CubeInfoCollection cubes = GetCubes();
```

### Example: Getting Cube Schema
```csharp
GetCubeSchema(cubeName);
```

### See also:
- [OlapSilverlight.Reports.OlapReport](https://Syncfusion.Winforms.OlapSilverlight.Reports)
- [CellSet](https://Syncfusion.Winforms.Cells)
- [CubeInfoCollection](https://Syncfusion.Winforms.Cubes)
- [MDX Query Execution](https://Syncfusion.Winforms.MdxExecution)

<!-- tags: Syncfusion, Winforms, OlapSilverlight, Reports, OLAP, MDX, Queries, CubeInfoCollection, CellSet, ProviderConnection keywords: GetMdxQuery, ExecuteOlapReport, ExecuteMdxQuery, GetCubes, GetCubeSchema, CloseConnection, Olap Common -->
```