```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_979.jpeg
document_name: grid
page_number: 979
page_id: grid#page_979
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:53:50Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes the AutoFilterRow feature in Grid Grouping control.
- Explains how to enable filtering using the ShowFilterBar property and AllowFilter property.
- Shows a grid with the Auto-Filter Row Enabled.

## Content

### AutoFilterRow in Grid Grouping Control

**Figure 372: Filtered Grid**

The Grid Grouping control provides an **AutoFilterRow** which can be enabled by setting the **ShowFilterBar** property to **true**. Once it is done, you must enable the **AllowFilter** property for the desired columns to enable filtering on those columns.

![Grid with Auto-Filter Row Enabled](https://i.imgur.com/placeholder.png)

**Figure 373: Grid with Auto-Filter Row Enabled**

The image shows a grid with the Auto-Filter Row Enabled. Key points:
- The grid displays a list of suppliers with details such as **SupplierID**, **CompanyName**, **ContactName**, and **ContactTitle**.
- The **ShowFilterBar** property is set to **True**, enabling the filter row at the top of the grid.
- The **AllowFilter** property is applied to the desired columns, allowing filtering on those columns.
- A sidebar on the right displays configurable properties, including settings for **TopLevelGroupOptions**, **CaptionText**, and **ShowFilterBar** set to **True**.

This setup provides a powerful filtering mechanism, enabling users to sort and filter grid data based on specific criteria.

### Example Configuration
The following properties are configured for the AutoFilterRow:
- **ShowFilterBar**: Set to **True** to enable filtering functionality.
- **CaptionText**: Customizable header text displayed above the grid.
- **AllowFilter**: Applied to specific columns to enable filtering on those columns.

This feature enhances the user experience by allowing for dynamic data manipulation directly within the grid.

### API Reference

#### Properties
- **ShowFilterBar**: Boolean property indicating whether the FilterBar is visible.
- **AllowFilter**: Boolean property for enabling filtering on specific columns.

#### Methods
- **FilterGrid**: Method to apply the filtering criteria based on the AutoFilterRow settings.

### Code Examples

#### C# Example

```csharp
// Enabling the AutoFilterRow
gridGroupingControl1.ShowFilterBar = true;

// Enabling filtering for specific columns
gridGroupingControl1.TableDescriptor.Columns["Company Name"].AllowFilter = true;
gridGroupingControl1.TableDescriptor.Columns["Contact Name"].AllowFilter = true;

// Applying the filter settings
gridGroupingControl1.Refresh();
```

## RAG Annotations
<!-- 
tags: grid, auto-filter, filtering, grid-grouping, winforms, showfilterbar, allowfilter, syncfusion, essentiality, windows-forms 
keywords: AutoFilterRow, ShowFilterBar, AllowFilter, Grid Grouping, Windows Forms, filtering, data manipulation, user interaction 
-->
```