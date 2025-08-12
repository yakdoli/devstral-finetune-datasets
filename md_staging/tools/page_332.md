```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_332.jpeg
document_name: tools
page_number: 332
page_id: tools#page_332
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:05:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section explains how to assign a `DataSet` to the `AutoCompleteControl.DataSource` property of the `ComboBoxAutoComplete`.
- Demonstrates setting dropdown list column attributes for the `AutoComplete`.
- Describes how to apply Visual Styles to the `ComboBoxAutoComplete` control using the `VisualStyle` property.

## Content

### Assigning a `DataSet` to the `AutoCompleteControl.DataSource` Property

The `DataSet` is assigned to the `AutoCompleteControl.DataSource` property of the `ComboBoxAutoComplete` as follows:

```csharp
' Assign DataSet to the AutoCompleteControl.DataSource property of the ComboBoxAutoComplete.
Me.comboBoxAutoComplete1.AutoCompleteControl.DataSource = Me.dataSet11.Sports
Me.comboBoxAutoComplete1.DisplayMember = "Name"
```

#### Setting Column Attributes

The attributes of columns in the dropdown list of the `AutoComplete` can be set as follows:

```csharp
' Sets the attributes of columns in the drop down list of the AutoComplete.
Me.comboBoxAutoComplete1.AutoCompleteControl.Columns.Add(Me.autoCompleteDataColumnInfol)
Me.comboBoxAutoComplete1.AutoCompleteControl.Columns.Add(Me.autoCompleteDataColumnInfo2)

Me.autoCompleteDataColumnInfol.ColumnHeaderText = "Name"
Me.autoCompleteDataColumnInfol.MatchingColumn = True
Me.autoCompleteDataColumnInfo2.ColumnHeaderText = "ID"
```

#### Visual Representation

![ComboBoxAutoComplete with Sports Data](image.png)

**Figure 145: ComboBoxAutoComplete with Sports Data**

### Visual Styles

#### Subheading: Visual Styles

**Visual Styles for the ComboBoxAutoComplete control can be set using `VisualStyle` property. The styles are:**

- Default
- Office2007

#### Setting VisualStyles

##### C#

```csharp
this.comboBoxAutoComplete1.VisualStyle = Syncfusion.Windows.Forms.Tools.ThemedComboBoxStyles.Office2007;
this.comboBoxAutoComplete1.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Managed;
```

##### VB.NET

```vb
' Code example for VB.NET will follow the same structure but is not provided in the image.
```

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Class**: ComboBoxAutoComplete
- **Members**:
  - **Properties**:
    - `DataSource`: Sets the data source for the `AutoCompleteControl`.
    - `DisplayMember`: Specifies the name of the data member that is displayed to the user.
    - `VisualStyle`: Determines the visual style of the control.

## Code Examples

### C# Example

```csharp
// Assigning the DataSource and DisplayMember
this.comboBoxAutoComplete1.AutoCompleteControl.DataSource = this.dataSet11.Sports;
this.comboBoxAutoComplete1.DisplayMember = "Name";

// Adding columns to the AutoCompleteControl
this.comboBoxAutoComplete1.AutoCompleteControl.Columns.Add(this.autoCompleteDataColumnInfol);
this.comboBoxAutoComplete1.AutoCompleteControl.Columns.Add(this.autoCompleteDataColumnInfo2);

// Setting column attributes
this.autoCompleteDataColumnInfol.ColumnHeaderText = "Name";
this.autoCompleteDataColumnInfol.MatchingColumn = true;
this.autoCompleteDataColumnInfo2.ColumnHeaderText = "ID";

// Setting VisualStyle
this.comboBoxAutoComplete1.VisualStyle = Syncfusion.Windows.Forms.Tools.ThemedComboBoxStyles.Office2007;
this.comboBoxAutoComplete1.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Managed;
```

## Additional Notes

- The `DisplayStyle` property can be used to control how items are displayed in the dropdown list.
- The `MatchedItemCheckBlock` property can be set to customize the appearance of the checked item.

<!-- tags: [ComboBoxAutoComplete, DataSet, AutoCompleteControl, VisualStyles, Office2007, Windows Forms, Syncfusion Winforms, ComboBox] keywords: [DataSource, DisplayMember, ColumnHeaderText, MatchedColumn] -->
```