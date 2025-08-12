```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_778.jpeg
document_name: grid
page_number: 778
page_id: grid#page_778
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:42:46Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Learn how to set up a filter bar in the GridGroupingControl.
- Enable the filter bar and customize its appearance.
- Allow filtering for specific columns programmatically or via the designer.

## Content

### Setting up a Filter Bar

The Filter Bar can be enabled by setting the `ShowFilterBar` and `AllowFilter` properties to `true`. The `AllowFilter` property can be set for the columns that require filter options.

Given below is the code to set the filter for all the columns in the main table.

#### Code Examples

**[C#]**
```csharp
// Show Filter Bar for the main table.
this.gridGroupingControl.TopLevelGroupOptions.ShowFilterBar = true;

// Change the appearance of the Filter Row.
this.gridGroupingControl.TableDescriptor.Appearance.FilterBarCell.BackColor = Color.Cornsilk;

// Enable filter for all columns.
for (int i = 0; i < gridGroupingControl1.TableDescriptor.Columns.Count; i++)
gridGroupingControl1.TableDescriptor.Columns[i].AllowFilter = true;
```

**[VB.NET]**
```vbnet
' Show Filter Bar for the main table.
Me.gridGroupingControl1.TopLevelGroupOptions.ShowFilterBar = True

' Change the appearance of the Filter Row .
Me.gridGroupingControl1.TableDescriptor.Appearance.FilterBarCell.BackColor = Color.AliceBlue

' Enable the filter for all columns.
Dim i As Integer = 0
Do While i < gridGroupingControl1.TableDescriptor.Columns.Count
gridGroupingControl1.TableDescriptor.Columns(i).AllowFilter = True
i += 1
Loop
```

### Through Designer

A filter bar can also be added at design time by setting the above properties through the property window of the grouping grid. The designer settings shown below adds the filter for the columns `CompanyName` and `ContactTitle`.

## Page-level Navigation/TOC (if applicable)
- [Unclear, as no explicit global or local TOC is present on this page]

## Cross References
- See also: other sections on GridGroupingControl customization and filter options.

<!-- tags: [Syncfusion Winforms, GridGroupingControl, FilterBar, AllowFilter] keywords: [Grid, Filter, Designer, Appearance, Column, Customization] -->
```
