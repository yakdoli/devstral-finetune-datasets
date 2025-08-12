```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_920.jpeg
document_name: grid
page_number: 920
page_id: grid#page_920
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:49:36Z
fidelity: lossless
-->

## Overview
- This page discusses customization of the selection colors in the `gridGroupingControl` using `SelectionBackColor` and `SelectionTextColor` properties in both C# and VB.NET.
- It highlights two specific options for selection colors: `ApplySelectionColor` and `DrawAlphablend`.

### Content
The text demonstrates how to customize the appearance of selected rows in a grid:

```csharp
this.gridGroupingControl1.TableOptions.SelectionTextColor = Color.Green;
```

```vb.net
Me.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.ApplySelectionColor
Me.gridGroupingControl1.TableOptions.SelectionBackColor = Color.PaleGreen
Me.gridGroupingControl1.TableOptions.SelectionTextColor = Color.Green
```

The effect of the above settings is shown in the following figure:

![](https://i.imgur.com/1.png "Figure 336: SelectionBackcolor = \"PaleGreen\" and SelectionTextcolor = \"Green\"")

#### Figure 336: SelectionBackcolor = "PaleGreen" and SelectionTextcolor = "Green"

- **Draw Alphablend**
  - This option draws alphablending over the selected row.

##### Code Example: Draw Alphablend

```csharp
this.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.DrawAlphablend;
```

```vb.net
Me.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.DrawAlphablend
```

## API Reference
- **Properties**
  - `TableOptions.ListBoxSelectionColorOptions`: Specifies the selection color option for the grid.
  - `TableOptions.SelectionBackColor`: Sets the background color for selected rows.
  - `TableOptions.SelectionTextColor`: Sets the text color for selected rows.

## Code Examples

### C# Example
```csharp
this.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.DrawAlphablend;
this.gridGroupingControl1.TableOptions.SelectionBackColor = Color.PaleGreen;
this.gridGroupingControl1.TableOptions.SelectionTextColor = Color.Green;
```

### VB.NET Example
```vb.net
Me.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.DrawAlphablend
Me.gridGroupingControl1.TableOptions.SelectionBackColor = Color.PaleGreen
Me.gridGroupingControl1.TableOptions.SelectionTextColor = Color.Green
```

<!-- tags: [gridGroupingControl, selectioncolor, drawalphablend, applyselectioncolor] keywords: [grid, selection, backcolor, textcolor, customization, alphablending] -->
```