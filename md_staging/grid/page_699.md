```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_699.jpeg
document_name: grid
page_number: 699
page_id: grid#page_699
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:34:34Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Adding Unbound Columns with Checkboxes

#### Step 1: Define an Unbound Field

The following code demonstrates how to add an unbound field to the `TableDescriptor` of the `gridGroupingControl1`.

**VB.NET Example:**

```vb
Dim unboundField As FieldDescriptor = New FieldDescriptor("CheckboxCol", "", False, "")
unboundField.ReadOnly = False
Me.gridGroupingControl1.TableDescriptor.UnboundFields.Add(unboundField)
```

#### Step 2: Configure Checkboxes in the Unbound Column

You can customize the appearance and behavior of the checkboxes in the unbound column through the `Appearance` property of the column.

**C# Example:**

```csharp
gridGroupingControl1.TableDescriptor.Columns["CheckboxCol"].Appearance.AnyRecordFieldCell.CellType = "CheckBox";
gridGroupingControl1.TableDescriptor.Columns["CheckboxCol"].Appearance.AnyRecordFieldCell.CheckBoxOptions.CheckedValue = "True";
gridGroupingControl1.TableDescriptor.Columns["CheckboxCol"].Appearance.AnyRecordFieldCell.CheckBoxOptions.UncheckedValue = "False";
gridGroupingControl1.TableDescriptor.Columns["CheckboxCol"].Appearance.AnyRecordFieldCell.HorizontalAlignment = GridHorizontalAlignment.Center;
gridGroupingControl1.TableDescriptor.Columns["CheckboxCol"].Appearance.AnyRecordFieldCell.VerticalAlignment = GridVerticalAlignment.Middle;
```

**VB.NET Equivalent:**

```vb
gridGroupingControl1.TableDescriptor.Columns("CheckboxCol").Appearance.AnyRecordFieldCell.CellType = "CheckBox"
gridGroupingControl1.TableDescriptor.Columns("CheckboxCol").Appearance.AnyRecordFieldCell.CheckBoxOptions.CheckedValue = "True"
gridGroupingControl1.TableDescriptor.Columns("CheckboxCol").Appearance.AnyRecordFieldCell.CheckBoxOptions.UncheckedValue = "False"
gridGroupingControl1.TableDescriptor.Columns("CheckboxCol").Appearance.AnyRecordFieldCell.HorizontalAlignment = GridHorizontalAlignment.Center
gridGroupingControl1.TableDescriptor.Columns("CheckboxCol").Appearance.AnyRecordFieldCell.VerticalAlignment = GridVerticalAlignment.Middle
```

#### Step 3: Handle QueryValue and SaveValue Events

To manage the unbound values effectively, you can handle the `QueryValue` and `SaveValue` events. A `HashTable` can be used to store and retrieve the unbound values.

**C# Example:**

```csharp
Hashtable unboundValues = new Hashtable();

private void gridGroupingControl1_QueryValue(object sender, FieldValueEventArgs e)
{
    // Logic to retrieve and set the unbound value
}

private void gridGroupingControl1_SaveValue(object sender, FieldValueEventArgs e)
{
    // Logic to save the unbound value
}
```

### Summary

The steps outlined here provide a structured approach to adding unbound columns with checkboxes to a `GridGroupingControl`. By configuring the `CellType`, `CheckedValue`, and alignment properties, you can ensure that the checkboxes function as intended. Additionally, handling `QueryValue` and `SaveValue` events ensures that the unbound values are managed effectively.

## API Reference

### GridGroupingControl

- **Properties:**
  - `TableDescriptor`: Provides access to the description of the table, including columns and their properties.
  - `UnboundFields`: Allows the addition of unbound fields for dynamic or calculated columns.
  - `Appearance`: Controls the visual appearance of individual cells.

- **Events:**
  - `QueryValue`: Triggered when the grid needs to retrieve the value for a cell.
  - `SaveValue`: Triggered when the grid needs to save the value for a cell.

### FieldDescriptor

- **Parameters:**
  - `Name`: Name of the field (e.g., "CheckboxCol").
  - `Caption`: Caption displayed for the field.
  - `ReadOnly`: Indicates whether the field is read-only.
  - `Unbound`: Indicates whether the field is unbound.

### CheckBoxOptions

- **Options:**
  - `CheckedValue`: Value assigned when the checkbox is checked.
  - `UncheckedValue`: Value assigned when the checkbox is unchecked.

### Alignment

- **Horizontal Alignment:**
  - `GridHorizontalAlignment.Center`: Centers the content horizontally.
- **Vertical Alignment:**
  - `GridVerticalAlignment.Middle`: Centers the content vertically.

## Code Examples

The provided code snippets demonstrate how to configure unbound columns with checkboxes and handle their values effectively in both C# and VB.NET.

### RAG Annotations

Try to use tags and keywords that are as specific and descriptive as possible based on the provided content. The example here incorporates essential terms and concepts for this specific functionality within Syncfusion's WinForms library.

<!-- tags: [syncfusion, grid, unbound-columns, checkboxes, windows-forms, queryvalue, savevalue] keywords: [unboundfield, celltype, checkedvalue, uncheckedvalue, horizontalalignment, verticalalignment, hashtable, gridgroupingcontrol, queryvalueevent] -->
```