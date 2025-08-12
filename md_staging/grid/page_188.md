```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_188.jpeg
document_name: grid
page_number: 188
page_id: grid#page_188
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:01:40Z
fidelity: lossless
-->

## Overview

- This page explains the configuration of cell behavior in the Essential Grid for Windows Forms, including the `ShowCurrentCellBorderBehavior` and `RefreshCurrentCellBehavior` properties.
- It provides examples in C# and VB.NET for setting these properties.
- It discusses the refresh behavior of cells and the options available through the `GridRefreshCurrentCellBehavior` enumeration.

## Content

### 1. Using C#

```csharp
this.gridControl1.ShowCurrentCellBorderBehavior = GridShowCurrentCellBorder.AlwaysVisible;
```

### 2. Using VB.NET

```vb.net
Me.gridControl1.ShowCurrentCellBorderBehavior = GridShowCurrentCellBorder.AlwaysVisible
```

### 4.1.4.2.9 Refreshing Behavior of Current Cell

#### Overview
The Grid property, `RefreshCurrentCellBehavior`, determines the behavior of refreshing the cells while the focus is moved from current cell to another. The `GridRefreshCurrentCellBehavior` enumeration specifies which cells to refresh when the focus is moved from current cell to another.

#### Notes
- **Refreshing behavior of the cells enables them to display the current data automatically after updates.**
- **Refreshing the cells denote reloading the cell's value.**

#### Options in the `GridRefreshCurrentCellBehavior` Enumeration
- **None:**
  - Setting `ShowCurrentCellBorderBehavior` property with this option does not initiate refresh when moving the current cell.
- **RefreshCell:**
  - Setting `ShowCurrentCellBorderBehavior` property with this option refreshes the current cell only.
- **RefreshRow:**
  - Setting `ShowCurrentCellBorderBehavior` property with this option refreshes the entire row to which the current cell belongs. Use this setting if you are using `GridShowButtons.ShowCurrentRow`.

#### Example: Setting `RefreshCurrentCellBehavior` Property

##### 1. Using C#

```csharp
this.gridControl1.RefreshCurrentCellBehavior =
```

## API Reference
- **Properties:**
  - `ShowCurrentCellBorderBehavior`: Controls the visibility of the current cell border.
  - `RefreshCurrentCellBehavior`: Controls the behavior of refreshing cells when the focus changes.

## Code Examples (multi-language supported)

### C#

```csharp
this.gridControl1.ShowCurrentCellBorderBehavior = GridShowCurrentCellBorder.AlwaysVisible;
this.gridControl1.RefreshCurrentCellBehavior = GridRefreshCurrentCellBehavior.RefreshRow;
```

### VB.NET

```vb.net
Me.gridControl1.ShowCurrentCellBorderBehavior = GridShowCurrentCellBorder.AlwaysVisible
Me.gridControl1.RefreshCurrentCellBehavior = GridRefreshCurrentCellBehavior.RefreshRow
```

## References
- Refer to the Essential Grid documentation for more details on these properties and behaviors.

### Known Bugs and Add-ons
- None reported at this time.

## RAG Annotations

- **Tags:** 
  - grid,
  - windows-forms,
  - current-cell-behavior,
  - refresh-behavior,
  - syncfusion-sdk
  
- **Keywords:** 
  - Grid,
  - Windows Forms,
  - Current Cell,
  - Refresh Behavior,
  - ShowCurrentCellBorderBehavior,
  - RefreshCurrentCellBehavior,
  - GridShowCurrentCellBorder,
  - GridRefreshCurrentCellBehavior,
  - Essential Grid,
  - Syncfusion Winforms,
  - C#,
  - VB.NET,
  - API Documentation.
```
