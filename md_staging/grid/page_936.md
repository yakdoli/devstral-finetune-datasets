```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_936.jpeg
document_name: grid
page_number: 936
page_id: grid#page_936
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:50:33Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
this.gridGroupingControl1.Table.SelectedRecords.Clear();
```

```vb
Me.gridGroupingControl1.Table.SelectedRecords.Clear()
```

> **Note:** For more details, refer the following browser sample:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Selection\Multi Record Selection Demo
```

## 4.3.4.7.5 Selected Ranges Collection

The selections that are made by the user are saved into a collection named `TableModel.SelectedRanges`. If the Selection option is turned on, then the grid will always listen to the selections that are being made and records all those selections into the `SelectedRanges` collection. You can loop through every selection range of this collection to get the information about the records that have been selected. The `SelectedRanges.ActiveRange` property gives the current selection range (i.e., last range in the collection).

### Example

This example shows how to loop through the `SelectedRanges` collection to retrieve the information about the records that are being selected.

1. Turn on any type of selection. Here the record-based selection is active. It is enabled by setting the `ListBoxSelectionMode` property to a value other than `None`. You could set the selection colors as well.

#### Code Example

```csharp
this.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.MultiExtended;
this.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.DrawAlphablend;
this.gridGroupingControl1.TableModel.Options.AlphaBlendSelectionColor = Color.Red;
```

## Page-level Navigation/TOC

- [Installation and Usage]
- [Selected Ranges Collection]
- [Example: Retrieving Selected Records]

## API Reference

### Namespace: Syncfusion.Windows.Forms.Grid

#### Properties
- `SelectedRecords`
- `SelectedRanges`
- `ActiveRange`
- `ListBoxSelectionMode`

#### Methods
- `Clear()`

### Code Examples

#### C#

```csharp
this.gridGroupingControl1.Table.SelectedRecords.Clear();
this.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.MultiExtended;
this.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.DrawAlphablend;
this.gridGroupingControl1.TableModel.Options.AlphaBlendSelectionColor = Color.Red;
```

```vb
Me.gridGroupingControl1.Table.SelectedRecords.Clear()
Me.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.MultiExtended
Me.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.DrawAlphablend
Me.gridGroupingControl1.TableModel.Options.AlphaBlendSelectionColor = Color.Red
```

## Cross References

See also:
- [Grid Grouping Control Overview]
- [Selection Modes in Grid Grouping Control]
- [Customizing Selection Colors]

<!-- tags: [syncfusion, windows forms, grid, essentialstudio, version 11.4.0.26] keywords: [record selection, selected ranges, active range, grid grouping control, selection mode, selection colors, sample code, user guide] -->
```