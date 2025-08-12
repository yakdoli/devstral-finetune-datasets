```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_585.jpeg
document_name: grid
page_number: 585
page_id: grid#page_585
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:25:32Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- Use **OptimizedListChangeEvent** to ensure the grid data is updated using **IBindingList.ListChanged** instead of **CurrencyManager** change events.
- Use **ResizeToFit on ColWidths** to resize column width to fit the cell content after data is loaded.
- Use **DataTableList** to ensure **Syncfusion.Collections.DataTableWrapperList** is used as the data source instead of a regular data table, improving performance for large datasets.

### Grid Performance Tuning Options

#### Manipulate Grid group box
- **Repeat Count and Batch Size**: Specify these to check the performance in batch updates.
- **Use ScrollWindow**: This invalidates only inserted or removed rows instead of the entire grid, optimizing for large datasets.
- **Insert Records, Remove Records, and Change Records**: These buttons allow checking performance when modifying records in the underlying data table.

The results of these operations can be seen in the following example:

##### Example: Grid Performance Check
```plaintext
Results:
---------
OptimizedListChanged=True   DataTableList=False    Autosize=False    ScrollWindow=True
Fill Datatable: 00:00:00.3593750
Set data source and categorize: 00:00:00.9375000
Repaint/Sizing: 00:00:01.2343750
Total time: 00:00:02.5312500
Total Row Count 20000
Process's physical memory usage: 39530 kb
```

### 4.2.2.17 Events
The important events in Grid control and Grid Data Bound Grid are as follows.

#### Current Cell Related Events
- **CurrentCellAcceptedChanges**: Occurs when the grid accepts changes made to the active current cell.

## API Reference

### Events
- **CurrentCellAcceptedChanges**: Triggered when the grid accepts changes to the current active cell.

### Summary of Performance Features
- **OptimizedListChanged**: Enhances data update performance using **IBindingList.ListChanged**.
- **ResizeToFit**: Automatically resizes column widths to fit content.
- **DataTableList**: Improves performance for inserting records into large tables by using **TableWrapperList**.
- **ScrollWindow**: Optimize invalidation for inserted or removed rows, minimizing impact on larger datasets.

---

<!-- tags: [grid, windows forms, performance, syncfusion, version:11.4.0.26] keywords: [OptimizedListChangeEvent, ResizeToFit, DataTableWrapperList, ScrollWindow, CurrentCellAcceptedChanges] -->
```