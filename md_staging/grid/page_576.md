```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_576.jpeg
document_name: grid
page_number: 576
page_id: grid#page_576
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:25:16Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains how the `ShowTreeLines` property affects the visual representation of hierarchical data in the grid.
- Demonstrates expanding and collapsing nodes using the `ExpandAll` and `CollapseAll` methods.

## Content

### Hierarchical Grid with Tree Lines
When the `ShowTreeLines` property is set to `true`, there is no separate column allotted for the plus/minus buttons. Instead, the indented text in the first column is displayed.

#### Figure: Hierarchical Grid with Tree Lines
The figure shows a hierarchical grid with tree lines:

| ParentName       | parentID | ParentDec |
|------------------|----------|-----------|
| ChildName        | childID  | ParentID  |
| GrandChildName   | grandChildI | ChildID  |
| GreatGrandChildN | greatGrand | GrandChildID |
| GreatGreatGrandC | greatGreat | GreatGrandC |
| parentName0      | 0        | desc0     |
| \+ ChildName5    | 5        | 0         |
| \+ ChildName7    | 7        | 0         |
| \+ ChildName17   | 17       | 0         |
| parentName1      | 1        | desc1     |
| \+ ChildName9    | 9        | 1         |
| \+ ChildName11   | 11       | 1         |
| \+ ChildName18   | 18       | 1         |
| parentName2      | 2        | desc2     |
| parentName3      | 3        | desc3     |
| parentName4      | 4        | desc4     |

> **Figure 226: Hierarchical Grid with Tree Lines**

A sample demonstrating this feature is available under the following sample installation path:

```bash
<Install Location>\Syncfusion\EssentialStudio\<Version Number>\Windows\Grid.Windows\Samples\2.0\Data Bound\Hierarchy\GDBG Tree Lines Demo
```

### ExpandAll and CollapseAll Methods

#### 1. ExpandAll
- **Description:** Using this method, the user can view the expanded nodes in the Grid Data Bound Grid, i.e., the parent, child, and subsequent sublevel nodes can be viewed.

##### Code Example: Setting ExpandAll Method for Grid Data Bound Grid
- **Language:** C#

```csharp
[C#]
```

## API Reference

### Methods
- **ExpandAll**:
  - **Description:** Expands all nodes in the Grid Data Bound Grid.
  - **Parameters:** None
  - **Returns:** None
  - **Example Usage:** See code example above.

- **CollapseAll**:
  - **Description:** Collapses all nodes in the Grid Data Bound Grid.
  - **Parameters:** None
  - **Returns:** None

## Cross References
- Related properties: `ShowTreeLines`
- Related samples: "GDBG Tree Lines Demo"

<!-- tags: [syncfusion, winforms, grid, essentialgrid, hierarchicaldata, showtreelines] keywords: [ExpandAll, CollapseAll, grid, data bound, hierarchical, tree lines, plusminus buttons, indentation, sample, installation path] -->
```