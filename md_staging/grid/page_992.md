```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_992.jpeg
document_name: grid
page_number: 992
page_id: grid#page_992
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:54:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes the use of the "Customers Order Report" print feature within the Syncfusion Windows Forms framework.
- Provides a sample browser path for further details on the print functionality.
- Highlights advanced features of the Essential Grid for Windows Forms includes scaling columns to fit, showing headers and footers, and print preview options.

## Content

### Print Grid Demo

For more details, refer the following sample browser.

<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Print\Print Grid Demo

![Customers Order Report Print Preview](Print preview of the Customers Order Report)

#### Customers Order Report
The screenshot shows the print preview of the "Customers Order Report," showcasing various details including OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate, ShipVia, Freight, and Ship Name. Additionally, header and footer options are configured, ensuring proper presentation when printing.

**Figure 385: Header and Footer set for page to be Printed**

### 4.3.4.13 Advanced Features

#### Overview
This section discusses the following advanced features:

This section explores advanced features such as:

- **Grid Print Options**:
  - Include options for setting headers and footers.
  - Scale columns to fit into the printed page.

### Example of Grid Print Options Interface

The interface shown in the figure includes settings for:

- **Show Header and Footer**: Ensures that headers and footers are included in the printed output.
- **Scale Columns To Fit**: Adjusts the column widths to fit on the printed page.

Additionally, a **PrintPreview** button is available to preview the output before printing.

### Page-Level Navigation
This section follows the detailed explanation of this functionality within the larger context of Syncfusion's Windows Forms documentation.

## API Reference
- **Grid Print Options**:
  - `ShowHeaderAndFooter`: Boolean setting for displaying headers and footers in the print preview.
  - `ScaleColumnsToFit`: Boolean setting to adjust column widths to fit on the printed page.

## Code Examples
```csharp
// Example: Configuring Grid Print Options
gridModel.Grid.PrintOptions.ShowHeaderAndFooter = true;
gridModel.Grid.PrintOptions.ScaleColumnsToFit = true;
gridModel.ShowPrintPreview();
```

## Cross References
See also:
- [Sample Browser Path](<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Print\Print Grid Demo)
- Additional sections on grid customization and print features in the Syncfusion documentation.

<!-- tags: [Syncfusion, Windows Forms, Grid, Print, Demo, Customers Order Report] keywords: [OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate, ShipVia, Freight, ShipName, PrintPreview, HeaderFooter, ScaleColumnsToFit, AdvancedFeatures] -->
```