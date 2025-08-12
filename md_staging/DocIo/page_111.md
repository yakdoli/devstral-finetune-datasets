```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_111.jpeg
document_name: DocIo
page_number: 111
page_id: DocIo#page_111
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:34:50Z
fidelity: lossless
-->

# Essential DocIO

The following screenshot illustrates the options provided by DocIO for setting the Page Number.

## Content

### Page Number Settings

![Figure: Page Number Settings](attachment:Figure_36_Page_Number_Settings.png "Figure 36: Page Number Settings")

### 4.3.3 Table

#### Overview
- WTable class represents a table in a Word document.
- Every table in the Word document consists of table rows (one or more).
- Each table row consists of table cells (one or more).

#### Detailed Explanation
WTable class has a similar architecture. It contains a collection of table rows, which is accessible through the **Rows** property. This property returns an object of the WRowCollection type. Each collection consists of WTableRow objects. For more details about WTableRow, refer to the WTableRow documentation. The **TableFormat** property defines formatting for the whole table; it returns an object of the RowFormat type. For more details about RowFormat, see **RowFormat**.

#### Key Features
- **ResetCells**: Enables users to create tables with a specified number of rows and a specified number of cells in each row.
- **WTableRow AddRow(bool isCopyFormat)**: Enables users to add a new row to the existing table. The **isCopyFormat** parameter defines whether to copy the row format from the previous row.
- **WTableRow AddRow(bool isCopyFormat, bool autoPopulateCells)**: Enables users to add a new row to the existing table. The second parameter, **autoPopulateCells**, determines whether the new row should be automatically populated with cells.

#### Notes
- The **Page Number Settings** screenshot shows options for configuring the number format, including chapter numbers, separators, and examples for page numbering.
- Users can choose to:
  - **Continue from previous section**: To start numbering from the last page of the previous section.
  - **Start at**: To set a specific starting page number for the current section.

#### References
- **RowFormat**: For detailed information on formatting rows.
- **WTableRow Documentation**: For more details on using WTableRow objects.

#### Code Examples
```csharp
// Example of using ResetCells
WTable table = document.Tables.Add("NewTable");
table.Rows.ResetCells(3, 4); // Creates a table with 3 rows and 4 columns

// Example of adding a row with specific formatting
WTableRow newRow = table.Rows.AddRow(true); // Copies the format from the previous row
```

#### Additional Resources
- Refer to the documentation for more detailed examples and parameters for the methods mentioned.

#### Page-level Navigation/TOC
- **4.3.3 Table**
  - Overview
  - Detailed Explanation
  - Key Features
  - Notes
  - References
  - Code Examples

#### Cross References
- See also: **RowFormat**, **WTableRow Documentation**

<!-- tags: [DocIO, Table, WTable, PageNumber, Format, PageNumberSettings, WinForms, syncfusion-sdk, 11.4.0.26] keywords: [WTable, Table, PageNumber, Format, AddRow, ResetCells, Rows, TableFormat, WTableRow] -->
```