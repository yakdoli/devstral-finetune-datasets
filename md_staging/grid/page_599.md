```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_599.jpeg
document_name: grid
page_number: 599
page_id: grid#page_599
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:27:11Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to bind a Grid Grouping control to a manual data source in Windows Forms.
- Walks through creating a DataTable, populating it with data, and attaching it to the grid grouping control.

## Content

### Adding Manual Data to DataTable
```csharp
myDataRow("id") = i
myDataRow("item") = "item " & i
myDataTable.Rows.Add(myDataRow)
```

### Binding the Grid Grouping Control

1. **Set the DataSource property**:
   ```csharp
   this.gridGroupingControl.DataSource = myDataTable;
   ```
   ```vb.net
   Me.GridGroupingControl1.DataSource = myDataTable
   ```

2. **Add the Grid Grouping Control to the Form**:
   ```csharp
   this.Controls.Add(this.gridGroupingControl);
   ```
   ```vb.net
   Me.Controls.Add(Me.GridGroupingControl1)
   ```

3. **Behavior upon execution**:
   - When the application runs, the grid will appear as shown in the following image.
   - Users can sort the data by clicking the header of the desired column.

   ![Figure 241: Binding a Grid Grouping control to a Manual Data Source](attachment://grid_manual_data_source.png)

   **Figure 241: Binding a Grid Grouping control to a Manual Data Source**

### Conclusion
This section illustrates the process of manually adding data to a DataTable and binding it to a Grid Grouping control in a Windows Forms application. The example demonstrates essential steps such as creating and populating the data source, assigning the data source to the grid, and adding the grid to the form.

## Code Examples

### C#.NET
```csharp
// Populating DataTable
myDataRow("id") = i
myDataRow("item") = "item " & i
myDataTable.Rows.Add(myDataRow)

// Binding DataSource
this.gridGroupingControl.DataSource = myDataTable;

// Adding Grid to Form
this.Controls.Add(this.gridGroupingControl);
```

### VB.NET
```vb.net
' Populating DataTable
myDataRow("id") = i
myDataRow("item") = "item " & i
myDataTable.Rows.Add(myDataRow)

' Binding DataSource
Me.GridGroupingControl1.DataSource = myDataTable

' Adding Grid to Form
Me.Controls.Add(Me.GridGroupingControl1)
```

## API Reference

### Properties
- **DataSource**: Sets the data source for the GridGroupingControl.
### Methods
- **Rows.Add**: Adds rows to the DataTable.
### Events
- **DataSourceChanged**: Triggered when the data source changes.

## Related Topics
- [Binding GridGroupingControl to a Database](#)
- [Sorting and Filtering Data in GridGroupingControl](#)

<!-- tags: [Syncfusion, WinForms, GridGroupingControl, DataTable, DataBinding] keywords: [data binding, grid grouping control, manual data source, Windows Forms] -->
```