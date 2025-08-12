```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_235.jpeg
document_name: grid
page_number: 235
page_id: grid#page_235
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:04:27Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Splitter feature in Essential Grid for managing sections within the grid.
- Freeze Pane feature to keep specific rows or columns visible during scrolling.
- Support for specifying the number of frozen rows and columns in code.

## Content

### WinForms-specific aspects

#### Freeze Pane

##### Overview

- Essential Grid supports MS Excel-like **Freeze Pane** feature.
- Useful for keeping column or row labels visible in large spreadsheets.
- Allows freezing of either columns or rows so they remain visible while scrolling.
- The number of rows to be frozen is specified using `Model.Rows.FrozenCount`.
- The number of columns to be frozen is specified using `Model.Cols.FrozenCount`.

##### Enabling Freeze Pane

**C# Code Example**

```csharp
this.gridControl1.Model.Rows.FrozenCount = 4;
this.gridControl1.Model.Cols.FrozenCount = 3;
```

### Figures and Captions

- **Figure 127: Splitter**
  - ![Splitter](image.png)

## Code Examples

### C# Example for Enabling Freeze Pane

```csharp
// Enable freeze pane in Essential Grid
this.gridControl1.Model.Rows.FrozenCount = 4;
this.gridControl1.Model.Cols.FrozenCount = 3;
```

## RAG Annotations

<!-- tags: [Essential Grid, Windows Forms, Splitter, Freeze Pane, C#] keywords: [Freeze Pane, Model.Rows.FrozenCount, Model.Cols.FrozenCount, Splitter, Windows Forms, Essential Grid, gridControl1] -->
```