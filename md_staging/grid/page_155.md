```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_155.jpeg
document_name: grid
page_number: 155
page_id: grid#page_155
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:58:46Z
fidelity: lossless
-->

## Overview

- Demonstrates how to configure dropdown styles and grid combo selection options using properties in Essential Grid for Windows Forms.
- Provides examples in C# and VB.NET to set these configurations.
- Explains the use of the `Control` cell type for placing arbitrary controls in grid cells.

## Content

### Setting the Dropdown Style to Editable

2. Set the Dropdown style as Editable as given in the following code:

```csharp
[C#]
this.gridControl1[RowIndex, ColIndex].DropDownStyle = GridDropDownStyle.Editable;
```

```vb
[VB]
Me.gridControl1(RowIndex, ColIndex).DropDownStyle = GridDropDownStyle.Editable
```

### Setting GridComboSelectionOptions

3. Set the `GridComboSelectionOptions` using the `AutoCompleteInEditMode` property as given in the following code:

```vb
[VB]
Me.gridControl1(RowIndex, ColIndex).AutoCompleteInEditMode = GridComboSelectionOptions.AutoSuggest
```

```vb
[VB]
Me.gridControl1(RowIndex, ColIndex).AutoCompleteInEditMode = GridComboSelectionOptions.AutoSuggest
```

### 4.1.4.1.4 Control

You can place an arbitrary control in a grid cell through the `Control` cell type. This cell type differs from most other cell types shipped with Essential Grid in which it cannot be shared among several cells. The Control cell type requires you to instantiate a control object for each cell that uses this cell type, and set that object to `style.Control`. A different control object is required for every cell that makes use of the Control cell type.

## API Reference

- `GridDropDownStyle.Editable`: Used to set the dropdown style to editable.
- `GridComboSelectionOptions.AutoSuggest`: Enables auto-suggestion in edit mode.

## Code Examples

- **C# Example**: Setting the dropdown style as editable.
  ```csharp
  this.gridControl1[RowIndex, ColIndex].DropDownStyle = GridDropDownStyle.Editable;
  ```

- **VB.NET Example**: Setting the dropdown style as editable.
  ```vb
  Me.gridControl1(RowIndex, ColIndex).DropDownStyle = GridDropDownStyle.Editable
  ```

- **C# Example**: Configuring `GridComboSelectionOptions` for auto-suggestion.
  ```csharp
  this.gridControl1[RowIndex, ColIndex].AutoCompleteInEditMode = GridComboSelectionOptions.AutoSuggest;
  ```

- **VB.NET Example**: Configuring `GridComboSelectionOptions` for auto-suggestion.
  ```vb
  Me.gridControl1(RowIndex, ColIndex).AutoCompleteInEditMode = GridComboSelectionOptions.AutoSuggest
  ```

## RAG Annotations
<!-- tags: [Essential Grid, Windows Forms, Dropdown Style, GridComboSelectionOptions, Control Cell Type, Syncfusion Windows Forms] keywords: [GridDropDownStyle.Editable, GridComboSelectionOptions.AutoSuggest, Control cell type, cell control instantiation] -->
```