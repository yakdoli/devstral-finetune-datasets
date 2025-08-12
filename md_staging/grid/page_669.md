```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_669.jpeg
document_name: grid
page_number: 669
page_id: grid#page_669
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:31:22Z
fidelity: lossless
-->

# `Essential Grid for Windows Forms`

## Overview
- Demonstrates the grouping performance in the Grid Grouping Control.
- Focuses on the optimization of grouping columns to improve performance.
- Explains the use of an `IList` bound to the `GridGroupingControl`.

## Content

### Figure 269: Checking the Grouping Performance in the Grid Grouping Control
The screenshot shows a `Grouping Performance` interface that allows users to initialize and manipulate a grid. The grid displays data grouped by state and zip code, with an example of states like South Carolina, Nevada, North Carolina, and Washington. To the right, there are options to configure grid settings such as record count, zip count, and sorting. Below the grid, detailed stats such as fill data time, set data source and categorize time, repaint time, and total load time are shown. The table record count is indicated as `20000`, matching the grid record count. The element count is displayed as `14907`. The physical memory usage is also noted as `76922 kb`.

#### Controls and Options
- **Initialize Table:**
  - `RecordCount`: `20000`
  - `Zip Count`: `100`
  - Options like `Sort and Categorize`, `Calculate Column Width`, `Use DataView Sort`, and `MultiThreading` are available.
  - Buttons for `Load Grid` and `Reset Grid` are present.
- **Manipulate Grid:**
  - `Repeat Count`: `300`
  - `Batch Size`: `50`
  - Option to `Use ScrollWindow`.
  - Buttons for `Remove Records`, `Insert Records`, `Change Records`, `Change Names`, `Collapse All`, and `Expand All`.

#### Results Section
The results section provides detailed timing information for various operations, including:
- `Fill Datatable`: `00:00:00.562500`
- `Set data source and categorize`: `00:00:02.4531250`
- `Repaint`: `00:00:01.125000`
- `Total time`: `00:00:04.1406250`
- Indications of `Table Record Count: 20000`, `Grid Record Count: 20000/20000`, and `Display Element Count: 14907`.
- Physical memory usage: `76922 kb`.

### 4.3.4.1.5 `IList Grouping Performance`
The `IList` bound to the `GridGroupingControl` has been implemented with an optimization process for grouping columns to enhance performance.

## API Reference (if applicable)
- **Namespace:**
  - `Syncfusion.Windows.Forms.Grid`
- **Class:**
  - `GridGroupingControl`
- **Properties/Methods/Events:**
  - `IList`: Bound to `GridGroupingControl` for grouping optimization.
  - `RecordCount`: Used for configuring the number of records.
  - `Zip Count`: Configurable parameter for grouping by zip code.
  - Various grouping methods such as sorting, categorizing, and column width calculation.

## Code Examples
No specific code examples are provided in this image.

## RAG Annotations
<!-- tags: [GridGroupingControl, IList, GroupingPerformance, Optimization, WindowsForms, Syncfusion, 11.4.0.26] keywords: [grouping performance, grid control, IList, record count, zip count, multi-threading, physical memory usage, performance optimization] -->
```