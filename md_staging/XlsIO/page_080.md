```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_080.jpeg
document_name: XlsIO
page_number: 080
page_id: XlsIO#page_080
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:53:44Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Basic properties and methods related to worksheet handling in XlsIO. Focus on functionalities for managing names, page setup, pictures, protection, and range objects.
- Emphasis on working with worksheet-specific names, read-only properties, and split ranges.

## Content

### WinForms-specific conventions
- The table below outlines key properties with their descriptions and functionalities.

#### Properties Table
| Property               | Description                                                                                                                              |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Name                   | Gets/sets name of the tab sheet.                                                                                                         |
| Names                 | For a Worksheet object, returns a Names collection that represents all the worksheet-specific names (names defined with the "WorksheetName!" prefix). Read-Only Names object. |
| PageSetup             | Returns a PageSetup object that contains all the page setup settings for the specified object. This is a Read-Only property.                            |
| Pictures              | Returns pictures collection. This is a Read-Only property.                                                                              |
| ProtectContents        | Indicates if current sheet is protected.                                                                                                 |
| ProtectDrawingObjects | This property is set to true if objects are protected. This is a Read-Only property.                                                    |
| Protection            | Gets protected options. For setting the protection options, use "Protect" method.                                                        |
| ProtectScenarios       | This property is set to true if the scenarios of the current sheet are protected. This is a Read-Only property.                              |
| Range                 | Returns a Range object that represents a cell or a range of cells.                                                                      |
| Rows                  | For a Worksheet object, returns an array of Range objects that represents all the rows on the specified worksheet.                         |
| SplitCell             | Returns split cell range.                                                                                                                 |
| StandardHeight        | Returns or sets the standard (default) height of all the rows in the worksheet, in points.                                               |
| StandardHeightFlag    | Returns or sets the standard (default) height option flag, which defines that standard (default) row height and book default font height do not match. |
| StandardWidth         | Returns or sets the standard (default) width of all                                                                                      |

---

## API Reference

### Namespace: Syncfusion.XlsIO

#### Members

##### Properties
- **Name**: Gets/sets the name of the tab sheet.
- **Names**: Represents all the worksheet-specific names in the form of a Names collection.
- **PageSetup**: Returns page setup settings for the specified object.
- **Pictures**: Returns a collection of all pictures on the worksheet.
- **ProtectContents**: Indicates if the current sheet is protected.
- **ProtectDrawingObjects**: Indicates protection status for drawing objects.
- **Protection**: Gets protection options and settings.
- **ProtectScenarios**: Indicates if scenarios of the current sheet are protected.
- **Range**: Represents a cell or a range of cells.
- **Rows**: Represents all rows on the specified worksheet.
- **SplitCell**: Represents the split cell range.
- **StandardHeight**: Gets or sets the default height of all rows.
- **StandardHeightFlag**: Gets or sets whether the standard row height differs from the book default font height.
- **StandardWidth**: Gets or sets the default width of all columns.

##### Methods
- **Protect()**: Sets protection options for the worksheet.

---

## Code Examples

Example of usingWorksheet properties in XlsIO:

```csharp
// Create workbook and worksheet
Workbook workbook = new Workbook();
IWorksheet worksheet = workbook.Worksheets[0];

// Accessing properties
worksheet.Name = "Sheet1";
IPageSetup pageSetup = worksheet.PageSetup;
IImagesCollection images = worksheet.Pictures;

// Protecting the worksheet
worksheet.Protect("password", ProtectionType.All);

// Accessing range
IRange range = worksheet.Range["A1:B5"];

// Adjusting standard height
worksheet.StandardHeight = 15;

```

---

## Cross References
- See also: [Formatting and Styling in XlsIO](#),
- [Page Setup Options in XlsIO](#),
- [Workbook and Worksheet Operations](#).

---

<!-- tags: [xlsio, worksheet, properties, protection, page setup, pictures] keywords: [worksheet, names, standard height, protection, pictures, range, page setup, split cell] -->
```