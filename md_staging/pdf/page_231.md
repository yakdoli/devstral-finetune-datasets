<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_231.jpeg
document_name: pdf
page_number: 231
page_id: pdf#page_231
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:39:49Z
fidelity: lossless
-->

# Essential PDF

## Overview

- Creating and formatting tables in PDF documents using the PdfLightTable class.
- Configuring table styles, such as alternate row and header row styles.
- Setting data sources and visual properties for PDF tables.

## Content

### Creating and Formatting PDF Tables

The following code example illustrates how to create and format tables.

#### C#

```csharp
// Create Pdf table.
PdfLightTable table = new PdfLightTable();

// Set Data source.
table.DataSource = dataTable;

// Set table alternate row style.
table.Style.AlternateStyle = altStyle;

// Set header row style.
table.Style.HeaderStyle = headerStyle;

// Show the header row.
table.Style.ShowHeader = true;

// Repeat header in all the pages.
table.Style.RepeatHeader = true;

// Set header data from column caption.
table.Style.HeaderSource = PdfHeaderSource.ColumnCaptions;

// Set layout properties.
PdfLayoutFormat format = new PdfLayoutFormat();
format.Break = PdfLayoutBreakType.FitElement;
format.Layout = PdfLayoutType.Paginate;

// Draw table.
table.Draw(page, PointF.Empty, format);
```

#### VB.NET

```vb
' Create Pdf table.
Dim table As PdfLightTable = New PdfLightTable()

' Set Data source.
table.DataSource = dataTable

' Set table alternate row style.
table.Style.AlternateStyle = altStyle
```

### API Reference

#### Namespaces
- **PdfLightTable**: Used for creating and styling tables in PDF documents.
- **PdfLayoutBreakType**: Defines the layout break type.
- **PdfLayoutType**: Defines the layout type for the table.
- **PdfHeaderSource**: Specifies the source for table headers.

### Code Examples

The above sections provide examples of how to use the PDF APIs to create and format tables effectively.

## Page-level Navigation/TOC

- **Creating and Formatting PDF Tables**
  - C#
  - VB.NET

## Cross References

See also:
- [Syncfusion WinForms Documentation](https://help.syncfusion.com/windowsforms/)
- [PDF Light Table Documentation](https://help.syncfusion.com/windowsforms/pdf-library/light-tables)

<!-- tags: [Syncfusion, PDF, WinForms, PdfLightTable, TableFormatting] keywords: [PDF, tables, formatting, alternate row style, header style, data source, layout properties, C#, VB.NET] -->