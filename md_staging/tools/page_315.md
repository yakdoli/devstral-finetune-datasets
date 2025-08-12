```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_315.jpeg
document_name: tools
page_number: 315
page_id: tools#page_315
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:05:49Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Demonstrates how to populate and use AutoComplete in WinForms with embedded data using a DataTable.
- Shows an example of adding rows to a DataTable and setting it as a data source for an AutoComplete control.
- Includes both C# and VB.NET code examples.

## Content

### Example Code in C#

```csharp
dt.Rows.Add(new object[] { "North Carolina " });
dt.Rows.Add(new object[] { "India " });
dt.Rows.Add(new object[] { "New York " });
dt.Rows.Add(new object[] { "Washington " });
dt.Rows.Add(new object[] { "London" });
dt.Rows.Add(new object[] { "Canada" });
autoCompletel.DataSource = dt;

private void button1_Click(object sender, System.EventArgs e)
{
    dt.Rows.Add(new object[] { "new1" });
    dt.Rows.Add(new object[] { "new2" });

    // sets the internal table data based on the AutoComplete.DataSource property.
    this.autoCompletel.SetTableData();
}
```

### Example Code in VB.NET

```vb
Private dt As DataTable

Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    dt = New DataTable("select")
    dt.Columns.Add("Countries")
    dt.Columns.Add("states")
    dt.Rows.Add(New Object() { "North Carolina " })
    dt.Rows.Add(New Object() { "India " })
    dt.Rows.Add(New Object() { "New York " })
    dt.Rows.Add(New Object() { "Washington " })
    dt.Rows.Add(New Object() { "London" })
    dt.Rows.Add(New Object() { "Canada" })
    autoComplete1.DataSource = dt
End Sub

Private Sub button1_Click(ByVal sender As Object, ByVal e As System.EventArgs)
    dt.Rows.Add(New Object() { "new1" })
    dt.Rows.Add(New Object() { "new2" })
    Me.autoComplete1.SetTableData()
End Sub
```

### Explanation

- The `DataTable` object `dt` is initialized and populated with rows containing names of countries and cities.
- The `DataSource` property of the `AutoComplete` control is set to this `DataTable`.
- On button click, two new rows are added to the `DataTable`, and the `SetTableData` method is called to refresh the AutoComplete control with the updated data.

## Page-level Navigation/TOC (if applicable)
- This section provides a clear example of how to dynamically update and use AutoComplete functionality with embedded data in WinForms.
<!-- tags: [Windows Forms, AutoComplete, DataTable, C#, VB.NET] keywords: [AutoComplete, DataTable, WinForms, data source, button click, dynamic update] -->
```