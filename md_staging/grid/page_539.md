```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_539.jpeg
document_name: grid
page_number: 539
page_id: grid#page_539
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:23:06Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Figure 209: Grid Data Bound Grid dragged from the toolbox onto the Form

The image shows a Windows Forms design window with a Grid Data Bound Grid dragged from the toolbox onto the form. The grid is displayed with a message indicating that the DataSource property should be set for preview.

---

### Steps for Configuring the Grid Data Bound Grid

1. **Size and position it.**
2. **Click the Smart tag, expand Choose DataSource combo box and click Add Project DataSource.**

### Explanation

This section describes the process of setting up a Grid Data Bound Grid in a Windows Forms application. The steps are:
1. **Size and position the grid**: After dragging the grid onto the form, resize and position it as needed.
2. **Configure the DataSource**: Click the Smart tag of the grid to access the DataSource configuration options. Expand the Choose DataSource combo box and select "Add Project DataSource" to bind the grid to a data source.

---

## API Reference

### Overview of Setting the DataSource

- **Property**: `DataSource`
- **Type**: `object`
- **Description**: Sets the data source for the grid, allowing it to bind to various data sources such as datasets, arrays, or other collections.
- **Default**: `null`
- **Required**: Yes

### Handling the BoundGrid Event

The `BoundGrid` control provides various events to handle data binding changes. For example, the `DataBindingComplete` event is triggered after the grid has finished binding to its data source.

#### Example: Handling DataBindingComplete Event
```csharp
private void Form_Load(object sender, EventArgs e)
{
    // Assuming the GridDataBoundGrid is named 'grid'
    grid.DataSource = yourDataSource; // Set your data source here
    grid.DataBindingComplete += grid_DataBindingComplete;
}

private void grid_DataBindingComplete(object sender, DataGridViewBindingCompleteEventArgs e)
{
    // Additional logic can be added here if needed
    MessageBox.Show("Data binding complete");
}
```

## Code Examples

### Example: Configuring Grid Data Bound Grid

```csharp
using System;
using System.Data;
using System.Windows.Forms;
using Syncfusion.Windows.Forms.Grid;

public partial class GridForm : Form
{
    public GridForm()
    {
        InitializeComponent();

        // Step 1: Size and position the grid
        grid1.Dock = DockStyle.Fill;

        // Step 2: Add event handler for DataSource binding completion
        grid1.DataSource = yourDataSource; // Replace with your actual data source
        grid1.DataBindingComplete += grid1_DataBindingComplete;
    }

    private void grid1_DataBindingComplete(object sender, DataGridViewBindingCompleteEventArgs e)
    {
        MessageBox.Show("Data binding complete");
    }
}
```

---

## Page-level Navigation/TOC

- [Grid Data Bound Grid Configuration](#grid-data-bound-grid-configuration)
- [Setting the DataSource Property](#setting-the-datasource-property)
- [Handling Data Binding Events](#handling-data-binding-events)

## Cross References

See also:
- [Syncfusion Grid Documentation](https://www.syncfusion.com/)
- [Windows Forms Data Binding Tutorial](https://docs.microsoft.com/windowsForms/data-binding)

---

<!-- tags: [Syncfusion, Windows Forms, Grid, Data Binding, DataSource] keywords: [GridDataBoundGrid, DataSource, DataBindingComplete, Windows Forms, Syncfusion Grid] -->
```