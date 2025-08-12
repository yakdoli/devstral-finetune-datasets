```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_331.jpeg
document_name: tools
page_number: 331
page_id: tools#page_331
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:06:45Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

Figure 144: Adding Columns "Name" and "ID" According to External Data Source

Using the below code, assign the dataset as the data source for the ComboBoxAutoComplete control.

## C#

```csharp
// Assign DataSet to the AutoCompleteControl.DataSource property of the ComboBoxAutoComplete.
this.comboBoxAutoCompletel.AutoCompleteControl.DataSource = this.dataSet1.Sports;
this.comboBoxAutoCompletel.DisplayMember = "Name";

// Sets the attributes of columns in the drop down list of the AutoComplete.
this.comboBoxAutoCompletel.AutoCompleteControl.Columns.Add(this.autoCompleteDataColumnInfo1);
this.comboBoxAutoCompletel.AutoCompleteControl.Columns.Add(this.autoCompleteDataColumnInfo2);

this.autoCompleteDataColumnInfo1.ColumnHeaderText = "Name";
this.autoCompleteDataColumnInfo1.MatchingColumn = true;
this.autoCompleteDataColumnInfo2.ColumnHeaderText = "ID";
```

## VB.NET

```vb
' VB.NET code would go here, but it's not provided in the image.
```

## API Reference
- Properties:
  - `AutoCompleteControl.DataSource`: Sets the data source for the AutoCompleteControl.
  - `AutoCompleteControl.DisplayMember`: Specifies the member to display in the AutoComplete dropdown.
  - `AutoCompleteControl.Columns`: Collection of columns to display in the dropdown list.

## Code Examples
- The above C# code demonstrates how to configure the ComboBoxAutoComplete with a dataset and set up the columns for the dropdown list.

## Cross References
See also:
- [AutoCompleteControl Core Features](#anchor: tools#page_331#autocompleterò-features)
- [Working with DataSources](#anchor: tools#page_331#working-with-datasources)

<!-- tags: WinForms, AutoCompleteControl, ComboBox, DataSource, DataRows, ColumnAttributes, API Reference keywords: AutoCompleteControl, ComboBoxAutoComplete, DataSource, ColumnHeaders, MatchingColumn, DisplayMember -->
```  
