```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_086.jpeg
document_name: Olap Common
page_number: 086
page_id: Olap Common#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:58Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Provides methods to execute OLAP reports and MDX queries.
- Handles connection management for data providers.
- Supports retrieving cube information, schemas, and member collections.

## Content

### WinForms-specific Conventions
The following functions are part of the `OlapCommon` class and are used to interact with OLAP data.

#### Functions

##### GetMdxQuery
```vb
Public Function GetMdxQuery(ByVal report As Syncfusion.OlapSilverlight.Reports.OlapReport) As String
    Dim mdxReturned As String = Me._dataManager.GetMdxQuery(report)
    Me._dataManager.DataProvider.CloseConnection()
    Return mdxReturned
End Function
```

##### ExecuteOlapReport
```vb
Public Function ExecuteOlapReport(ByVal report As OlapReport) As CellSet
    Dim cellSet As CellSet = _dataManager.ExecuteOlapReport(report)
    _dataManager.DataProvider.CloseConnection()
    Return cellSet
End Function
```

##### ExecuteMdxQuery
```vb
Public Function ExecuteMdxQuery(ByVal mdxQuery As String) As CellSet
    Dim cellSet As CellSet = _dataManager.ExecuteMdxQuery(mdxQuery)
    _dataManager.DataProvider.CloseConnection()
    Return cellSet
End Function
```

##### GetCubes
```vb
Public Function GetCubes() As CubeInfoCollection
    Dim cubes As CubeInfoCollection = _dataManager.GetCubes()
    _dataManager.DataProvider.CloseConnection()
    Return cubes
End Function
```

##### GetCubeSchema
```vb
Public Function GetCubeSchema(ByVal cubeName As String) As CubeSchema
    Dim cubeSchema As CubeSchema = _dataManager.GetCubeSchema(cubeName)
    _dataManager.DataProvider.CloseConnection()
    Return cubeSchema
End Function
```

##### GetChildMembers
```vb
Public Function GetChildMembers(ByVal memberUniqueName As String, ByVal cubeName As String) As MemberCollection
    Dim childMembers As MemberCollection = _dataManager.GetChildMembers(memberUniqueName, cubeName)
    _dataManager.DataProvider.CloseConnection()
    Return childMembers
End Function
```

##### GetLevelMembers
```vb
Public Function GetLevelMembers(ByVal levelUniqueName As String, ByVal cubeName As String) As MemberCollection
    Dim levelMembers As MemberCollection = _dataManager.GetLevelMembers(levelUniqueName, cubeName)
    _dataManager.DataProvider.CloseConnection()
    Return levelMembers
End Function
```

##### Execute
```vb
Public Function Execute(ByVal mdxQuery As String) As Object
    Dim resultSet As var = Me._dataManager.Execute(mdxQuery)
    _dataManager.DataProvider.CloseConnection()
    Return resultSet
End Function
```

## API Reference

### Methods

#### GetMdxQuery
- **Parameters**: `report` (Syncfusion.OlapSilverlight.Reports.OlapReport)
- **Returns**: String (MDX query string)

#### ExecuteOlapReport
- **Parameters**: `report` (OlapReport)
- **Returns**: CellSet (Result set of the OLAP report)

#### ExecuteMdxQuery
- **Parameters**: `mdxQuery` (String)
- **Returns**: CellSet (Result set of the MDX query)

#### GetCubes
- **Returns**: CubeInfoCollection (Collection of available cubes)

#### GetCubeSchema
- **Parameters**: `cubeName` (String)
- **Returns**: CubeSchema (Schema of the specified cube)

#### GetChildMembers
- **Parameters**: `memberUniqueName` (String), `cubeName` (String)
- **Returns**: MemberCollection (Collection of child members)

#### GetLevelMembers
- **Parameters**: `levelUniqueName` (String), `cubeName` (String)
- **Returns**: MemberCollection (Collection of members at the specified level)

#### Execute
- **Parameters**: `mdxQuery` (String)
- **Returns**: Object (Result of the executed MDX query)

<!-- tags: [WinForms, OLAP, MDX, Cube, Schema, Member, DataProvider, Connection] keywords: [GetMdxQuery, ExecuteOlapReport, ExecuteMdxQuery, GetCubes, GetCubeSchema, GetChildMembers, GetLevelMembers, Execute] -->
```