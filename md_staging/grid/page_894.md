```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_894.jpeg
document_name: grid
page_number: 894
page_id: grid#page_894
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:50:24Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- 1-3 bullets summarizing the page scope using only visible text.
  - Demonstrates the setup and configuration of a `GridGroupingControl` using the `StackedHeaderRows` property.
  - Manages layout and design properties for stacked header rows in a Grid.
  - Configures visible columns and table descriptors for data display.

## Content

### StackedHeader Rows Configuration

#### GridGroupingControl Properties
- The `GridGroupingControl` is accessed through the Properties window.
- The `StackedHeaderRows` property is highlighted, indicating its importance in defining stacked headers for the grid.

#### GridStackedHeaderRowDescriptor Collection Editor
This editor is used to define properties for each stacked header row in the grid.

##### Row 2 Properties
- **Name**: `Row 2`
- **Headers**: `Count = 2`

##### StackedHeader 1 Properties
- **Name**: `StackedHeader 1`
- **Look And Feel**
  - **Appearance**: `Appearance`
- **TableDescriptors**
  - **Name**: `StackedHeader 1`
- **VisibleColumns**: `Count = 3`

#### GridStackedHeaderVisibleColumnDescriptor Collection Editor
This editor allows setting properties for visible columns.

##### CustomerID Properties
- **TableDescriptors**
  - **Name**: `CustomerID`

## API Reference

### Namespace
- `Syncfusion.Windows.Forms.Grid`

### Members
- **StackedHeaderRows**: Property to manage stacked header rows.
- **GridStackedHeaderRowDescriptor**: Descriptor for configuring each stacked header.
- **TableDescriptors**: Property to define the table structure.

## Code Examples

```csharp
// Example of configuring StackedHeaderRows
GridStackedHeaderRowDescriptor header1 = new GridStackedHeaderRowDescriptor();
header1.Name = "StackedHeader 1";
header1.HeaderText = "Header 1";

GridStackedHeaderRowDescriptor header2 = new GridStackedHeaderRowDescriptor();
header2.Name = "Row 2";
header2.Headers.Add(new GridStackedHeaderDescriptor()
{
    Name = "Header 2",
    HeaderText = "Header 2"
});

GridGroupingControl1.StackedHeaderRows.Add(header1);
GridGroupingControl1.StackedHeaderRows.Add(header2);
```

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, GridGroupingControl, StackedHeaderRows, TableDescriptors] keywords: [GridGroupingControl, StackedHeaders, HeaderRows, VisibleColumns, TableDescriptors] -->
```