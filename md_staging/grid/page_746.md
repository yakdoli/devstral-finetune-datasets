```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_746.jpeg
document_name: grid
page_number: 746
page_id: grid#page_746
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:40:14Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Summaries can be set at design time itself through the property window of the grid grouping control. In the property window, the SummaryRows under the TableDescriptor node will let you manage the summaries for a grouping grid. Accessing the SummaryRows property will open the GridSummaryRowDescriptor collection editor. The editor contains a list of properties such as Title, SummaryColumn, Appearance, etc. that allows you to define the summaries for the desired columns and to control the appearance of these summaries.

## GridSummaryRowDescriptor Collection Editor

The GridSummaryRowDescriptor Collection Editor is used to manage the summaries for the desired columns. The editor provides a list of properties that can be defined to control the appearance and behavior of the summaries. Below are two screenshots that illustrate the use of this editor:

### Screenshot 1: GridSummaryRowDescriptor Collection Editor
- **Members:**
  - Row 1
- **Row 1 properties:**
  - **Misc:**
    - Name: Row 1
    - Visible: True
    - Title
    - TitleColumnCount: 0
    - SummaryColumns: Count = 1

### Screenshot 2: GridSummaryColumnDescriptor Collection Editor
- **Members:**
  - TotalWins
- **TotalWins properties:**
  - **Design:**
    - Name: TotalWins
    - **Look And Feel:**
      - Format: {Count}
      - Style: Column
      - Appearance: Appearance
    - **Misc:**
      - SummaryType: Int32Aggregate
      - DataMember: wins
      - DisplayColumn: wins
      - IgnoreRecordFilter: False
      - MaxLength: 12

## Event List

## Data Source Operations

### Features

### Summaries

Using the GridSummaryRowDescriptor and GridSummaryColumnDescriptor collection editors, you can easily define and customize summaries for your grid columns. These features are particularly useful for performing calculations such as total wins, as demonstrated in the screenshots.

## API Reference

### GridSummaryRowDescriptor

#### Properties
- **Name**: Sets the name of the summary row.
- **Visible**: Determines whether the summary row is visible.
- **Title**: Sets the title of the summary row.
- **TitleColumnCount**: Specifies the number of title columns.
- **SummaryColumns**: Manages the list of summary columns associated with the row.

### GridSummaryColumnDescriptor

#### Properties
- **Name**: Sets the name of the summary column.
- **Format**: Specifies the format for the summary value.
- **Style**: Defines the style of the summary column.
- **SummaryType**: Indicates the type of summary operation (e.g., Int32Aggregate).
- **DataMember**: Specifies the data member to use for the summary.
- **DisplayColumn**: Indicates the column to use for displaying the summary.
- **IgnoreRecordFilter**: Determines whether record filtering should be ignored.
- **MaxLength**: Sets the maximum length for the summary display.

## Code Examples

```csharp
// Example of setting up summary rows and columns in code
GridSummaryRowDescriptor summaryRow = new GridSummaryRowDescriptor();
summaryRow.Name = "Row 1";
summaryRow.Visible = true;
summaryRow.Title = "Total Wins";

GridSummaryColumnDescriptor summaryColumn = new GridSummaryColumnDescriptor();
summaryColumn.Name = "TotalWins";
summaryColumn.Format = "{Count}";
summaryColumn.SummaryType = GridSummaryType.Int32Aggregate;
summaryColumn.DataMember = "wins";

// Adding the summary column to the summary row
summaryRow.SummaryColumns.Add(summaryColumn);

// Adding the summary row to the grid
gridGroupingControl1.TableDescriptor.SummaryRows.Add(summaryRow);
```

### Understanding Summaries

By defining the properties in the GridSummaryRowDescriptor and GridSummaryColumnDescriptor, you can create summaries such as total wins, average, minimum, or maximum values from the data in your grid. These summaries provide a quick and easy way to aggregate and display important information directly within the grid control.

### Features and Benefits

- **Flexibility**: Summaries can be customized to meet specific needs by changing properties such as format and style.
- **Ease of Use**: The designer interface makes it simple to configure summaries without writing extensive code.
- **Performance**: Aggregations are optimized to handle large datasets efficiently.

## Conclusion

The GridSummaryRowDescriptor and GridSummaryColumnDescriptor collection editors provide powerful tools for defining and customizing summaries in the Syncfusion Windows Forms Grid control. By utilizing these features, developers can enhance the functionality and usability of their applications by providing meaningful aggregations of data right within the grid interface.

```html
```