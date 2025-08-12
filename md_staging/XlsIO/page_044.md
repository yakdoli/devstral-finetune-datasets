```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_044.jpeg
document_name: XlsIO
page_number: 044
page_id: XlsIO#page_044
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:51:01Z
fidelity: lossless
-->

# Essential XlsIO

An instance of XlsIO is created.

## Overview
1. Create an instance of the Excel application through the IApplication interface.

### Code Example: Creating Excel Application Instance
#### C#
```csharp
// Step 2: Instantiate the excel application object.
IApplication application = excelEngine.Excel;
```

#### VB.NET
```vb
' Step 2: Instantiate the excel application object.
Dim application As IApplication = excelEngine.Excel
```

## Creating an Excel Document
An Excel document is created.

### Creating a Workbook
2. Create a workbook. A newly created workbook has three worksheets by default. You can change the number of worksheets, using the Create method of IWorkBook as shown in the following code.

#### C#
```csharp
// A new workbook is created. [Equivalent to creating a new workbook in MS Excel].
// The new workbook will have 5 worksheets.
IWorkbook workbook = application.Workbooks.Create(5);
```

#### VB.NET
```vb
' A new workbook is created. [Equivalent to creating a new workbook in MS Excel].
' The new workbook will have 5 worksheets.
Dim workbook As IWorkbook = application.Workbooks.Create(5)
```

### Accessing Worksheet and Setting Data
A workbook with the mentioned number of worksheets is created in the Excel document.

1. Access the worksheet in the workbook and set the data for the given range, say "A1".

#### C#
```csharp
// The first worksheet object in the worksheets collection is accessed.
IWorksheet sheet = workbook.Worksheets[0];
```

## API Reference

### Methods
- **IWorkbook.Create(int numSheets)**
  - **Description**: Creates a new workbook with the specified number of worksheets.
  - **Parameters**:
    - `numSheets`: The number of worksheets to include in the new workbook.
  - **Returns**: An `IWorkbook` object representing the new workbook.
  - **Exceptions**:
    - Throws an exception if the number of sheets is invalid.

### Properties
- **IWorkbook.Worksheets**: Represents the collection of worksheets in the workbook.
  - **Type**: `IWorksheets`

## Code Examples

### Creating and Accessing a Worksheet
#### C#
```csharp
// Create a new workbook with 5 worksheets
IWorkbook workbook = application.Workbooks.Create(5);

// Access the first worksheet
IWorksheet sheet = workbook.Worksheets[0];

// Set data in cell A1
sheet.Cells["A1"].Value = "Hello, Excel!";
```

#### VB.NET
```vb
' Create a new workbook with 5 worksheets
Dim workbook As IWorkbook = application.Workbooks.Create(5)

' Access the first worksheet
Dim sheet As IWorksheet = workbook.Worksheets(0)

' Set data in cell A1
sheet.Cells("A1").Value = "Hello, Excel!"
```

## Summary
This section demonstrates the process of creating an instance of XlsIO, creating a new Excel workbook, and accessing a worksheet to set data. The examples provided are in both C# and VB.NET, showcasing how to manipulate Excel documents programmatically using Syncfusion's XlsIO library.

<!-- tags: [xlsio, exceledit, workbook, worksheet, syncfusion winforms, version 11.4.0.26] keywords: [create workbook, access worksheet, set cell data, C#, VB.NET, Excel manipulation, Excel application, IWorkbook, IWorksheet, IApplication, exceledit] -->
```