```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_003.jpeg
document_name: PivotGrid
page_number: 003
page_id: PivotGrid#page_003
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:52:37Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Overview
- **Exporting Pivot Grid to Excel, Word, and PDF**: This section explains how to export PivotGrid data into Excel, Word, and PDF formats.
- **Print Option**: Provides details on the printing functionality of the PivotGrid control.

## Content

### Exporting Pivot Grid to Excel, Word, and PDF
1. **Overview**: Learn how to export data from PivotGrid to Excel, Word, and PDF formats effortlessly.
2. **Process**: Step-by-step guide to configuring and executing the export operations.
3. **Features**: Overview of features supported during the export process, such as formatting and data details.

### Print Option
1. **Overview**: Understanding the printing capabilities of the PivotGrid control.
2. **Configuration**: Instructions on setting up printing options for the PivotGrid.
3. **Usage**: Examples and best practices for utilizing the print options effectively.

## API Reference

### Methods
- **ExportToExcel()**: Exports the PivotGrid data to an Excel format.
- **ExportToWord()**: Exports the PivotGrid data to a Word document.
- **ExportToPdf()**: Exports the PivotGrid data to a PDF format.
- **Print()**: Triggers the printing of the PivotGrid content.

## Code Examples

### Exporting to Excel
```csharp
// C# Example
PivotGridControl pivotGrid = new PivotGridControl();
pivotGrid.ExportToExcel("output.xlsx");
```

### Print Option Usage
```csharp
// C# Example
PivotGridControl pivotGrid = new PivotGridControl();
pivotGrid.Print();
```

## Cross References
See also: **Getting Started with PivotGrid**, **Data Binding in PivotGrid**, **Performance Optimization in PivotGrid**

<!-- tags: [pivotgrid, export, print, windowsforms, syncfusion] keywords: [exporting, printing, windowsforms, pivotgrid, pdf, excel, word] -->
```