```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_085.jpeg
document_name: calculate
page_number: 085
page_id: calculate#page_085
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:53Z
fidelity: lossless
-->

# Zero-Based and One-Based Indexing in Essential Calculate

## Overview

- The second convention involves zero-based and one-based indexing.
- Discusses the conflict between zero-based indexing in data sources and one-based indexing in CalcEngine to mimic Excel.
- Highlights the need to ensure consistency in index usage.
- Explains the requirement for one-based indexing in Essential Calculate.
- Illustrates tweaking indexes for consistency with zero-based data sources.

## Content

### Zero-Based and One-Based Indexing

The second convention in Essential Calculate involves the use of zero-based and one-based indexing. It is important to note that many data sources utilize zero-based indexing for accessing values. However, in the CalcEngine, one-based indexing is employed to emulate Excel's behavior. This can lead to potential conflicts when dealing with indexing. To maintain consistency and ensure clarity on which indexing should be used, Essential Calculate mandates that all indexes (including rows and column integer values) should be one-based. This may necessitate adjustments to the indexes passed through ICalcData methods and event arguments to align them with any zero-based data sources in use. One example discussed in this section is the DataGrid, where you can observe the index-based adjustments in the following code samples:

```csharp
[C#]

public class CalcDataGrid : DataGrid, Syncfusion.Calculate.ICalcData
{
    public CalcDataGrid() : base()
    {
        // Avoid the complexity of sorting.
        this.AllowSorting = false;
    }

    // Used to subscribe to the DataTable.ColumnChanged event. This ColumnChanged event will raise the required ValueChanged event.
    // Without this ValueChanged event, the CalcEngine would have no knowledge of the data.
    public void WireParentObject()
    {
        // Assumes grid's datasource is a DataTable.
        DataTable dt = this.DataSource as DataTable;
        dt.ColumnChanged += new DataColumnChangeEventHandler(dt_ColumnChanged);

        // Avoids the complexity of a new row.
        dt.DefaultView.AllowNew = false;
    }

    // This event handler raises the required ICalcData.ValueChanged event when the data in the DataTable changes.
    private void dt_ColumnChanged(object sender, DataColumnChangeEventArgs e)
    {
        CurrencyManager cm = (CurrencyManager)this.BindingContext[this.DataSource, this.DataMember];
        DataTable dt = this.DataSource as DataTable;
        int pos = cm.Position;
        int field = dt.Columns.IndexOf(e.Column);
        string val = this[pos, field].ToString();
    }
}
```

## API Reference (if applicable)

### WinForms-specific conventions

- The code block provided demonstrates how to manage zero-based indexing by converting it to one-based indexing using event handling mechanisms.

### Methods

- `CalcDataGrid()`: Constructor for the `CalcDataGrid` class, initializing without sorting complexity.
- `WireParentObject()`: Method to subscribe to the `DataTable.ColumnChanged` event.
- `dt_ColumnChanged()`: Event handler to manage data changes and trigger the required `ICalcData.ValueChanged` event.

## Code Examples (multi-language supported)

The provided C# example showcases the implementation of handling `DataTable` changes and ensuring one-based indexing for compatibility with the `CalcEngine`.

## RAG Annotations

<!-- tags: [essential-calculate, data-sources, calcengine, indexing, syncfusion-winform, data-grid, event-handling] keywords: [zero-based, one-based, indexing, conflict, compatibility, calcengine, datagrid, dataSource, eventhandler, icalcdata, valuechanged] -->
```