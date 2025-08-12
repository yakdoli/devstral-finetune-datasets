```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_742.jpeg
document_name: grid
page_number: 742
page_id: grid#page_742
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:39:45Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the usage of foreign key relationships in a grid.
- Explains how to display the CustomerName column in the Foreign Table corresponding to the Customer column in the Main Table.
- Highlights the mechanism of matching values in the Customer column with CustomerID in the Foreign Table.

## Content

### Figure 296: Foreign-Key Relation

The following figure illustrates a grid with multiple columns and rows, showing data in a structured format:

- **Columns**: rID, CompanyName, ShipName, Customer.
- **Rows**: Contains various company and customer data detailed below.

#### Sample Data from the Grid

| rID    | CompanyName              | ShipName                  | Customer                        |
|--------|---------------------------|---------------------------|---------------------------------|
| 1031   | Folies gourmandes        | Peacock                   | Anabela Domingues              |
| 1036   | Wilman Kala              | Peacock                   | Anne Granger                   |
| 1027   | Ernst Handel             | White Clover Markets      | Catherine Dewey                |
| 1025   | Consolidated Holdings     | Wellington Importadora     | Eduardo Saaedra                |
| 1024   | Drachenblut Delikatessen  | Suprêmes délices          | Elizabeth Brown                 |
| 1020   | Antonio Moreno Taqueria   | Vins et alcools Chevalier | Frédérique Citeaux             |
| 1028   | Bon app'                  | White Clover Markets      | Helvetius Nagy                 |
| 1026   | Folies gourmandes        | Ottilies Käseladen:      | Janine Labrune                 |
| 1022   | Around the Horn           | Hanari Carnes             | Karl Jablonski                 |
| 1035   | Toms Spezialitäten        | Callahan                  | Karl Jablonski                 |
| 1021   | Berglunds snabbköp        | Toms Spezialitäten       | Laurence Lebihan               |
| 1033   | Let's Stop N Shop         | Dodsworth                 | Matti Karttunen                |
| 1029   | B's Beverages             | Buchanan                  | Palle Ibsen                    |
| 1037   | Wartian Herkku            | Leverling                 | Paula Parente                  |
| 1034   | QUICK-Stop                | Davolio                   | Pirkko Koskitalo               |
| 1030   | Folk och fä HB            | Suyama                    | Rita Müller                    |
| 1023   | Blauer See Delikatessen   | Victuailles en stock      | Victoria Ashworth              |
| 1032   | Eastern Connection        | Leverling                 | Zbyszek Piestrzeniewicz       |

In the figure above, the CustomerName column is displayed in the Foreign Table where a column named Customer is located in the Main Table. The Customer column holds key values that match the values in a column named CustomerID in the Foreign Table.

#### Sample Path

Refer to the following sample in our sample browser:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Sort\Sort By Display Member Demo
```

### 4.3.4.3.2.1 Enable or Disable Sorting

By default, the Grouping Grid supports automatic sorting. When you want to disable this automatic sorting, you can use the following methods to prevent sorting on specific columns.

#### Steps to Disable Sorting

1. Identify the specific columns for which sorting should be disabled.
2. Use the appropriate method or property to disable sorting for those columns.
3. Ensure that the changes are applied to the grid to reflect the intended behavior.

Note that this section outlines the general process without specific code examples. Additional details can be found in the full documentation or sample browser.

## API Reference (if applicable)
- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: GridControl

### Methods:
- `DisableSorting(columnIndex: int)`  
  - Disables sorting for the specified column index.
- `IsSortingEnabled(columnIndex: int)`  
  - Returns a boolean indicating whether sorting is enabled for the specified column index.

### Parameters
- `columnIndex`: The index of the column for which sorting is to be enabled or disabled.

#### Returns
- `boolean`: Indicates whether sorting is currently enabled for the specified column.

#### Exceptions
- `ArgumentOutOfRangeException`: If the columnIndex is out of range.

## Code Examples (multi-language supported)
- **C# Example**:
  ```csharp
  // Disable sorting for column with index 2
  gridControl.DisableSorting(2);
  ```

- **VB.NET Example**:
  ```vb.net
  ' Disable sorting for column with index 2
  gridControl.DisableSorting(2)
  ```

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, Grid, sorting, foreign key, customer, company, version: 11.4.0.26] keywords: [disable sorting, foreign key relation, customer name, company name, ship name, customer column, customer ID, automatic sorting] -->
```