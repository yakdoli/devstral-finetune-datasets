```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_066.jpeg
document_name: XlsIO
page_number: 066
page_id: XlsIO#page_066
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:52:07Z
fidelity: lossless
-->

## Overview
- Lists important properties and their descriptions for the XlsIO API.
- Focuses on read-only and configurable properties for managing Excel workbooks and settings.
- Includes details about separators and file handling configurations.

## Content

### Properties of XlsIO

| Property Name                  | Description                                                                                                                          |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ActiveWorkbook                 | Returns a Workbook object that represents the workbook in the active window (the window on top). It is a Read-Only property. Returns nothing if there are no windows open or if either the Info window or the Clipboard window is the active window. |
| ArgumentsSeparator             | Formula arguments separator. This can be used to change the separator used in the formulas as per the culture.                                                                                     |
| Build                          | Returns the Microsoft Excel build number. It is a Read-Only property.                                                                                                                         |
| ChangeStyleOnCellEdit         | If this property is set to True, then if some cells have reference to the same style, changes will influence all these cells. Default value is False.                                                        |
| CSVSeparator                   | Represents CSV Separator. Using for Auto recognize file type.                                                                                                                                    |
| DecimalSeparator               | Sets or returns the character used for the decimal separator as a String.                                                                                                                       |
| DefaultFilePath                | Returns or sets the default path that Microsoft Excel uses when it opens files.                                                                                                                  |
| DefaultVersion                 | Gets/sets default Excel version. This value is used in create methods.                                                                                                                          |
| DeleteDestinationFile          | Indicates whether XlsIO should delete the destination file before saving into it. Default value is True.                                                                                          |
| FixedDecimal                   | All data entered after this property is set to True will be formatted with the number of fixed decimal places set by the FixedDecimalPlaces property.                                               |
| FixedDecimalPlaces            | Returns or sets the number of fixed decimal places used when the FixedDecimal property is set to True.                                                                                             |
| Path                           | Returns the complete path to the application, excluding the final separator and name of the application. It is a Read-Only property.                                                               |

## API Reference

### Namespaces and Class Context
- This segment pertains to the XlsIO library, which is part of the Syncfusion Winforms framework.

### Properties
- `ActiveWorkbook`: A read-only property providing a reference to the active workbook.
- `Build`: A read-only property returning the Excel build number.
- `Path`: A read-only property providing the application's complete path.
- `DeleteDestinationFile`: A configurable property to manage file deletion before saving.

## Code Examples

```csharp
// Example of using ActiveWorkbook
using Syncfusion.XlsIO;

IApplication application = new Application();
try
{
    IWorkbook workbook = application.ActiveWorkbook;
    if (workbook != null)
    {
        // Perform operations on the workbook
    }
}
finally
{
    if (workbook != null)
    {
        workbook.Dispose();
    }
    application.Dispose();
}
```

## Cross References
- See also the broader documentation on Excel file handling and property management in the XlsIO API Reference section.

<!-- tags: [syncfusion, xlsio, workbook, properties, excel, winforms] keywords: [active workbook, formula arguments separator, build number, style editing, decimal separator, file path, fixed decimal places, path to application, delete destination file] -->
```