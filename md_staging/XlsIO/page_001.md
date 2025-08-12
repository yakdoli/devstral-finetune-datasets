```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_001.jpeg
document_name: XlsIO
page_number: 001
page_id: XlsIO#page_001
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:48:20Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Comprehensive guide to using Essential XlsIO in Syncfusion Winforms applications
- Focus on handling Excel documents in .NET applications with ease
- Detailed explanations and examples for XlsIO functionalities

## Content

### What is Essential XlsIO?

Essential XlsIO is a powerful component designed for reading, writing, and modifying Excel files in .NET applications. It is part of Syncfusion's portfolio of tools aimed at enhancing productivity and providing innovative solutions for developers. Essential XlsIO enables developers to work with Excel spreadsheets programmatically, allowing them to automate repetitive tasks and integrate Excel functionality seamlessly into their applications.

### Key Features of Essential XlsIO

- **High Performance**: Efficient parsing and generation of Excel files for fast processing of large datasets.
- **Rich API**: Extensive set of functionalities that allow developers to manipulate Excel files without the need for Microsoft Office Excel.
- **Platform Support**: Works across different .NET platforms including Windows Forms, WPF, ASP.NET, and more.
- **Flexibility**: Supports various Excel file formats such as .xlsx, .xls, and .xlsm.
- **Customization**: Offers extensive control over almost every aspect of Excel documents, including formatting, formulas, charts, pivot tables, and more.

### Getting Started

To start using Essential XlsIO in your Syncfusion Winforms application, follow these steps:

1. **Download and Install**: Ensure you have the required version of Essential XlsIO (v.11.4.0.26) from the Syncfusion website.
2. **NuGet Installation**: Install the Essential XlsIO package from NuGet using the command:
   ```bash
   NuGet install Syncfusion.XlsIO.Netcore
   ```
3. **Set Up References**: Add the necessary references in your project.

### Basic Usage Example

Here is a simple example demonstrating how to create and save an Excel file using Essential XlsIO:

```csharp
using Syncfusion.XlsIO;

// Create a new Workbook instance
using (IWorkbook workbook = new Workbook())
{
    IWorksheet worksheet = workbook.Worksheets[0];

    // Add some data to the worksheet
    worksheet["A1"].Text = "Name";
    worksheet["B1"].Text = "Age";
    worksheet["A2"].Text = "John Doe";
    worksheet["B2"].Text = 30;

    // Save the workbook to a file
    workbook.Save("Output.xlsx", ExcelVersion.Excel2013);
}
```

### Customization Examples

#### Formatting Cells

You can format cells using different styles:

```csharp
using Syncfusion.XlsIO;

// Create a new Workbook instance
using (IWorkbook workbook = new Workbook())
{
    IWorksheet worksheet = workbook.Worksheets[0];

    // Set the font and color for a cell
    var cell = worksheet["A1"];
    cell.Text = "Header";
    cell.Font.SetBold();
    cell.Style.Color = ColorTranslator.ToOle(System.Drawing.Color.Lavender);

    // Save the workbook
    workbook.Save("Formatted.xlsx", ExcelVersion.Excel2013);
}
```

#### Working with Formulas

Essential XlsIO supports inserting and calculating formulas:

```csharp
using Syncfusion.XlsIO;

// Create a new Workbook instance
using (IWorkbook workbook = new Workbook())
{
    IWorksheet worksheet = workbook.Worksheets[0];

    // Insert formula into a cell
    worksheet["A1"].Text = "# of items";
    worksheet["A2"].Value = 10;
    worksheet["A3"].Formula = "=A2*2";

    // Save the workbook
    workbook.Save("Formulas.xlsx", ExcelVersion.Excel2013);
}
```

### Saving Files in Various Formats

Essential XlsIO supports saving Excel files in multiple formats:

```csharp
using Syncfusion.XlsIO;

// Create a new Workbook instance
using (IWorkbook workbook = new Workbook())
{
    workbook.Save("Output.xlsx", ExcelVersion.Excel2013);
    workbook.Save("Output.xls", ExcelVersion.Excel2003);
    workbook.Save("Output.xlsm", ExcelVersion.Excel2013); // Macro-enabled
}
```

## API Reference

### Namespace: Syncfusion.XlsIO

#### Classes

- **IWorkbook**: Represents the Excel workbook.
- **IWorksheet**: Represents a single worksheet within a workbook.
- **IStyle**: Represents the style of a cell, including font, fill, and borders.
- **IStyle.Fill**: Provides methods to set the fill color of a cell.
- **IStyle.Borders**: Provides methods to set the border styles of a cell.

#### Methods

- **Save(string fileName, ExcelVersion version)**: Saves the workbook to the specified file with the specified Excel version.
- **Worksheet(string name)**: Adds a new worksheet with the specified name to the workbook.
- **Cell(string address)**: Gets the cell at the specified address.

#### Properties

- **Rows**: Represents all rows in the worksheet.
- **Columns**: Represents all columns in the worksheet.
- **Formulas**: Provides access to the formulas in the workbook.

### Parameters

| Name            | Type                       | Description                                                                     | Default | Required |
|-----------------|----------------------------|---------------------------------------------------------------------------------|---------|----------|
| fileName        | string                     | The name of the file to save the workbook.                                   | -       | Yes      |
| version         | ExcelVersion               | The Excel version (e.g., Excel2013, Excel2003).                            | -       | Yes      |
| address         | string                     | The address of the cell to access (e.g., "A1", "B2").                      | -       | Yes      |

### Returns

- **void**: The `Save` method returns nothing.
- **IStyle**: The `Style` property returns the style of a cell.

### Exceptions

- **FileNotFoundException**: If the specified file is not found.
- **IOException**: If an I/O error occurs.
- **InvalidOperationException**: If an operation is not valid in the current state.

## Code Examples

### Example 1: Creating a Simple Spreadsheet

```csharp
using Syncfusion.XlsIO;
using System.Drawing;

// Create a new workbook
using (IWorkbook workbook = new Workbook())
{
    IWorksheet worksheet = workbook.Worksheets[0];

    worksheet["A1"].Text = "Product";
    worksheet["B1"].Text = "Quantity";
    worksheet["A2"].Text = "Widget";
    worksheet["B2"].Value = 100;

    workbook.Save("ProductInventory.xlsx", ExcelVersion.Excel2013);
}
```

### Example 2: Using Excel Formulas

```csharp
using Syncfusion.XlsIO;

// Create a workbook
using (IWorkbook workbook = new Workbook())
{
    IWorksheet worksheet = workbook.Worksheets[0];

    worksheet["A1"].Text = "Price";
    worksheet["B1"].Text = "Quantity";
    worksheet["A2"].Value = 50.0;
    worksheet["B2"].Value = 10;
    worksheet["C2"].Formula = "=A2*B2";

    workbook.Save("Calculator.xlsx", ExcelVersion.Excel2013);
}
```

## Page-level Navigation/TOC (if applicable)

- [Getting Started](#getting-started)
- [Basic Usage Example](#basic-usage-example)
- [Customization Examples](#customization-examples)
- [Saving Files in Various Formats](#saving-files-in-various-formats)
- [API Reference](#api-reference)
- [Code Examples](#code-examples)

## Cross References

- See also:
  - [Syncfusion Documentation](https://help.syncfusion.com/) for more details.
  - [Essential Studio Documentation](https://help.syncfusion.com/) for general information on Syncfusion tools.

## RAG Annotations

<!-- tags: [Syncfusion, Winforms, XlsIO, Excel, API, 11.4.0.26] keywords: [Essential XlsIO, Excel, .NET, Workbook, Worksheet, Formula, Style, Cell, Format, Save, File] -->
```
