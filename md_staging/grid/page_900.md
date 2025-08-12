```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_900.jpeg
document_name: grid
page_number: 900
page_id: grid#page_900
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:48:05Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to create stacked headers in the GridGroupingControl.
- Explains the process of programmatically adding stacked header rows at runtime.
- Provides code examples in C# and VB.NET for implementing stacked headers.

## Content

### Stacked Headers in the GridGroupingControl

Figure 360: Stacked Headers created for the Grid Grouping Control

![Figure: Stacked Headers created for the Grid Grouping Control](#)

#### Programmatically Adding Stacked Headers

You can add the Stacked Header Rows at run time too. To achieve this, first you must define a required number of GridStackedHeaderDescriptors by specifying the VisibleColumns for each. Next, create a StackedHeaderRow by instantiating GridStackedHeaderRowDescriptor and add the above defined stacked headers into it. Finally, add this header row into the TableDescriptor.StackedHeaderRows collection. The following code example illustrates this process.

### C#

```csharp
GridStackedHeaderDescriptor shd = new 
GridStackedHeaderDescriptor("header1", "StackedHeader1");
shd.VisibleColumns.Add(new 
GridStackedHeaderVisibleColumnDescriptor("CustomerName"));
shd.VisibleColumns.Add(new 
GridStackedHeaderVisibleColumnDescriptor("Companyname"));
GridStackedHeaderRowDescriptor shrd = new 
GridStackedHeaderRowDescriptor("R1l",
new GridStackedHeaderDescriptor[] { shd });
this.gridGroupingControl1.TableDescriptor.StackedHeaderRows.Add(shrd);

// Customize the Appearance.
this.gridGroupingControl1.Appearance.StackedHeaderCell.BackColor = 
Color.Teal;
```

### VB.NET

```vb
Dim shd As New GridStackedHeaderDescriptor("header1", "StackedHeader1")
shd.VisibleColumns.Add(New GridStackedHeaderVisibleColumnDescriptor("CustomerName"))
shd.VisibleColumns.Add(New GridStackedHeaderVisibleColumnDescriptor("Companyname"))
Dim shrd As New GridStackedHeaderRowDescriptor("R1l", New GridStackedHeaderDescriptor() {shd})
Me.gridGroupingControl1.TableDescriptor.StackedHeaderRows.Add(shrd)

' Customize the Appearance.
Me.gridGroupingControl1.Appearance.StackedHeaderCell.BackColor = Color.Teal
```

## API Reference

- **GridStackedHeaderDescriptor**: Represents a descriptor for the stacked header.
  - Properties:
    - `VisibleColumns`: Collection of visible columns in the stacked header.
- **GridStackedHeaderRowDescriptor**: Represents a row descriptor for the stacked headers.
  - Methods:
    - `Add`: Method to add stacked headers to the row.
- **TableDescriptor.StackedHeaderRows**: Collection to hold stacked header rows.

## Code Examples

The examples above demonstrate how to dynamically add stacked headers to the GridGroupingControl and customize their appearance.

## RAG Annotations

<!-- tags: [WinForms, GridGroupingControl, StackedHeaders, Programmatically, C#, VB.NET] keywords: [GridStackedHeaderDescriptor, GridStackedHeaderRowDescriptor, TableDescriptor, StackedHeaderRows, runtime, CustomAppearance,SalesRepresentative,Owner] -->
```