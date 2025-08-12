```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_792.jpeg
document_name: grid
page_number: 792
page_id: grid#page_792
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:40:52Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The implementation includes the following classes.

- GroupingGridFilterBarExt - It derives a custom filter bar cell type named FilterByDisplayMemberCell and use this cell type in the place of default filter bar cell.
- GridFilterByDisplayMemberCellModel - This is the cell model class that loads the filter drop down with the display strings of the respective filter bar column and creates cell renderer.
- GridFilterByDisplayMemberCellRenderer - This is the cell renderer class that sets up the actual filter string by replacing the display string with the value string.

## Using Custom Filter

### Enabling/Disabling

Following code example illustrates how to enable/disable this custom filter.

```csharp
// Enable filter.
GroupingGridFilterBarExt gGFilter = new GroupingGridFilterBarExt();
gGFilter.WireGrid(gridGroupingControl);

// Disable filter.
gGFilter.UnwireGrid(gridGroupingControl);
```

```vb
' Enable filter.
Dim gGFilter As GroupingGridFilterBarExt = New GroupingGridFilterBarExt()
gGFilter.WireGrid(gridGroupingControl)

' Disable filter.
gGFilter.UnwireGrid(gridGroupingControl)
```

<!-- tags: [Essential Grid, Windows Forms, custom filter, grouping, cell model, renderer, filter bar] keywords: [custom filter, filter bar, display strings, renderer class, enable/disable] -->
``` 
