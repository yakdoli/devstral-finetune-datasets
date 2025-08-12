```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_421.jpeg
document_name: grid
page_number: 421
page_id: grid#page_421
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:15:45Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

The calculations are done through the Grouping Engine, which is a part of Essential Grouping. The default calculation is Summation, but there exists an option to change the calculation type to Average, Median, Percentiles, Variances, Standard Deviations, and so on. You can also provide "custom" calculations through the grouping engine.

### Features

- Data-binding support
- Auto-calculation of Total Summary
- Filters
- Grouping support
- Customizable Appearance
- Support for XML and Binary Serialization

### APIs

Here is a brief explanation on some important methods implemented in the Pivot Grid.

- **CollapseAll()** - This will collapse all the expanded tables in the Pivot Grid.

    ```csharp
    pivotGridControl1.CollapseAll();
    ```

- **ExpandAll()** - Expands all the collapsed nodes in the Pivot Grid.

    ```csharp
    pivotGridControl1.ExpandAll();
    ```

- **InitSchema()** - A new Pivot schema will be created, and it will be associated with the Pivot Grid.

    ```csharp
    pivotGridControl1.InitSchema();
    ```

- **ResetSchema()** - Resets the Pivot Grid control into an initial schema which will be empty.

    ```csharp
    pivotGridControl1.ResetSchema();
    ```

<!-- tags: [Pivot Grid, Grouping Engine, Essential Grouping, Syncfusion Winforms] keywords: [Summation, Average, Median, Percentiles, Variances, Standard Deviations, Custom Calculations, Data-binding support, Auto-calculation, Filters, Grouping support, Customizable Appearance, XML Serialization, Binary Serialization, CollapseAll(), ExpandAll(), InitSchema(), ResetSchema()] -->
```