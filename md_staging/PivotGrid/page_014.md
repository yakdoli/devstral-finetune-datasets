```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_014.jpeg
document_name: PivotGrid
page_number: 014
page_id: PivotGrid#page_014
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:17Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

```csharp
{
    // Specifying the ItemSource for Pivot Grid
    this.PivotGridControl.ItemsSource = ProductSales.GetSalesData();

    // Adding Pivot Rows to Grid
    this.PivotGridControl.PivotRows.Add(new PivotItem { FieldMappingName = "Product", TotalHeader = "Total" });
    this.PivotGridControl.PivotRows.Add(new PivotItem { FieldMappingName = "Year", TotalHeader = "Total" });

    // Adding Pivot Columns to Grid
    this.PivotGridControl.PivotColumns.Add(new PivotItem { FieldMappingName = "Country", TotalHeader = "Total" });
    this.PivotGridControl.PivotColumns.Add(new PivotItem { FieldMappingName = "State", TotalHeader = "Total" });

    // Adding Pivot Calculations to Grid
    this.PivotGridControl.PivotCalculations.Add(new PivotComputationInfo { FieldName = "Amount", Format = "C", SummaryType = SummaryType.DoubleTotalSum });
    this.PivotGridControl.PivotCalculations.Add(new PivotComputationInfo { FieldName = "Quantity", Format = "#,#0" });
}
```

### [VB]

```vb
Protected Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    ' Specifying the ItemSource for Pivot Grid
    Me.PivotGridControl1.ItemSource = ProductSales.GetSalesData()

    ' Adding Pivot Rows to Grid
    Me.PivotGridControl1.PivotRows.Add(New PivotItem With {.FieldMappingName = "Product", .TotalHeader = "Total"})
    Me.PivotGridControl1.PivotRows.Add(New PivotItem With {.FieldMappingName = "Year", .TotalHeader = "Total"})

    ' Adding Pivot Columns to Grid
    Me.PivotGridControl1.PivotColumns.Add(New PivotItem
```

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.PivotGrid
- **Class**: PivotGridControl
  - **Properties**:
    - `ItemSource`: Specifies the data source for the Pivot Grid.
    - `PivotRows`: Collection of `PivotItem` for rows.
    - `PivotColumns`: Collection of `PivotItem` for columns.
    - `PivotCalculations`: Collection of `PivotComputationInfo` for calculations.
  - **Methods**:
    - `Add(PivotItem)`: Adds a pivot item to the collection.
    - `GetSalesData()`: Retrieves sales data.

## Code Examples

### C#

```csharp
this.PivotGridControl.ItemsSource = ProductSales.GetSalesData();
this.PivotGridControl.PivotRows.Add(new PivotItem { FieldMappingName = "Product", TotalHeader = "Total" });
this.PivotGridControl.PivotRows.Add(new PivotItem { FieldMappingName = "Year", TotalHeader = "Total" });
this.PivotGridControl.PivotColumns.Add(new PivotItem { FieldMappingName = "Country", TotalHeader = "Total" });
this.PivotGridControl.PivotColumns.Add(new PivotItem { FieldMappingName = "State", TotalHeader = "Total" });
this.PivotGridControl.PivotCalculations.Add(new PivotComputationInfo { FieldName = "Amount", Format = "C", SummaryType = SummaryType.DoubleTotalSum });
this.PivotGridControl.PivotCalculations.Add(new PivotComputationInfo { FieldName = "Quantity", Format = "#,#0" });
```

### VB

```vb
Me.PivotGridControl1.ItemSource = ProductSales.GetSalesData()
Me.PivotGridControl1.PivotRows.Add(New PivotItem With {.FieldMappingName = "Product", .TotalHeader = "Total"})
Me.PivotGridControl1.PivotRows.Add(New PivotItem With {.FieldMappingName = "Year", .TotalHeader = "Total"})
Me.PivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldMappingName = "Country", .TotalHeader = "Total"})
Me.PivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldMappingName = "State", .TotalHeader = "Total"})
Me.PivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Amount", .Format = "C", .SummaryType = SummaryType.DoubleTotalSum})
Me.PivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Quantity", .Format = "#,#0"})
```

<!-- tags: [pivotgrid, windowsforms, itemsource, pivotrows, pivotcolumns, pivotcalculations, syncfusion, winforms, 11.4.0.26] keywords: [pivot grid, item source, pivot rows, pivot columns, pivot calculations, sales data, product, year, country, state, amount, quantity, format, summary type] -->
```