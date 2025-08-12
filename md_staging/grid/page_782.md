```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_782.jpeg
document_name: grid
page_number: 782
page_id: grid#page_782
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:43:01Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Editing Filter Conditions using the RecordFilterDescriptor Collection Editor

Figure 314: Editing Filter Conditions by using the RecordFilterDescriptor Collection Editor

#### NestedTables and NestedGroups

AutoFilterRow can also be added to the nested tables and groups. To turn on the Filter Bar for the Nested Tables, set the property ShowFilterBar under NestedTableGroupOptions. For all the groups, ShowFilterBar under ChildGroupOptions need to be set to true.

```csharp
// Show Filter Bar for the child tables.
this.gridGroupingControl.NestedTableGroupOptions.ShowFilterBar = true;

// Show Filter Bar for the groups.
this.gridGroupingControl.ChildGroupOptions.ShowFilterBar = true;
```

```vb
[VB.NET]
```

## API Reference (if applicable)
- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Class:** GridGroupingControl
- **Members:**
  - **Property:** NestedTableGroupOptions
    - Property: ShowFilterBar (Type: bool)
  - **Property:** ChildGroupOptions
    - Property: ShowFilterBar (Type: bool)

## Code Examples

### C# Example
```csharp
// Configure Filter Bar for nested tables and groups
this.gridGroupingControl.NestedTableGroupOptions.ShowFilterBar = true;
this.gridGroupingControl.ChildGroupOptions.ShowFilterBar = true;
```

### VB.NET Example
```vb
' Configure Filter Bar for nested tables and groups
gridGroupingControl.NestedTableGroupOptions.ShowFilterBar = True
gridGroupingControl.ChildGroupOptions.ShowFilterBar = True
```

### Cross References
- See also: Filter Bar configuration for main tables and regular groups.

### RAG Annotations
<!-- tags: [winforms, grid, filter, nestedtables, nestedgroups, essentialgrid] keywords: [nested tables, nested groups, filter bar, grid grouping control, showfilterbar, configuration, auto filter row, grid, essential grid for windows forms] -->
```