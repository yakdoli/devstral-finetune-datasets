```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_898.jpeg
document_name: grid
page_number: 898
page_id: grid#page_898
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:50:40Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how `VisibleColumns` can be rearranged using Drag and Drop features.
- Explains the functionality of `StackedHeaders` for handling nested groups within a grid.

## Content

### StackedHeaders for NestedGroups
Stacked Headers can be enabled for Child Groups by setting `ChildGroupOptions.ShowStackedHeaders` to `true`. The grouping grid in the example displays stacked headers for nested groups.

#### Figure 357: VisibleColumns rearranged as a result of the above Drag / Drop

| ContactTitle         | Address                     | City         | Country   | CustomerID | CompanyName             |
|----------------------|-----------------------------|--------------|-----------|------------|-------------------------|
| Sales Representative | Obere Str. 57              | Berlin       | Germany   | ALFKI      | Alfreds Futterkiste    |
| Owner                | Avda. de la Constitución 222 | Mexico D.F. | Mexico    | ANATR      | Ana Trujillo Emparedado |
| Owner                | Mataderos 2312             | Mexico D.F.  | Mexico    | ANTON      | Antonio Moreno Taquería  |
| Sales Representative | 120 Hanover Sq.            | London       | UK        | AROUT      | Around the Horn         |
| Order Administrator   | Berguvsvägen 8            | Luleå        | Sweden    | BERGS      | Berglunds snabbköp      |
| Sales Representative | Forsterstr. 57             | Mannheim     | Germany   | BLAUS      | Blauer See Delikatessen |
| Marketing Manager    | 24, place Kléber           | Strasbourg   | France    | BLONP      | Blondel père et fils    |
| Owner                | C/ Araquil, 67             | Madrid       | Spain     | BOLID      | Bólido Comidas preparad |
| Owner                | 12, rue des Bouchers        | Marseille    | France    | BONAP      | Bon app’                |
| Accounting Manager   | 23 Tsawassen Blvd.         | Tsawassen    | Canada    | BOTTM      | Bottom-Dollar Markets   |
| Sales Representative | Fauntleroy Circus           | London       | UK        | BSBEV      | B’s Beverages           |

**StackedHeaders for NestedGroups**

Stacked Headers can be enabled for `Child Group` by setting `ChildGroupOptions.ShowStackedHeaders` to `true`. The grouping grid in the example image displays the stacked headers for the nested groups.

#### Figure 358: Stacked Headers for Nested Groups

| Key                 | Description                                                |
|---------------------|------------------------------------------------------------|
| Stacked Headers for Top Level Group                  | Header 1, Header 2, Stacked Header Row 2 |
| Stacked Headers for Child Group                     | Header 1, Header 2, Stacked Header Row 2 |

### Appearance

The visual layout effectively showcases the grid's columns and headers with stacked headers for nested groups, ensuring a clear and organized display.

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: GridControl
- **Properties**: `ChildGroupOptions.ShowStackedHeaders`
- **Unions**: `VisibleColumns`, `StackedHeaders`

## Code Examples
Example of enabling Stacked Headers for Child Groups:
```csharp
gridControl1.ChildGroupOptions.ShowStackedHeaders = true;
```

## Cross References
See also:
- [Stacked Headers Documentation](#stacked-headers-doc)
- [Grid Grouping Documentation](#grid-grouping-doc)

<!-- tags: [essential-grid, windows-forms, stacked-headers, nested-groups] keywords: [visiblecolumns, drag and drop, grid group, child group, grid control, stacked headers, nested groups, windows forms] -->
```