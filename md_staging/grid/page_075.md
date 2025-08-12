```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_075.jpeg
document_name: grid
page_number: 075
page_id: grid#page_075
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:20:33Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Learn how to display data using the Grid Grouping control.
- Explore grouping functionality by dragging column headers.
- Understand how to visualize data without writing code.

## Content

### Displaying Data from the MDB File

13. Run the application to see the Grid Grouping control display the data from the MDB file (without having written a single line of code). Your form should look similar to the one in the following screenshot.

![Figure 41: Application showing Grid Grouping control with Data](./grid.jpg)

**Figure 41: Application showing Grid Grouping control with Data**

### Grouping Data by Column

14. To group by `CompanyName`, click on the `CompanyName` column header and drag it to the drop area as illustrated in the following screenshot.

![Unclear content description. Missing screenshot content.]()

## API Reference

This section does not provide any specific API references directly related to the screenshot content. However, the Grid Grouping control typically includes methods and properties for managing grouping, sorting, and data binding. For detailed API information, refer to the Syncfusion documentation.

## Code Examples

No code examples are provided in the current content. To work with the Grid Grouping control in Syncfusion Winforms, you can use the following structure as a starting point:

```csharp
using Syncfusion.Windows.Forms.Grid;
using Syncfusion.Windows.Forms.Grid.Grouping;

// Create the GridGroupingControl instance
GridGroupingControl gridGroupingControl = new GridGroupingControl();

// Connect to a data source (e.g., from an MDB file)
// This typically involves setting up data binding through the DataSource property
gridGroupingControl.DataSource = yourDataSource;

// Enable grouping functionality
gridGroupingControl.AllowGrouping = true;

// Add the control to your form
yourForm.Controls.Add(gridGroupingControl);
```

## Page-level Navigation/TOC
- Displaying Data from the MDB File
- Grouping Data by Column

## Cross References
- Refer to the Syncfusion documentation for more information on the Grid Grouping control and its features.
- Check the official Syncfusion documentation for specific API details and advanced usage scenarios.

<!-- tags: [windows-forms, grid-grouping, data-binding, grouping, essential-grid] keywords: [displaying data, group by, column header, mdb file, drag and drop, grid grouping control] -->
``` 
