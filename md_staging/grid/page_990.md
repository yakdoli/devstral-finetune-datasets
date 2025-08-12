```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_990.jpeg
document_name: grid
page_number: 990
page_id: grid#page_990
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:57:03Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the use of Print Preview Dialog Box in Grid Grouping control.
- Explains advanced printing features supported by Grid Grouping control.
- Instructions for setting headers and footers for printed pages.

## Content

### Figure 384: Grid with Print Preview Dialog Box
The figure displays a Grid Grouping control with a Print Preview Dialog Box. The grid shows categories and products, with the Print Preview Dialog Box providing a preview of the document layout, including headers, footers, and content.

**Note:** For more details, refer to the following browser sample:

```plaintext
<Install Location>\Syncfusion\EssentialStudio\<Version Number>\Windows\Grid.Grouping.Windows\Samples\2.0\Print\Print Grid Demo
```

### Advanced printing

Grid Grouping control supports the following advanced printing features:

- **Printing Entire Grid's Column on a Single Page**: It allows the printing of the entire grid's column on a single page.
- **Specifying Headers and Footers**: Users can specify custom headers and footers for the printed pages.
- **Using Username and Password**: The control can include a prompt for a password, as shown in the figure.
- **Setting Column Fit**: Column fitting can be adjusted to fit on a single page by setting the `ScaleColumnsToFitPage` property to `true`.

Headers and footers can be added using the events `DrawGridPrintHeader` and `DrawGridPrintFooter`.

#### Setting Headers and Footers
The following code example illustrates setting the header and footer for the page to be printed.

```csharp
// Example code for setting headers and footers
GridPrintDocumentAdv printDoc = new GridPrintDocumentAdv();
printDoc.DrawGridPrintHeader += (sender, e) =>
{
    e.Graphics.DrawString("Custom Header", new Font("Arial", 10), 
        Brushes.Black, new Rectangle(0, 0, e.PageBounds.Width, 20));
};
printDoc.DrawGridPrintFooter += (sender, e) =>
{
    e.Graphics.DrawString("Custom Footer", new Font("Arial", 10),
        Brushes.Black, new Rectangle(0, e.PageBounds.Height - 20, 
        e.PageBounds.Width, 20));
};
```

### Conclusion
This document provides an overview of the Grid Grouping control's advanced printing features, including how to print the grid, specify custom headers and footers, and ensure a proper layout fit on a single page.

## API Reference

### GridPrintDocumentAdv
- **Methods**: 
  - `DrawGridPrintHeader`: Customizes the header of the printed page.
  - `DrawGridPrintFooter`: Customizes the footer of the printed page.

### Properties
- `ScaleColumnsToFitPage`: Controls whether columns fit within a single page.

### Events
- `DrawGridPrintHeader`: Triggered when the header of the printed page is drawn.
- `DrawGridPrintFooter`: Triggered when the footer of the printed page is drawn.

## Page-level Navigation/TOC
- **Overview**
- **Content**
  - **Figure 384: Grid with Print Preview Dialog Box**
  - **Advanced printing**
  - **Setting Headers and Footers**

## Cross References
- **See also**:
  - Browser sample: `<Install Location>\Syncfusion\EssentialStudio\<Version Number>\Windows\Grid.Grouping.Windows\Samples\2.0\Print\Print Grid Demo`

<!-- tags: [essentialsd, grid grouping control, windows forms, advanced printing, headers, footers] keywords: [grid, print preview, headers, footers, advanced printing, user guide] -->
```