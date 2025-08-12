```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_357.jpeg
document_name: XlsIO
page_number: 357
page_id: XlsIO#page_357
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:13:09Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Provides a feature to sort any range of cells dynamically at runtime without any dependency on MS Excel.
- Allows sorting based on cell values, font color, and cell color.
- Notes the unsupported features for sorting based on cell icon, parsing, and serialization of sorting details.

## Content

### 4.5.3 Data Sorting for a Given Range of Cells in the Worksheet
This feature allows sorting any range of cells dynamically at runtime, without any dependency on MS Excel. You can sort a given range of cells in a worksheet by applying the sort feature to a range, which changes the related data within the range. The user can sort the range in the following ways:
- Sorting by Cell Values
- Sorting by Font Color
- Sorting by Cell Color

**Note:** Presently we don’t support sorting based on cell icon, parsing and serialization of the sorting details.

#### 4.5.3.1 Properties, Methods and Events tables

#### IDataSort Members:
IDataSort members represent the sort of the range.

#### Properties

| Name            | Description                                      |
|-----------------|--------------------------------------------------|
| IsCaseSensitive | Indicates whether or not to perform case sensitive sort |
| HasHeader       | Indicates whether the range has header         |
| Orientation     | Represents the sort orientation                 |
| SortFields      | Represents the SortFields Collection           |
| SortRange       | Represents the sort range                      |
| Algorithm       | Represents the algorithm to sort               |

#### Methods

| Name    | Description                                 |
|---------|---------------------------------------------|
| Sort()  | Sorts the range, based on the sort fields. |

## API Reference (if applicable)
- **Namespace**: Essential.XlsIO
- **Class**: IDataSort

#### Properties
- **IsCaseSensitive**: Indicates whether or not to perform case-sensitive sorting.
- **HasHeader**: Indicates whether the range has a header.
- **Orientation**: Represents the sort orientation.
- **SortFields**: Represents the SortFields Collection.
- **SortRange**: Represents the sort range.
- **Algorithm**: Represents the algorithm to sort.

#### Methods
- **Sort()**: Sorts the range based on the specified sort fields.

## Code Examples (multi-language supported)
```csharp
// Example: Sorting a range of cells in a worksheet
using Syncfusion.XlsIO;
using System;

class Program
{
    static void Main()
    {
        // Create a new instance of the workbook
        using (var workbook = new Workbook())
        {
            IWorksheet worksheet = workbook.Worksheets[0];

            // Define the range to sort
            IRange sortRange = worksheet["A1:B10"];

            // Get the sort object
            IDataSort dataSort = sortRange.DataSort;

            // Configure sorting parameters
            dataSort.IsCaseSensitive = true;
            dataSort.HasHeader = true;
            dataSort.Orientation = SortOrientation.Ascending;
            dataSort.SortFields.Add(0); // Sort by first column

            // Perform the sort
            dataSort.Sort();

            // Save the workbook
            workbook.Save("SortedWorkbook.xlsx");
        }
    }
}
```

## Page-level Navigation/TOC (if applicable)
- 4.5.3 Data Sorting for a Given Range of Cells in the Worksheet
- 4.5.3.1 Properties, Methods and Events tables

## Cross References
- See also: Other sections related to data manipulation in XlsIO.

<!-- tags: XlsIO, data sorting, workbook, cell, dynamic sorting, runtime sorting, font color, cell color, sorting options, unsupported features, WinForms, version: 11.4.0.26 -->
```