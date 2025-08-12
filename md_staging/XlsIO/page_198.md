```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_198.jpeg
document_name: XlsIO
page_number: 198
page_id: XlsIO#page_198
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:00:27Z
fidelity: lossless
-->

## Overview
- Describes various `CopyFlags` applicable for copying worksheet elements.
- Provides examples using C# to copy worksheets with specified copy options.

## Content

### CopyFlags Options

The `CopyFlags` enumeration in `Syncfusion.XlsIO` allows you to specify which elements of a worksheet to copy. The following table lists the available copy options:

| **CopyFlag**         | **Description**                                               |
|-----------------------|---------------------------------------------------------------|
| CopyColumnHeight     | Copies Column Height.                                         |
| CopyOptions          | CopyOptions copy flags.                                       |
| CopyMerges           | Copies Merges.                                                |
| CopyShapes           | Copies Shapes.                                                |
| CopyConditionalFormats| Represents the CopyConditionalFormats copy flags.          |
| CopyAutoFilters       | Copies AutoFilters.                                          |
| CopyDataValidations  | Copies Data Validations.                                     |
| CopyPageSetup        | Copy page setup (page breaks, paper orientation, header, footer and other properties). |
| CopyAll              | Represents the CopyAll copy flags.                            |
| CopyWithoutNames     | Represents the CopyWithoutNames copy flags.                   |

### Example: Copying Worksheets

The following code example illustrates copying worksheets using specific copy flags.

#### C# Sample Code

```csharp
// Open the Source Workbook.
IWorkbook sourceWorkbook = 
    application.Workbooks.Open(@".........\Data\SourceWorkbookTemplate.xls");

// Open the Destination Workbook.
IWorkbook destinationWorkbook = 
    application.Workbooks.Open(@".........\Data\DestinationWorkbookTemplate.xls");

// Copy the first worksheet from the Source workbook to the destination 
// workbook with data validations.
destinationWorkbook.Worksheets.AddCopy(sourceWorkbook.Worksheets[0],
    ExcelWorksheetCopyFlags.CopyDataValidations);

// Activate the newly added worksheet in the destination workbook.
destinationWorkbook.ActiveSheetIndex = 1;

// Saving the workbook to disk.
destinationWorkbook.SaveAs("Sample.xls");
```

## API Reference

### Methods
- **AddCopy(Worksheet, CopyFlags)**:
  - **Description**: Copies a worksheet with the specified `CopyFlags`.
  - **Parameters**:
    - **Worksheet**: The source worksheet to copy.
    - **CopyFlags**: The specific elements to include in the copy.
  - **Returns**: A new worksheet in the destination workbook.

## Code Examples

The C# example demonstrates how to open source and destination workbooks, copy the first worksheet with data validations, activate the new worksheet, and save the destination workbook.

## Page-level Navigation/TOC
- CopyFlags Options
- Example: Copying Worksheets
- API Reference
- Code Examples

## Cross References
- See also: XlsIO documentation on advanced worksheet manipulation.

<!-- tags: [Syncfusion, XlsIO, Worksheet, CopyFlags, C#] keywords: [CopyColumnHeight, CopyOptions, CopyMerges, CopyShapes, CopyConditionalFormats, CopyAutoFilters, CopyDataValidations, CopyPageSetup, CopyAll, CopyWithoutNames] -->
```
