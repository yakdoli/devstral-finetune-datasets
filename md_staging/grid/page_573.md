```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_573.jpeg
document_name: grid
page_number: 573
page_id: grid#page_573
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:24:52Z
fidelity: lossless
-->

## Overview
- Demonstrates how to associate a filter string between a parent and child table.
- Provides code examples in both C# and VB.NET.
- Features a nested dropdown grid to visually illustrate the functionality.

## Content

### Parent-Child Table Filtering

The following code demonstrates how to provide filter strings between a parent table and a child table. This ensures that only relevant data is displayed in the child grid based on the selected row in the parent grid.

#### C#

```csharp
// Parent table to Child table.
private void ProvideOrdersFilterStrings(object sender, QueryFilterStringEventArgs e)
{
    if (this.customerGrid1.Model[e.Row, e.Column + 1].Text != "")
    {
        // Add 1 to get to Customer ID.
        e.FilterString = string.Format("CustomerID = '{0}'", 
            this.customerGrid1.Model[e.Row, e.Column + 1].Text);
    }
}
```

#### VB.NET

```vb.net
' Parent table to Child table.
Private Sub ProvideOrdersFilterStrings(ByVal sender As Object, ByVal e As QueryFilterStringEventArgs)
    If Me.customerGrid1.Model(e.Row, e.Column + 1).Text <> "" Then
        ' Add 1 to get to Customer ID.
        e.FilterString = String.Format("CustomerID = '{0}'", 
            Me.customerGrid1.Model(e.Row, e.Column + 1).Text)
    End If
End Sub
```

### Nested Drop-down Grids

The following image illustrates the concept of nested drop-down grids, where the selection in the parent grid dynamically filters the data displayed in the child grid.

#### Figure 224: Nested Drop-down Grids

![Nested Drop-down Grids](image_link)

**Description**: The top grid (parent) contains customer information, and the bottom grid (child) shows orders associated with the selected customer. When a customer is selected in the parent grid, the child grid updates to show only the orders related to that customer.

### Sample Demonstration

A sample demonstrating this feature is available under the following sample installation path.

```markdown
A sample demonstrating this feature is available under the following sample installation path.
```

### Notes

- Ensure the `customerGrid1` grid is correctly initialized and connected to the appropriate data source.
- The `e.FilterString` is essential to dynamically filter the child grid's data based on the selected row in the parent grid.

## Cross References

- For more information on grids and related controls, refer to the [Syncfusion WinForms Grid Controls Documentation](documentation_link).

<!-- tags: [syncfusion, winforms, grid, filter, sample, nested grid, child table, parent table] keywords: [parent table, child table, filter string, nested dropdown, customerid, orders, dynamic filtering, sample path] -->
```