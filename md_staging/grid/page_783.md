```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_783.jpeg
document_name: grid
page_number: 783
page_id: grid#page_783
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:40:04Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
' Show Filter Bar for the child tables.
Me.gridGroupingControl1.NestedTableGroupOptions.ShowFilterBar = True

' Show Filter Bar for the groups.
Me.gridGroupingControl1.ChildGroupOptions.ShowFilterBar = True
```

**Note:** For more details, refer the following browser sample:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Filters and Expressions\Filter Bar Demo
```

## 4.3.4.3.4.2.2 Dynamic Filter

### Overview
- Dynamic Filter serves as a good replacement for the default Filter Bar, offering advanced filtering capabilities.
- It is an add-on feature for Essential Grid, based on the regular filter bar with additional provisions for dynamic filtering, user-friendliness, etc.

### Content

#### Key Features
- The dynamic filter can be used with Nested Tables and Nested Groups.
- Adds a Filter Button at the right-most corner of every Filter Bar Cell.
- The button drops down to show available comparative operators.
- Hovering any filter bar cell displays a filter icon, indicating whether a filter is applied.
- Allows viewing filter results as you type.
- Supports user-defined filter criteria.

#### Set up Dynamic Filter

The dynamic filter is defined in the `GridDynamicFilter` class, which exposes two public methods, `WireGrid` and `UnwireGrid`, to hook up and unhook the dynamic filter with the desired grid.

```csharp
GridDynamicFilter f = new GridDynamicFilter();
if (showDynamicFilter)
{
    f.WireGrid(gridGroupingControl1);
}
```

## API Reference

### Namespace: Syncfusion.Windows.Forms.Grid
- **Class**: `GridDynamicFilter`
  - **Methods**:
    - `WireGrid(GridControlBase grid)`: Hooks the dynamic filter to the grid.
    - `UnwireGrid()`: Unhooks the dynamic filter from the grid.

### Code Examples

```csharp
GridDynamicFilter filter = new GridDynamicFilter();
if (enableDynamicFilter)
{
    filter.WireGrid(gridControl);
}
else
{
    filter.UnwireGrid();
}
```

## Cross References

See also:
- [Essential Grid for Windows Forms Documentation](https://www.syncfusion.com/documentation/windowsforms/essentials-grid)
- [Dynamic Filtering in Essential Grid](https://www.syncfusion.com/kb/essentials-grid/dynamic-filter)

<!-- tags: [product: Essential Grid, module: Dynamic Filter, version: 11.4.0.26] keywords: [Dynamic Filter, GridDynamicFilter, Filter Bar, Nested Tables, Nested Groups, User-Defined Filter, Advanced Filtering] -->
```