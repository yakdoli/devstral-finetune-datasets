```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_584.jpeg
document_name: grid
page_number: 584
page_id: grid#page_584
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:25:58Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates initialization and manipulation of the Essential Grid with a large dataset.
- Focuses on the performance aspects of loading a grid with 20,000 records.
- Provides details on optimizing performance using options such as OptimizedListChanged, ResizeToFit, and ScrollWindow.

```markdown
## Grid Data Bound Grid

For more details, refer to the sample under the following path from the sample browser:

```
<Install Location>\Syncfusion\EssentialStudio\<Version Number>\Windows\Grid.Windows\Samples\2.0\Data Bound\Grid Performance Demo
```

### Overview

## Example

The Grid can be loaded by specifying the number of records and using the options: Use OptimizedListChangeEvent, Use ResizeToFit on ColWidths, and Use DataTableList.

## Content

### Initialize Table Group Box

#### Figure 235: Grid Data Bound Grid

The image shows a window各界面 labeled **GDBG Performance Demo** with the following components:

1. **Grid Data Display**:
   - A grid displays records with columns labeled **Name**, **State**, and **Zip**.
   - The records are populated with sample data such as **Name00000**, **South Carolina**, **45**, and so on.

2. **Initialize Table**:
   - Options to set **RecordCount** to **20000** and **Zip Count** to **100**.
   - Checkboxes for:
     - **Use OptimizedListChangeEvent**
     - **Use ResizeToFit on ColWidths**
     - **Use DataTableList**
   - Buttons for:
     - **Load Grid**
     - **Reset Grid**
     - **Information**

3. **Manipulate Grid**:
   - Options to set **Repeat Count** to **300** and **Batch Size** to **50**.
   - A checkbox for **Use ScrollWindow**.
   - Buttons for:
     - **Remove Records**
     - **Insert Records**
     - **Change Records**
     - **Change Names**

4. **Results**:
   - Outputs performance metrics:
     - **OptimizedListChanged=True**, **DataTableList=False**, **Autosize=False**, **ScrollWindow=True**
     - **Fill Datatable: 00:00:00.3593750**
     - **Set data source and categorize: 00:00:00.9375000**
     - **Repaint/Sizing: 00:00:01.2343750**
     - **Total time: 00:00:02.5312500**
     - **Total Row Count: 20000**
     - **Process’s physical memory usage: 39530 kb**

### WinForms-specific conventions
- The grid is used to bind data and manage a large number of records efficiently.
- Performance optimizations are highlighted, showing how to speed up data loading, categorization, and rendering.

### Code Examples
C# Example to load the grid:
```csharp
GridControl grid = new GridControl();
grid.RecordCount = 20000;
grid.ZipCount = 100;
grid.UseOptimizedListChangeEvent = true;
grid.UseResizeToFitOnColWidths = false;
grid.UseDataTableList = false;
grid.UseScrollWindow = true;
```

## API Reference
- **Namespace**: Syncfusion.Windows.Forms
- **Class**: GridControl
- **Properties**:
  - RecordCount: Sets the number of records.
  - ZipCount: Sets the number of zip codes.
  - UseOptimizedListChangeEvent: Boolean to optimize list change events.
  - UseResizeToFitOnColWidths: Boolean to resize columns to fit.
  - UseDataTableList: Boolean to use a DataTableList for data binding.
  - UseScrollWindow: Boolean to scroll the window.

## Code Examples
- Demonstrates configuring the grid to handle performance optimizations.
- Provides methods to manipulate the grid and observe the performance metrics.

## Cross References
- Refer to the Grid Performance Demo for detailed implementation examples and further optimizations.

## RAG Annotations
<!-- tags: [Essential Grid, Windows Forms, performance optimization, data binding, record count, scroll window, optimization options, large dataset, Grid Performance Demo] keywords: [GridControl, RecordCount, ZipCount,OptimizedListChangeEvent, ResizeToFit, DataTableList, ScrollWindow, large data set, data grid, sample browser, version number] -->
```