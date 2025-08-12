```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_153.jpeg
document_name: grid
page_number: 153
page_id: grid#page_153
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:58:46Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes how to configure ComboBox cells in `gridControl` with custom data sources and AutoComplete support.
- Demonstrates the use of `CellType`, `DataSource`, `DisplayMember`, and `ValueMember` properties.
- Highlights the AutoComplete feature for ComboBox cells, including different modes such as `AutoComplete`, `AutoSuggest`, and `Both`.

## Content

```csharp
gridControl1(rowIndex, colIndex).Text = "Five"
gridControl1(rowIndex, colIndex).CellType = "ComboBox"
gridControl1(rowIndex, colIndex).ExclusiveChoiceList = True

' Or use a data source such as a table in a dataset.
gridControl1(2, 2).CellType = "ComboBox"
gridControl1(2, 2).DataSource = Me.dataSet1.Tables("Customers")
gridControl1(2, 2).DisplayMember = "CustomerID"
gridControl1(2, 2).ValueMember = "CustomerID"
```

### Figure 78: Combo Box Cells

<details>
<summary>Figure: ComboBox Cells</summary>

```markdown
| ComboBox Cells - both editable (with autocomplete) and dropdown only |
|-------------|-------------|-------------|-------------|-------------|
| Five        |             | Three       |             |             |
|             |             | One         |             |             |
|             |             | Two         |             |             |
|             |             | **Three**   |             |             |
|             |             | Four        |             |             |
|             |             | Five        |             |             |
|             |             | Six         |             |             |
```
</details>

### 4.1.4.1.3.1 AutoComplete Support for Combo Box in Edit Mode

Essential Grid provides AutoComplete support for combo box cells. The AutoComplete feature is a filtered suggestion list presented in a drop-down that is pulled from a mapped data source as the user enters text into a text box. AutoComplete for combo box cells provides the following properties:

- **AutoComplete**—Displays suggestion in the text box. The content other than what you have typed will be highlighted.
- **AutoSuggest**—Dynamically populates a list based on the entered text.
- **Both**—Enables normal editable behavior.
- **None**—No operations will be performed in the text box and list box areas.

#### Use Case Scenarios

You can choose the suggestion instead of typing the entire content.

#### Properties

## API Reference

### Properties
- `CellType` - Determines the type of cell (e.g., "ComboBox").
- `DataSource` - Specifies the data source for the combo box.
- `DisplayMember` - Defines the property of the data source that is shown to the user.
- `ValueMember` - Defines the property of the data source that is stored as the value of the combo box.
- `ExclusiveChoiceList` - Controls whether the user can type values not present in the combo box's data source.
- `AutoComplete` - Specifies the AutoComplete behavior for the combo box cell.

## Code Examples
```csharp
// Configuring a ComboBox cell with a data source
gridControl1(2, 2).CellType = "ComboBox";
gridControl1(2, 2).DataSource = Me.dataSet1.Tables("Customers");
gridControl1(2, 2).DisplayMember = "CustomerID";
gridControl1(2, 2).ValueMember = "CustomerID";
```

## RAG Annotations
<!-- tags: [Essential Grid, Windows Forms, ComboBox, AutoComplete, AutoSuggest, Data Source, DisplayMember, ValueMember] keywords: [gridControl, CellType, DataSource, DisplayMember, ValueMember, ExclusiveChoiceList, AutoComplete] -->
```