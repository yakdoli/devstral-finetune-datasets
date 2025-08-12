```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_899.jpeg
document_name: grid
page_number: 899
page_id: grid#page_899
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:48:34Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Explains how to control the appearance of Stacked Headers in the grid.
- Describes two methods to apply appearance settings to stacked headers: using the Appearance.StackedHeaderCell property and through the GridStackedHeaderRow Descriptor.
- Highlights the customization options for individual stacked headers within each StackedHeaderRow.

## Content

### Controlling the Appearance of StackedHeaders

A couple of ways are there to control the appearance of the StackedHeaders. By one way you can access Appearance.StackedHeaderCell property to enter the appearance definitions. Appearance set this way will be applied to all the stacked header cells. An alternate way is to specify the appearance settings through the GridStackedHeaderRow Descriptor. In this way, you can have different settings for individual stacked headers in each StackedHeaderRow.

#### Property Window with GridStackedHeaderRowDescriptor Collection Editor

Here is the property window with GridStackedHeaderRowDescriptor Collection Editor showing the appearance settings of Stacked Headers defined.

#### Figure 359: Appearance Settings for Stacked Headers

![GridStackedHeaderRowDescriptor Collection Editor Image](#)

This image shows the property window that allows you to define appearance settings for stacked headers. It includes options for styling individual stacked headers by setting different interior colors for each header.

### Output

Here is the effect of the above settings.

## API Reference

### GridStackedHeaderRowDescriptor

- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: GridStackedHeaderRowDescriptor
- **Properties**:
  - Headers: Contains a collection of StackedHeader cells.
  - Name: Identifier for the stacked header row.
  - HeaderText: Text displayed in the stacked header.
  - VisibleColumns: Specifies the visible columns associated with the stacked header.
  - Appearance: Defines the appearance settings.
  - StackedHeaderCell: Provides styling options, such as setting the background color (e.g., PaleGreen or WhiteSmoke).

### Example Usage

This example demonstrates how to configure the appearance settings for stacked headers in the GridStackedHeaderRowDescriptor.

```csharp
gridStackedHeaderRowDescriptor.Row1.Headers[0].Appearance.StackedHeaderCell.Interior = Color.PaleGreen;
gridStackedHeaderRowDescriptor.Row1.Headers[1].Appearance.StackedHeaderCell.Interior = Color.WhiteSmoke;
```

## RAG Annotations

<!-- tags: [syncfusion, winforms, grid, stackedheaders, appearance] keywords: [StackedHeader, GridStackedHeaderRowDescriptor, Appearance, StackedHeaderCell, interior, PaleGreen, WhiteSmoke, customization] -->
```