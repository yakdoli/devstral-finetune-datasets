```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_582.jpeg
document_name: grid
page_number: 582
page_id: grid#page_582
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:26:03Z
fidelity: lossless
-->

## Overview
- Records can be displayed by typing in the NavigationBar.
- Grid Data Bound Grid is displayed within a Grid Record Navigation control.
- Demonstrates the use of multiple headers in Grid Data Bound Grid.

## Content

### Records Displayed in the Grid Data Bound Grid
A Grid Data Bound Grid is displayed within a Grid Record Navigation control, as shown in Figure 233. Records can be navigated and displayed by typing in the NavigationBar.

#### Figure 233: Records displayed in the Grid Data Bound Grid added to the Grid Record Navigation Control
The figure illustrates records displayed in a Grid Data Bound Grid, showcasing fields such as `CustomerID`, `CompanyName`, `ContactName`, `ContactTitle`, and `Address`.

| CustomerID | CompanyName | ContactName | ContactTitle | Address |
|------------|-------------|-------------|--------------|---------|
| ALFKI      | Alfreds Futterkiste | Maria Anders | Sales Representative | Obere Str. 57 |
| ANATR      | Ana Trujillo Emparedados y helados | Ana Trujillo | Owner | Avda. de la Constitución 2222 |
| ANTON      | Antonio Moreno Taquería | Antonio Moreno | Owner | Mataderos 2312 |
| AROUT      | Around the Horn | Thomas Hardy | Sales Representative | 120 Hanover Sq. |
| BERGS      | Berglunds snabbköp | Christina Berglund | Order Administrator | Berguvsvägen 8 |
| BLAUS      | Blauer See Delikatessen | Hanna Moos | Sales Representative | Forsterstr. 57 |
| BLONP      | Blondesddsl père et fils | Frédérique Citeaux | Marketing Manager | 24, place Kléber |
| BOLID      | Bólido Comidas preparadas | Martin Sommer | Owner | C/ Araquil, 67 |
| BONAP      | Bon app' | Laurence Lebihan | Owner | 12, rue des Bouchers |
| BOTTM      | Bottom-Dollar Markets | Elizabeth Lincoln | Accounting Manager | 23 Tsawassen Blvd. |
| BSBEV      | B's Beverages | Victoria Ashworth | Sales Representative | Fauntleroy Circus |
| CACTU      | Cactus Comidas para llevar | Patricio Simpson | Sales Agent | Cerrito 333 |
| CENTC      | Centro comercial Moctezuma | Francisco Chang | Marketing Manager | Sierras de Granada 9993 |
| CHOPS      | Chop-suey Chinese | Yang Wang | Owner | Hauptstr. 29 |
| COMMI      | Comércio Mineiro | Pedro Afonso | Sales Associate | Av. dos Lusiadas, 23 |

### 4.2.2.15 Multiple Headers

#### Overview
Grid Data Bound Grid supports the display of multiple row and column headers. Additional row headers can be added alongside the existing header by setting `Model.Rows.HeaderCount`, and additional column headers can be added below the existing column header by setting the `Model.Cols.HeaderCount` property.

#### Code Example
The following code example illustrates how to display multiple row and column headers:

```csharp
int extraRowHeaders = 1;
int extraColHeaders = 1;

// Initialize extra row and column headers.
this.gridDataBoundGrid1.Model.Rows.HeaderCount = extraRowHeaders;
this.gridDataBoundGrid1.Model.Cols.HeaderCount = extraColHeaders;
```

## API Reference

### Properties
- `Model.Rows.HeaderCount`: Specifies the number of row headers.
- `Model.Cols.HeaderCount`: Specifies the number of column headers.

### Methods
- `InitializeExtraRowAndColumnHeaders()`: Initializes additional row and column headers.

## Cross References
- See also: Grid Data Binding, Grid Navigation Controls

<!-- tags: [syncfusion, winforms, grid, data binding, navigation controls] keywords: [Grid Data Bound Grid, Grid Record Navigation, Multiple Headers, Model.Rows.HeaderCount, Model.Cols.HeaderCount, NavigationBar, records] -->
```