```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_088.jpeg
document_name: XlsIO
page_number: 088
page_id: XlsIO#page_088
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:54:25Z
fidelity: lossless
-->

# Support for Excel 2007 file formats in XlsIO

This page summarizes the various features and functionalities provided by XlsIO in handling Excel 2007 file formats.

## Overview

- Merged cells support.
- Row and column settings, including default style, height/width, and visibility.
- Named ranges support.
- Ability to open Excel 2007 files and save them in 2003 format, excluding unsupported items.
- Existing functionality for AutoFilters.
- Read/write data validation support.
- Support for conditional formatting, with increased possible rules compared to Excel 97-2003.
- New visualizations such as Data bars, Icon sets, and Color scales.
- Adjustments for row/column height and width, including inserting, grouping/ungrouping (with summary settings), freezing, and splitting panes.
- Operations for images, including insertion, removal, movement, resizing, opening, and saving without fill.
- Read/write hyperlinks functionality.
- Comments (open/save/move/resize/add/remove/get and set rich text, author, and without fill).
- Access to document properties (both built-in and custom) and sheet level properties.
- Page setup includes handling header/footer images, page breaks, layout, zoom, and sheet alignment adjustment.
- Control of worksheet properties such as tab color and background.

## Detailed Features

### Excel File Format Handling

- **Merged cells support**: Ensures functionality for merged cells is retained.
- **Row and column settings**: Customize styles, dimensions, and visibility of rows and columns.

### Data Component

- **Named ranges**: Support for accessing and manipulating named ranges within a worksheet.

### File Compatibility

- **Compatibility between 2007 and 2003 formats**: Smoothly open Excel 2007 files and export to 2003 format, omitting unsupported features.

### Data Filtering and Validation

- **AutoFilters**: Leverage the existing AutoFilter functionality to filter data dynamically.
- **Read/write data validation**: Implement and manage data validation rules.

### Conditional Formatting and Visual Enhancements

- **Conditional formatting**: Enhance existing functionality to handle more than three conditional formatting rules.
- **New visualizations**: Utilize Data bars, Icon sets, and Color scales to present data visually.

### Row and Column Management

- Manipulate row and column dimensions, insert, group, ungroup, freeze, and split panes to optimize worksheet layout.

### Image and Link Management

- Perform various operations on images within the worksheet and manage hyperlinks.

### Comments and Properties

- Handle comments with open/save functionalities, along with rich text and author tracking.
- Access and modify both built-in and custom document and sheet level properties.

### Page Setup and Layout

- Configure all page setup aspects, including header/footer images, page breaks, zoom, and alignment.
- Provide the capability to preview page breaks.

### Worksheet Properties

- Customize the appearance of worksheets by adjusting tab color and background.

## API Reference

- Refer to detailed documentation for specific APIs related to these functionalities within XlsIO.

## Code Examples

- Examples demonstrating the implementation of these features are available in the official documentation.

## RAG Annotations

<!-- tags: [xlsio, excel, file formats, data validation, hyperlinks, comments, page setup, worksheet properties] keywords: [Syncfusion, Excel 2007, XlsIO, conditional formatting, named ranges, image operations, data validation, auto filters, worksheet properties] -->
```