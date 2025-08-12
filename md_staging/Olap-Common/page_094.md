```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_094.jpeg
document_name: Olap Common
page_number: 094
page_id: Olap Common#page_094
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:33Z
fidelity: lossless
-->

## Essential OlapCommon

### Code Example: C# and VB

```csharp
[C#]
OlapDataManager olapDataManager = new OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW");
string mdxQuery =
@"SELECT NON EMPTY ({{Hierarchize({DrilldownLevel({[Customer].[Customer Geography].[All Customers]}})) * 
{[MEASURES].[Internet Sales Amount]}) dimension properties 
member_type ON COLUMNS, NON EMPTY ({{Hierarchize(
{DrilldownLevel({[Date].[Fiscal].[All Periods]}}))}} ) 
dimension properties member_type ON ROWS 
FROM [Adventure Works]   CELL PROPERTIES
VALUE, FORMAT_STRING, FORMATTED_VALUE";
olapDataManager.ExecuteCellSet(mdxQuery);
```

```vb
[VB]
Dim olapDataManager As OlapDataManager = New OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW")
Dim mdxQuery As String = "SELECT NON EMPTY ({{Hierarchize({DrilldownLevel({[Customer].[Customer Geography].[All Customers]}})) * 
{[MEASURES].[Internet Sales Amount]}) dimension properties 
member_type ON COLUMNS, NON EMPTY ({{Hierarchize(
{DrilldownLevel({[Date].[Fiscal].[All Periods]}}))}} ) 
dimension properties member_type ON ROWS 
FROM [Adventure Works]   CELL PROPERTIES
VALUE, FORMAT_STRING, FORMATTED_VALUE"
olapDataManager.ExecuteCellSet(mdxQuery)
```

### Sequential Diagram

**Sequential Diagram**

The following sequential diagram is matching when user gives input as MDX query:

---

> **Note:** The diagram is not included in this markdown representation.

---

## API Reference

### WinForms-specific Information
The provided code examples demonstrate the use of the `OlapDataManager` class to execute MDX queries in a Windows Forms application. The `ExecuteCellSet` method is used to retrieve the results of the MDX query as a cell set.

## Code Examples (C# and VB)
The code examples provided above illustrate how to connect to a data source, construct an MDX query, and execute it using the `OlapDataManager`. The MDX query retrieves non-empty members of the specified dimensions and measures, formatting the values appropriately.

## Cross References
- See also: [MDX Query Basics](#mdx-query-basics)
- See also: [OlapDataManager Class Reference](#olapdatamanager-class-reference)

<!-- tags: [OlapDataManager, MDXQuery, WinForms, Syncfusion, C#, VB] keywords: [olap, mdx, query, data manager, windows forms, cell set, non-empty members, dimensions, measures, formatted values] -->
```