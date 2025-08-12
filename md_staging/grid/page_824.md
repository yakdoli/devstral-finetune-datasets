```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_824.jpeg
document_name: grid
page_number: 824
page_id: grid#page_824
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:42:47Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to create and add a USStates object to a SourceListSet.
- Explains the process of creating a datatable with a column of type Country.
- Shows code examples in both C# and VB.NET for implementation.

## Content

### Implementing USStates in SourceListSet

1. **Create an object of USStates and add this object into the SourceListSet with a lookup name.**

#### C#
```csharp
CountriesCollection countries = 
    CountriesCollection.CreateDefaultCollection();
this.gridGroupingControl.Engine.SourceListSet.Add("Countries", countries);
```

#### VB.NET
```vb
Dim countries As CountriesCollection = 
    CountriesCollection.CreateDefaultCollection()
Me.gridGroupingControl.Engine.SourceListSet.Add("Countries", countries)
```

### Creating a DataTable with a Country Column

2. **Create a datatable with one of the columns is of type Country.**

#### C#
```csharp
DataTable table = new DataTable();
table.Columns.Add("Id", typeof(string));
table.Columns.Add("Country", typeof(Country));

// Adding Rows.
```

## Cross References
- Refer to the documentation on `CountriesCollection` for more details on its usage.
- See the GridGroupingControl API for additional methods and properties.

<!--
tags: [Grid, Windows Forms, SourceListSet, CountriesCollection, USStates, DataTable, Country, C#, VB.NET, API Reference] 
keywords: [Add, Countries, CreateDefaultCollection, Engine, SourceListSet, DataTable, Country, Columns, Rows]
-->
``` 
