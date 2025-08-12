```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_964.jpeg
document_name: grid
page_number: 964
page_id: grid#page_964
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:52:25Z
fidelity: lossless
-->

# Grid Grouping Data

## Overview
- Demonstrates how to group data columns using the Syncfusion Winforms Grid control.
- Provides an example of grid customization with grouping and exporting functionalities.
- Features the use of a "PDF Export Demo" interface to export grid data to PDF format.

## Content

### Data Grid Example

The grid showcases a table of products with various attributes such as ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, and UnitPrice.

#### Sample Data
| ProductID | ProductName               | SupplierID | CategoryID | QuantityPerUnit               | UnitPrice |
|-----------|---------------------------|------------|------------|--------------------------------|-----------|
| 1         | Chai                      | 1          | 1          | 10 boxes x 20 bags            | 18        |
| 2         | Chang                     | 1          | 1          | 24 - 12 oz bottles           | 19        |
| 3         | Aniseed Syrup             | 1          | 2          | 12 - 550 ml bottles          | 10        |
| 4         | Chef Anton's Cajun Seasoning | 2          | 2          | 48 - 6 oz jars               | 22        |
| 5         | Chef Anton's Gumbo Mix    | 2          | 2          | 36 boxes                     | 21.35     |
| 6         | Grandma's Boysenberry Spread | 3          | 2          | 12 - 8 oz jars              | 25        |
| 7         | Uncle Bob's Organic Dried Pears | 3          | 7          | 12 - 1 lb pkgs.            | 30        |
| 8         | Northwoods Cranberry Sauce | 3          | 2          | 12 - 12 oz jars             | 40        |
| 9         | Mishi Kobe Niku           | 4          | 6          | 18 - 500 g pkgs.            | 97        |
| 10        | Ikura                     | 4          | 8          | 12 - 200 ml jars            | 31        |
| 11        | Queso Cabrales           | 5          | 4          | 1 kg pkg.                   | 21        |
| 12        | Queso Manchego La Pastora | 5          | 4          | 10 - 500 g pkgs.            | 38        |
| 13        | Konbu                     | 6          | 8          | 2 kg box                    | 6         |
| 14        | Tofu                      | 6          | 7          | 40 - 100 g pkgs.            | 23.25     |
| 15        | Genen Shouyu              | 6          | 2          | 24 - 250 ml bottles         | 15.5      |
| 16        | Pavlova                   | 7          | 3          | 32 - 500 g boxes            | 17.45     |
| 17        | Alice Mutton              | 7          | 6          | 20 - 1 kg tins              | 39        |
| 18        | Carnarvon Tigers          | 7          | 8          | 16 kg pkg.                  | 62.5      |
| 19        | Teatime Chocolate Biscuits | 8          | 3          | 10 boxes x 12 pieces        | 9.2       |
| 20        | Sir Rodney's Marmalade    | 8          | 3          | 30 gift boxes               | 81        |

#### Features
- **Grouping**: Users can drag a column header to group data by that column.
- **PDF Export**: An option to export the grid data to a PDF file.
- **Header & Footer**: Options to show or hide headers and footers in the exported PDF.
- **Margins**: Adjust margins for left, right, top, and bottom of the PDF.

### Export Options
- **Header Footer**:
  - Show Header: Checked
  - Show Footer: Checked
- **Margin**:
  - Left: 1
  - Right: 1
  - Top: 1
  - Bottom: 1

#### Button
- **Export to PDF**: A button to initiate the export process.

## API Reference

This section provides a reference for the grid features and APIs used in this example.

### Key Features
- **Grouping**: `Drag a column header here to group by that column.`
- **PDF Export**: `Export to PDF` functionality to save grid data.

### Interface Interactive Elements
- **Header Footer**:
  - Show Header
  - Show Footer

- **Margin Adjustment**:
  - Left, Right, Top, and Bottom margins can be adjusted for PDF export.

### Developer Notes
- Ensure that the grid is properly configured for grouping and export functionalities.
- Customize headers, footers, and margins as per the application's requirements.

## Code Examples

#### Sample C# Code for Exporting Grid Data to PDF
```csharp
using Syncfusion.Windows.Forms.Grid;
using Syncfusion.Pdf.Grid;

// Assuming gridControl is your Syncfusion Grid control
GridPdfExport pdfExport = new GridPdfExport();
pdfExport.Export(gridControl);
pdfExport.Save(FILEPATH);
```

## Conclusion
This example illustrates how to use the Syncfusion Winforms Grid control to group data and export it to a PDF format. The grid provides options for customization, including grouping, header/footer inclusion, and margin adjustment, making it versatile for various data visualization needs.

## Cross References
- Refer to the documentation on Grid Grouping for more details on configuring and customizing grouped data.
- See the PDF Export section in the Winforms Grid documentation for additional export options and configurations.

<!-- tags: [grid, grouping, pdf-export, winforms, syncfusion-sdk] -->
<!-- keywords: [grouping data, pdf export, winforms grid, header footer, margin adjustment, grid customization, data visualization] -->
```