```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_814.jpeg
document_name: grid
page_number: 814
page_id: grid#page_814
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:45:04Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- A tool for setting up foreign key lookups.
- Describes the `GridForeignKeyHelper` class and its usage.
- Guides users through the methods for establishing foreign key relationships.

## Content

### Note: For more details, refer the following browser sample:
```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Relations And Hierarchy\ForeignKey\Reference Demo
```

#### GridForeignKeyHelper

**GridForeignKeyHelper** is a helper class that makes it easy for users to use foreign key relations to do foreign key lookups. With this class available, users can easily hook up a foreign table by a single method call instead of going through all the steps described above.

The `GridForeignKeyHelper` class exposes a static method called `SetupForeignTableLookUp` that accepts grouping grid, main table, foreign table, main table column, foreign table value column, and foreign table display column and sets up the Foreign Key relation using these parameter values.

- **C#**
```csharp
string valueColInMainTable = "Country", valueColInForeignTable = "CountryCode", 
displayColInForeignTable = "CountryName";
GridForeignKeyHelper.SetupForeignTableLookUp(
    gridGroupingControl1, 
    valueColInMainTable, 
    countries, 
    valueColInForeignTable, 
    displayColInForeignTable);
```

- **VB.NET**
```vbnet
Dim valueColInMainTable As String = "Country", valueColInForeignTable As String = "CountryCode", 
displayColInForeignTable As String = "CountryName"
GridForeignKeyHelper.SetupForeignTableLookUp(
    gridGroupingControl1, 
    valueColInMainTable, 
    countries, 
    valueColInForeignTable, 
    displayColInForeignTable)
```

### 4.3.4.3.5.3 Foreign Key KeyWords Relation

`ForeignKeyKeyWords` is a unique relation kind which is offered by the grouping engine. It is a foreign key relation where matching keys in the columns of the parent and child table define a relationship between the two tables. This is an m:n relation. Field summaries of the related child table can be referenced using a `.` dot in the `FieldDescriptor.MappingName` of the main table.

This relation kind allows you to have multi-valued columns in the grid.

## API Reference (if applicable)

This section includes information about the namespace, methods, properties, and events relevant to the `GridForeignKeyHelper` class.

- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Class:** GridForeignKeyHelper
- **Method:** `SetupForeignTableLookUp`
  - **Parameters:**
    - `groupingGridControl`: The grid control where the foreign key relationship will be established.
    - `mainTable`: The main table.
    - `foreignTable`: The foreign table.
    - `mainTableColumn`: The column in the main table used for the foreign key.
    - `foreignTableValueColumn`: The value column in the foreign table.
    - `foreignTableDisplayColumn`: The display column in the foreign table.

## Code Examples (multi-language supported)

- **Setting up a Foreign Key Relationship in C#**
```csharp
// Example usage of GridForeignKeyHelper in a C# application
using Syncfusion.Windows.Forms.Grid;

string valueColInMainTable = "Country";
string valueColInForeignTable = "CountryCode";
string displayColInForeignTable = "CountryName";

GridForeignKeyHelper.SetupForeignTableLookUp(
    gridGroupingControl1,
    valueColInMainTable,
    countries,
    valueColInForeignTable,
    displayColInForeignTable);
```

- **Setting up a Foreign Key Relationship in VB.NET**
```vbnet
' Example usage of GridForeignKeyHelper in a VB.NET application
Imports Syncfusion.Windows.Forms.Grid

Dim valueColInMainTable As String = "Country"
Dim valueColInForeignTable As String = "CountryCode"
Dim displayColInForeignTable As String = "CountryName"

GridForeignKeyHelper.SetupForeignTableLookUp(
    gridGroupingControl1,
    valueColInMainTable,
    countries,
    valueColInForeignTable,
    displayColInForeignTable)
```

## Page-level Navigation/TOC (if applicable)

- GridForeignKeyHelper
- SetupForeignTableLookUp Method
- ForeignKeyKeyWords Relation

## Cross References

- Refer to the sample browser for more details and examples.
- See also: [Syncfusion Windows Forms Documentation](link to documentation)

<!-- tags: [syncfusion, winforms, grid, foreign key, lookup, helper, api, 11.4.0.26] keywords: [GridForeignKeyHelper, Foreign Key Lookup, C#, VB.NET, gridGroupingControl, FieldDescriptor.MappingName, multi-valued columns] -->
```
