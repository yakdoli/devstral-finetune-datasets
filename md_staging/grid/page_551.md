```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_551.jpeg
document_name: grid
page_number: 551
page_id: grid#page_551
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:24:04Z
fidelity: lossless
-->

### Essential Grid for Windows Forms

```vb
dr = table.NewRow()
dr("FirstName") = "Sue"
dr("LastName") = "Gaskins"
table.Rows.Add(dr)

dr = table.NewRow()
dr("FirstName") = "John"
dr("LastName") = "Jacobs"
table.Rows.Add(dr)

dr = table.NewRow()
dr("FirstName") = "Sam"
dr("LastName") = "Garfunkel"
table.Rows.Add(dr)

dr = table.NewRow()
dr("FirstName") = "George"
dr("LastName") = "Shepherd"
table.Rows.Add(dr)

dr = table.NewRow()
dr("FirstName") = "Becky"
dr("LastName") = "Dunsford"
table.Rows.Add(dr)

Return table
End Function
```

### 4.2.2.3 Accessing Values in the Grid Data Bound Grid and in the Data Source
To access values in the Grid Data Bound Grid, use the indexer and retrieve the value from the GridStyleInfo object.

#### Code Examples

##### [C#]
```csharp
// Get value at (row, col).
object myValue = this.gridDataBoundGrid1[row, col].CellValue;
```

##### [VB.NET]
```vb
' Get Value at (row, col).
```

## Footer

- © 2013 Syncfusion. All rights reserved. | 551
```
```