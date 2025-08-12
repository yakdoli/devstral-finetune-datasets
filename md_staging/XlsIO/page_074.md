```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_074.jpeg
document_name: XlsIO
page_number: 074
page_id: XlsIO#page_074
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:52:39Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Explains key elements of the `IWorkbook` interface in **Syncfusion Winforms**.
- Lists properties and methods available for workbook manipulation.
- Provides an introduction to worksheet-related features and event handling.
- Focuses on the `Worksheet` object and its role within the `Worksheets` collection.

## Content

### Workbook Properties

| Property             | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `StandardFontSize`   | Returns or sets the standard font size, in points.                        |
| `Styles`            | Returns a `Styles` collection that represents all the styles in the specified workbook. |
| `TabSheets`         | Returns collection of tab sheets.                                           |
| `ThrowOnUnknownNames`| Indicates whether exception should be thrown when unknown name was found in a formula. |
| `Version`           | Gets/sets Excel version.                                                    |
| `Worksheets`        | Returns a `Sheets` collection that represents all the worksheets in the specified workbook. **Read-Only Sheets object.** |

### Public Events

| Event          | Description                                             |
|-----------------|--------------------------------------------------------|
| `OnFileSaved`  | This event is handled after workbook is successfully saved. |
| `OnReadOnlyFile`| This event is handled when trying to save to a read-only file. |

### 3.6.3 Worksheet

#### Introduction
The worksheet object is a member of the `Worksheets` collection. The `Worksheets` collection contains all the worksheet objects in a workbook. The `IWorksheet` interface is responsible for applying settings that are sheet-oriented. This controls the worksheet visibility, importing data from various data sources, and row and column manipulation.

#### Public Methods

| Method      | Description                                                  |
|-------------|--------------------------------------------------------------|
| `Activate`  | Makes the current sheet the active sheet. Equivalent to clicking the sheet's tab. |
```