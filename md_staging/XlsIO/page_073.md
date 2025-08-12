```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_073.jpeg
document_name: XlsIO
page_number: 073
page_id: XlsIO#page_073
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:53:07Z
fidelity: lossless
-->

# XlsIO

## Overview
- Indicates if a window is protected.
- Returns the maximum column count for each worksheet in a workbook.
- Returns the maximum row count for each worksheet in a workbook.
- Returns a Names collection representing all the names in the active or specified workbook.
- Gets the Palette of colors available in an Excel document.
- Gets/sets the password to encrypt a document.
- Indicates if the workbook is opened as Read-only.
- Indicates if a message is displayed recommending opening a file as read-only.
- Gets/sets the row separator for array parsing.
- Indicates if the workbook has unsaved changes.
- Returns or sets the name of the standard font.

## Content

### Workbook Properties

| Property           | Description                                                                                                                                                                                                 |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IsWindowProtection | Indicates if the window is protected.                                                                                                                                                                      |
| MaxColumnCount     | Returns the maximum column count for each worksheet in this workbook. This is a Read-Only property.                                                                                                         |
| MaxRowCount        | Returns the maximum row count for each worksheet in this workbook. This is a Read-Only property.                                                                                                             |
| Names             | For an Application object, returns a Names collection representing all the names in the active workbook. For a Workbook object, returns a Names collection representing all the names in the specified workbook, including all worksheet-specific names. |
| Palette           | Gets the Palette of colors which an Excel document can have. <br>Here is a table of color indexes to places in the color tool box provided by Excel application: <br>------------- | 1 | 2 | 3 | 4 | 5 | 6<br>--------------------------------------------------------------- | 7 | 8 | --- + --------------------------------------------------------------- | 1 | 00 | 51 | 50 | 49 | 47 | 10 | 53 | 54 | 2 | 08 | 45 | 11 | 09 | 13 | 04 | 46 | 15 | 3 | 02 | 44 | 42 | 48 | 41 | 40 | 12 | 55 | 4 | 06 | 43 | 05 | 03 | 07 | 32 | 52 | 14 | 5 | 37 | 39 | 35 | 34 | 33 | 36 | 38 | 01 | --- + --------------------------------------------------------------- | 6 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 7 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | ---------------------------- |
| PasswordToOpen     | Gets/sets the password to encrypt the document.                                                                                                                                                           |
| ReadOnly           | True if the workbook has been opened as Read-only.                                                                                                                                                        |
| ReadOnlyRecommended| True to display a message when the file is opened, recommending that the file be opened as read-only.                                                                                                       |
| RowSeparator       | Gets/sets the row separator for array parsing.                                                                                                                                                            |
| Saved              | This property is set to true if no changes have been made to the specified workbook since it was last saved.                                                                                               |
| StandardFont       | Returns or sets the name of the standard font.                                                                                                                                                            |

### Summary
- **Protection**: IsWindowProtection indicates the protection status of a window.
- **Structure**: MaxColumnCount and MaxRowCount return the maximum dimensions of worksheets.
- **Names Management**: The Names property provides access to named ranges or defined names within a workbook.
- **Customization**: Palette offers a way to get the color palette used by Excel.
- **Security**: PasswordToOpen can be used to encrypt workbooks.
- **State Management**: Read-only and Save status can be checked or enforced programmatically.

### Figure: Palette Index Mapping
| Palette Index Mapping                              |
|----------------------------------------------------|
| Table showing the mapping of color indexes to places in the Excel color tool box. |

### Code Example (C#)
```csharp
// Example of accessing and setting properties
using Syncfusion.XlsIO;

Workbook workbook = new Workbook();
IApplication application = workbook.Excel.Application;

// Accessing palette
Color[] palette = application.Palette;

// Setting password to open
application.PasswordToOpen = "SecurePassword";

// Checking if workbook is read-only
bool isReadOnly = workbook.Readonly;

// Saving the workbook
workbook.Save("Output.xlsx");
workbook.Close();
```

## API Reference
- **Namespace**: `Syncfusion.XlsIO`
- **Type**: `Workbook`/`IApplication`

### Properties
- **IsWindowProtection**: Indicates whether the window is protected.
- **MaxColumnCount**: Returns the maximum column count for each worksheet.
- **MaxRowCount**: Returns the maximum row count for each worksheet.
- **Names**: Returns a Names collection representing all names in the workbook.
- **PasswordToOpen**: Gets or sets the password to encrypt the document.
- **ReadOnly**: Indicates if the workbook is read-only.
- **ReadOnlyRecommended**: Indicates if a message is displayed for read-only recommendation.
- **RowSeparator**: Gets or sets the row separator for array parsing.
- **Saved**: Indicates if the workbook is saved without changes.
- **StandardFont**: Returns or sets the name of the standard font.

### Methods
- No specific methods mentioned in this section.

### Events
- No specific events mentioned in this section.

## RAG Annotations
<!-- tags: [xlsio, workbook, properties, palette, password, read-only, names, standard-font] keywords: [iswindowprotection, maxcolumncount, maxrowcount, names, palette, passwordtoopen, readonly, readonlyrecommended, rowseparator, saved, standardfont] -->
```