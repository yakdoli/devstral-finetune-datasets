```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_672.jpeg
document_name: grid
page_number: 672
page_id: grid#page_672
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:32:45Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the process of grouping records in Essential Grid.
- Highlights the efficient binding capabilities of the grid grouping control.
- Focuses on methods of data binding supported by the grid grouping control.

## Content

### Figure 271: Time Taken to Group the Records
The figure illustrates the speed at which records are grouped in the Essential Grid. The interface shows a grid with 50,000 items bound to an `IList`. The grouping operation completes in `00:00:00.0126958 Sec`, as indicated by a pop-up message that states, "Grouped in 00:00:00.0126958 Sec."

### 4.3.4.2 Data Binding

#### Overview of Data Binding
To display data, the grid grouping control must be bound to a data source. The grid supports various data sources, including:
- DataTables
- DataSets
- Any component that implements interfaces such as:
  - `IList`
  - `IBindingList`
  - `ITypedList`
  - `IListSource`

The data source can have multiple nested tables, which will be displayed hierarchically by the grid grouping control.

#### Data Binding Mechanisms
This section covers the different types of data binding mechanisms supported by the grid grouping control, as follows:
1. **Binding to DataTables and DataSets**: The grid can directly bind to `DataTables` and `DataSets`, providing a robust way to display relational data.
2. **Interface-Based Binding**: The grid supports binding to any component that implements interfaces like `IList`, `IBindingList`, `ITypedList`, or `IListSource`.
3. **Hierarchical Data Display**: Nested tables within the data source can be displayed in a hierarchical manner, allowing for structured and navigable display of complex data relationships.

## Page-level Navigation/TOC (if applicable)
- **Figure 271**: Time Taken to Group the Records
- **4.3.4.2 Data Binding**
  - Overview of Data Binding
  - Data Binding Mechanisms

## Cross References
- Related topics involving different types of data sources and their manipulation may be covered in earlier sections of the document.

<!-- tags: [essential-grid, windows-forms, data-binding, grid-grouping-control, performance, datatables, datasets, ilist, ibindinglist] keywords: [data grouping, data binding, performance benchmark, hierarchical data display, interface-based binding] -->
```