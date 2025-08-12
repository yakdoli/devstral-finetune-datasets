```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_070.jpeg
document_name: XlsIO
page_number: 070
page_id: XlsIO#page_070
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:52:25Z
fidelity: lossless
-->

## Overview

- This page describes the **IWorkbook** interface and its role in handling Excel workbooks. It covers the method to open Excel files, detailed explanations of the IWorkbook interface, and a list of its public methods with descriptions.

## Content

### Opening Excel Files

```csharp
excelEngine.Excel.Workbooks.Open("Excel2003.xls", ExcelOpenType.Automatic);
excelEngine.Excel.Workbooks.Open("Excel2007.xlsx", ExcelOpenType.Automatic);
```

**For more details on the Open method and its overloads**, see Class Reference in the documentation.

### IWorkbook

**IWorkbook** is used to represent a single workbook in the collection. This interface is responsible for customizing a single workbook and applies settings such as document properties, protection, find and replace that are common to the whole workbook. The **Save/SaveAs method** of IWorkbook is responsible for saving any changes made to worksheets. Note that any changes made after the Save/SaveAs statement will not be reflected in the output.

#### Public Methods

| Method                   | Description                                                                        |
|--------------------------|--------------------------------------------------------------------------------------|
| **Activate**             | Activates the first window associated with the workbook.                             |
| **AddFont**              | Adds font to the inner fonts collection and makes this font read-only.                |
| **Clone**                | Creates a copy of the current instance.                                            |
| **Close**                | Closes the workbook.                                                               |
| **CopyToClipboard**      | Copies the workbook to the clipboard.                                              |
| **CreateHFEEngine**      | Creates header/footer engine.                                                      |
| **CreateTemplateMarkersProcessor** | Creates an object that can be used for template markers processing. |
| **FindAll**              | Finds all the data that matches the given string.                                  |
| **FindFirst**            | Finds the matching data that appears first in the workbook.                         |
| **GetNearestColor**      | Gets the nearest color.                                                            |
| **GetPaletteColor**      | Returns a Color object from the workbook palette by its index.                     |
```