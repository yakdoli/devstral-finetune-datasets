```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_152.jpeg
document_name: grid
page_number: 152
page_id: grid#page_152
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:57:49Z
fidelity: lossless
-->

## winforms.grid.control.cell.type.combobox

### Overview
- Demonstrates configuring a cell to display a `ComboBox` in a grid control.
- Shows how to set up choices and integrate data sources with the `ComboBox`.
- Explains the properties like `CellType`, `ChoiceList`, `DisplayMember`, and `ValueMember` for customizing the `ComboBox` effectively.

### Content

#### Table Explanation

| Property             | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| data source        | The object to be displayed in the cell.                                      |
| ValueMember          | A string that names the public property from the data source object to be used as the value for this cell. |

The following code example illustrates how to set the cell type to ComboBox.

#### Code Examples

##### [C#]

```csharp
// Generate the choices.
StringCollection items = new StringCollection();
items.Add("One");
items.Add("Two");
items.Add("Three");
items.Add("Four");
items.Add("Five");

// Set up the control.
gridControl1[rowIndex, colIndex].CellType = "ComboBox";
gridControl1[rowIndex, colIndex].ChoiceList = items;
gridControl1[rowIndex, colIndex].Text = "Five";
gridControl1[rowIndex, colIndex].CellType = "ComboBox";
gridControl1[rowIndex, colIndex].ExclusiveChoiceList = true;

// Or use a data source such as a table in a data set.
gridControl1[2, 2].CellType = "ComboBox";
gridControl1[2, 2].DataSource = this.dataSet11.Tables["Customers"];
gridControl1[2, 2].DisplayMember = "CustomerID";
gridControl1[2, 2].ValueMember = "CustomerID";
```

##### [VB.NET]

```vb
' Generate the choices.
Dim items As StringCollection = New StringCollection()
items.Add("One")
items.Add("Two")
items.Add("Three")
items.Add("Four")
items.Add("Five")

' Set up the control.
gridControl1(rowIndex, colIndex).CellType = "ComboBox"
gridControl1(rowIndex, colIndex).ChoiceList = items
```

#### Setting Up Choices and Data Sources
The example demonstrates:
1. **Using a `StringCollection` for Choices:**
   - Creates a `StringCollection` and adds items to define the `ComboBox` options.
2. **Setting up the `ComboBox` Control:**
   - Configures the `CellType` property to `"ComboBox"`.
   - Assigns the `ChoiceList` to the predefined options.
   - Sets the `Text` property to select a default value.
3. **Using a Data Source:**
   - Binds the `ComboBox` to a data table (`Customers`) from a `DataSet`.
   - Defines `DisplayMember` and `ValueMember` to map the data source properties.

### API Reference

- **Properties:**
  - `CellType`: Specifies the type of control to be placed in the cell (e.g., `"ComboBox"`).
  - `ChoiceList`: Determines the options available in the `ComboBox`.
  - `DisplayMember`: Specifies the property of the data source object to be displayed in the cell.
  - `ValueMember`: Indicates the property of the data source object used as the value for the cell.

### Code Examples (Continued)

#### C# Example with Data Source Integration
```csharp
// Integrating with a data source.
gridControl1[2, 2].CellType = "ComboBox";
gridControl1[2, 2].DataSource = this.dataSet11.Tables["Customers"];
gridControl1[2, 2].DisplayMember = "CustomerID";
gridControl1[2, 2].ValueMember = "CustomerID";
```

### Summary
This section provides a detailed walkthrough on setting up a `ComboBox` within a grid cell, offering flexibility through both static choices and dynamic data sources. Users can leverage properties like `CellType`, `ChoiceList`, `DisplayMember`, and `ValueMember` to customize the behavior and display of the `ComboBox`.

### Page-level Navigation/TOC
- Overview
- Content
  - Table Explanation
  - Code Examples
    - [C#]
    - [VB.NET]
- API Reference
- Code Examples (Continued)

### Cross References
See also:
- Related grid customization guides
- Advanced data binding techniques

### RAG Annotations
<!-- tags: [Syncfusion, Winforms, Grid, ComboBox, DataBinding, TableProperty] keywords: [CellType, ChoiceList, DisplayMember, ValueMember, StringCollection, DataSet, Customers, CustomerID] -->
```
