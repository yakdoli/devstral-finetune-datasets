```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_568.jpeg
document_name: grid
page_number: 568
page_id: grid#page_568
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:24:43Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- Details the SortBehaviour property's configuration options: SingleClick, DoubleClick, and None.
- Demonstrates single-click sorting functionality with sample code in C# and VB.NET.

### Content

Following is the list of options/values that can be assigned to the SortBehaviour property:

- **SingleClick**: Sort column when user clicks once.
- **DoubleClick**: Sort column when user double-clicks.
- **None**: No sorting when user clicks.

The following code example illustrates sorting of columns on a single click.

#### Code Examples

- **[C#]**

```csharp
this.gridDataBoundGrid1.SortBehavior = GridSortBehavior.SingleClick;
```

- **[VB.NET]**

```vb
Me.gridDataBoundGrid1.SortBehavior = GridSortBehavior.SingleClick
```

#### Visual Representation

Figure 222 displays the sorting functionality applied to the "Zip" column, as shown below:

![Figure 222: Sorting Column](attachment:Figure_222_Sorting_Column.png)

### 4.2.2.11 Sort by DisplayMember

#### Overview
- By default, sorting in a Grid Data Bound Grid is handled through the `IBindingList`.

#### Details
- Sorting is performed through the `IBindingList` interface, ensuring compatibility and functionality.

---

<!-- tags: [Syncfusion Winforms, Essential Grid, SortBehaviour, grid#page_568, DisplayMember, IBindingList] keywords: [SingleClick, DoubleClick, None, Grid Data Bound Grid, sorting, columns, C#, VB.NET] -->
```