```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_084.jpeg
document_name: Olap Common
page_number: 084
page_id: Olap Common#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:31Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
/// <returns></returns>
public CubeSchema GetCubeSchema(string cubeName)
{
    CubeSchema cubeSchema = _dataManager.GetCubeSchema(cubeName);
    _dataManager.DataProvider.CloseConnection();
    return cubeSchema;
}

/// <summary>
/// Gets the child members.
/// </summary>
/// <param name="memberUniqueName">Name of the member unique.</param>
/// <param name="cubeName">Name of the cube.</param>
/// <returns></returns>
public MemberCollection GetChildMembers(string memberUniqueName, string cubeName)
{
    MemberCollection childMembers = _dataManager.GetChildMembers(memberUniqueName, cubeName);
    _dataManager.DataProvider.CloseConnection();
    return childMembers;
}

/// <summary>
/// Gets the level members.
/// </summary>
/// <param name="levelUniqueName">Name of the level unique.</param>
/// <param name="cubeName">Name of the cube.</param>
/// <returns></returns>
public MemberCollection GetLevelMembers(string levelUniqueName, string cubeName)
{
    MemberCollection levelMembers = _dataManager.GetLevelMembers(levelUniqueName, cubeName);
    _dataManager.DataProvider.CloseConnection();
    return levelMembers;
}

/// <summary>
/// Executes the specified MDX query.
/// </summary>
/// <param name="mdxQuery">The MDX query.</param>
/// <returns></returns>
public object Execute(string mdxQuery)
{
    var resultSet = this._dataManager.Execute(mdxQuery);
    // Closing the Provider Connection
    _dataManager.DataProvider.CloseConnection();
}
```

## API Reference

### Methods

- `GetCubeSchema(string cubeName)`
  - **Returns**: `CubeSchema`
  - Retrieves the schema for a given cube.

- `GetChildMembers(string memberUniqueName, string cubeName)`
  - **Returns**: `MemberCollection`
  - Retrieves the child members for a specified member unique name within a cube.

- `GetLevelMembers(string levelUniqueName, string cubeName)`
  - **Returns**: `MemberCollection`
  - Retrieves the members for a specified level unique name within a cube.

- `Execute(string mdxQuery)`
  - **Returns**: `object`
  - Executes the specified MDX query and returns the result set.

### Parameters

- `cubeName`: The name of the cube to access.
- `memberUniqueName`: The unique name of the member to retrieve child members for.
- `levelUniqueName`: The unique name of the level to retrieve members for.
- `mdxQuery`: The MDX query to execute.

## Code Examples

### Example: Retrieving Cube Schema

```csharp
CubeSchema cubeSchema = OlapCommon.GetCubeSchema("SalesCube");
```

### Example: Retrieving Child Members

```csharp
MemberCollection childMembers = OlapCommon.GetChildMembers("Product.Category", "SalesCube");
```

### Example: Executing an MDX Query

```csharp
object resultSet = OlapCommon.Execute(
    "SELECT " +
    "    {[Measures].[Sales Amount]} ON COLUMNS, " +
    "    {[Product].[Category].Members} ON ROWS " +
    "FROM [SalesCube]"
);
```

<!-- tags: [product, OlapCommon, CubeSchema, MemberCollection, MDX Query, API Reference, Parameters, Methods, Code Examples] keywords: [cube schema, child members, level members, MDX execution, data retrieval, OOAP] -->
```