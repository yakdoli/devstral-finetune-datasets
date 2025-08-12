```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_071.jpeg
document_name: XlsIO
page_number: 071
page_id: XlsIO#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:52:39Z
fidelity: lossless
-->

## Overview
- Provides methods for managing and protecting workbooks, including saving, replacing, and setting protections.
- Lists public properties that facilitate access and manipulation of workbook features such as active sheets, data validation, and application settings.

## Content

### Workbook Methods
The following methods are used to manage workbooks:

| Method               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| Protect              | Protects the workbook.                                                     |
| Replace              | Replaces the given data.                                                   |
| ResetPalette         | Recovers palette to default values.                                        |
| Save                 | Saves changes to the same workbook.                                        |
| SaveAs              | Saves changes to another workbook.                                         |
| SaveAsXml           | Save as Xml [SpreadsheetML].                                               |
| SetColorOrGetNearest| Gets/sets the nearest color.                                               |
| SetPaletteColor      | Sets user color for specified element in Color table.                    |
| SetSeparators       | Sets separators for formula parsing.                                       |
| SetWriteProtectionPassword | This method sets write protection password.                        |
| Unprotect           | Removes protection.                                                        |

### Public Properties
The following properties provide access to various workbook features and settings:

| Property                   | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| ActiveSheet                | Returns an object that represents the active sheet (the sheet on top) in the active workbook or in the specified window or workbook. Returns nothing if no sheet is active. This is a Read-Only property. |
| ActiveSheetIndex           | Gets/sets index of the active sheet.                                      |
| AddInFunctions             | Returns collection of all workbook's add-in functions. This is a Read-Only property. |
| Allow3DRangesInDataValidation | Indicates whether to allow usage of 3D ranges in DataValidation list property (MS Excel does not allow usage of 3D ranges in DataValidation list property). |
| Application                | Application object for this object (Inherited from IParentApplication).   |
| ArgumentsSeparator        | Formula arguments separator.                                             |

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.

## Cross References
- See also: `Essential XlsIO`, `Workbook`, `Workbooks`, `Formulas`

## RAG Annotations
<!-- tags: [Syncfusion Winforms, XlsIO, Workbook, Workbooks, Methods, Properties] keywords: [Protect, Replace, ResetPalette, Save, SaveAs, SaveAsXml, SetColorOrGetNearest, SetPaletteColor, SetSeparators, SetWriteProtectionPassword, Unprotect, ActiveSheet, ActiveSheetIndex, AddInFunctions, Allow3DRangesInDataValidation, Application, ArgumentsSeparator] -->
```

