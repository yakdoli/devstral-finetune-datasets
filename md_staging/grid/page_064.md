```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: grid
page_number: 064
page_id: grid#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:20:04Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains how to bind an MDB file to a Grid Grouping control using Visual Studio 2005 and .NET 2.0.
- Demonstrates grouping grid functionality with sample data.
- Focuses on designer-based tutorial with no coding required.

## Content

### WinForms Grouped Grid

#### Figure 27: Grouped Grid
The image shows a grouped grid displaying a list of suppliers categorized by their company names. Each category is expandable/collapsible, with items listed under specific company names, including address and city details.

### 3.1.2.2 Binding to an MDB File By Using VS 2005
The steps in this lesson are for use with Visual Studio 2005 and .NET 2.0. You can use Smart Tags that are available in the .NET 2.0 Designer to hook into your MDB file. This tutorial is strictly a designer tutorial. You do not have to write even a single line of code.

1. **From the Syncfusion tab in the toolbox**, drag a **Grid Grouping control** onto your form.
2. **In the Grid Grouping control smart tag**, click the **Choose Data Source** drop down. Then click the **Add Project Data Source** link in the drop down.

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: GridGroupingControl
- **Properties**:
  - **DataSource**: Specifies the data source for the grid.
  - **SmartTags**: Enables designer-based configuration for binding.

## Code Examples
```csharp
// Designer-based approach to bind an MDB file
// This example uses Smart Tags for data binding in the Grid Grouping Control
```

## RAG Annotations
<!-- tags: [Syncfusion Winforms, GridGroupingControl, Visual Studio 2005, .NET 2.0, Smart Tags, Designer-based tutorial, MDB file, Grouped Grid] keywords: [Grid, DataBinding, CompanyName, Address, City, Exotic Liquids, Escargots Nouveaux, Cooperativa de Quesos 'Las Cabras'] -->
```