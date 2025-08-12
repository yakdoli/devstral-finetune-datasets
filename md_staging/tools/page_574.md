```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_574.jpeg
document_name: tools
page_number: 574
page_id: tools#page_574
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:21:41Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
Me.comboBoxAdv1.AutoComplete = True
Me.comboBoxAdv1.CaseSensitiveAutocomplete = True
Me.comboBoxAdv1.MatchFirstCharacterOnly = True
```

![Figure 354: AutoComplete = "True"](attachment://image_file_name_1)

## 3.5.5.2.3.3.2 Data Binding

ComboBoxAdv control can be bound with external data source. Objects that can act as Datasource to ComboBoxAdv are:

- ArrayList
- DataView
- DataTable

We can add objects to the ComboBoxAdv by using the Items method. You can also add objects to a ComboBoxAdv using the DataSource, DisplayMember, and Valuemember properties to fill the ComboBox.

When the DataSource property is set, we cannot modify the items collection. If setting the DataSource property causes the data source to change, the Datasource event is raised. If setting this property causes the data member to change, the DisplayMember event is raised.

When you set DataSource to a null reference, DisplayMember is set to an empty string ("").

ComboBoxAdv can be bound to DataView using the following code snippet.

```csharp
[C#]

// Create a DataTable.
DataTable dt = new DataTable("Table1");

// Adding Columns.
dt.Columns.Add("FirstName");
dt.Columns.Add("LastName");
dt.Columns.Add("occupation");
dt.Columns.Add("place");
```

## Page-level Navigation/TOC (if applicable)
- Essential Tools for Windows Forms
- Data Binding

## RAG Annotations
<!-- tags: [product, comboboxadv, data binding, version: 11.4.0.26] keywords: [ComboBoxAdv, AutoComplete, DataView, DataTable, DataSource, DisplayMember, Valuemember] -->
```