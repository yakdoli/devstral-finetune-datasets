```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_330.jpeg
document_name: tools
page_number: 330
page_id: tools#page_330
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:07:18Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to fill a DataSet with data from a database.
- Explains adding columns to a popup in a ComboBoxAutoComplete control.
- Includes both C# and VB.NET code examples for populating a DataSet.

## Content

6. Enter the following code in the Load event of your form to fill the `DataSet` with data from the database.

### Filling a DataSet with Data

#### External DataSource Table

![Sports Query](https://example.com/assets/Sports_Query_C_acc_mdb.png)

**Figure 143: External DataSource Table**

The `Sports` table contains the following data:

| id  | Name       |
|-----|------------|
| 1   | Football   |
| 2   | Basketball |
| 3   | Baseball   |
| NULL| NULL       |

##### C# Code Example:
```csharp
// Fills the DataSet with data from the database.
this.oleDbDataAdapter1.Fill(this.dataSet11);
```

##### VB.NET Code Example:
```vb
' Fills the DataSet with data from the database.
Me.oleDbDataAdapter1.Fill(Me.dataSet11)
```

### Adding Columns to the Popup and Setting the Matching Column

#### Adding Columns via Designer

Add columns through the designer using the `ComboBoxAutoComplete.AutoCompleteControl.Columns` property. Set the first column as the matching column.

## API Reference
- **Methods:**
  - `Fill`: Populates the DataSet from the database.

## Code Examples
-
```csharp
// C# Example
this.oleDbDataAdapter1.Fill(this.dataSet11);
```

```vb
' VB.NET Example
Me.oleDbDataAdapter1.Fill(Me.dataSet11)
```

#### Designer Process:
- Access the `ComboBoxAutoComplete` control's `AutoCompleteControl` property.
- Add columns by configuring the `Columns` property.
- Set the first column as the matching column.

## Cross References
- See also: Database connectivity examples in the Syncfusion Windows Forms documentation.

<!-- tags: [windows forms, combobox autocomplete, dataset, data binding, c#, vb.net] keywords: [sports table, auto complete control, columns, matching column, fill dataset] -->
```