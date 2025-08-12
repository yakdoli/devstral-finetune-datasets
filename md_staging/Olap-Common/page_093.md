```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_093.jpeg
document_name: Olap Common
page_number: 093
page_id: Olap Common#page_093
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:29Z
fidelity: lossless
-->

# Essential OlapCommon

OlapDataManager will accept the MDX query in the string format through any one of this and process the data based on the query. Once the connection is established you can pass the MDX query in string format.

The following code will illustrate the passing of the MXD query as input:

### [C#]

```csharp
OlapDataManager olapDataManager = new OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW");
string mdxQuery =
@"SELECT NON EMPTY ({{Hierarchy. ( [DrilldownLevel(( [Customer].[Customer Geography].[All Customers] ) ) ) } } * 
{ [MEASURES].[Internet Sales Amount]}}) dimension properties member_type ON COLUMNS, NON EMPTY ({{Hierarchy. ( 
[DrilldownLevel(({ [Date].[Fiscal].[All Periods]} ) ) ) } ) } } ) 
dimension properties member_type ON ROWS
FROM [Adventure Works] CELL PROPERTIES 
VALUE, FORMAT_STRING, FORMATTED_VALUE";
olapDataManager.MdxQuery = mdxQuery;
olapDataManager.ExecuteCellSet();
```

### [VB]

```vb
Dim olapDataManager As OlapDataManager = New 
OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW") 
Dim mdxQuery As String = "SELECT NON EMPTY ({{Hierarchy. ( [DrilldownLevel(( [Customer].[Customer Geography].[All Customers] ) ) ) } } * 
{ [MEASURES].[Internet Sales Amount]}}) dimension properties member_type ON COLUMNS, NON EMPTY ({{Hierarchy. ( 
[DrilldownLevel(({ [Date].[Fiscal].[All Periods]} ) ) ) } ) } ) } ) 
dimension properties member_type ON ROWS
FROM [Adventure Works]     CELL PROPERTIES 
VALUE, FORMAT_STRING, FORMATTED_VALUE"
olapDataManager.MdxQuery = mdxQuery
olapDataManager.ExecuteCellSet()
```

This will accept the MDX query as a string and assign it to the OlapDataManager's mdxQuery property and invoke the data process.

<!-- tags: [Olap Common, OlapDataManager, MDX, Query, C#, VB] keywords: [OlapDataManager, MDX, Query, Connection, Data Processing] -->
```