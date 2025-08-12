```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_303.jpeg
document_name: tools
page_number: 303
page_id: tools#page_303
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:05:01Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Implementation of AutoComplete with Multiple Columns

Here's how to implement an `AutoComplete` feature with multiple columns in both C# and VB.NET:

#### C#
```csharp
this.autoComplete2.Columns.Add(this.autoCompleteDataColumnInf0);
this.autoComplete2.Columns.Add(this.autoCompleteDataColumnInfo2);
this.autoComplete2.ShowColumnHeader = true;
this.autoComplete2.MatchMode = AutoCompleteMatchModes.Automatic;

this.autoCompleteDataColumnInf0.ColumnHeaderText = "Title";
this.autoCompleteDataColumnInf0.MatchingColumn = true;
this.autoCompleteDataColumnInf0.Visible = true;
```

#### VB.NET
```vb.net
Me.autoComplete2.Columns.Add(Me.autoCompleteDataColumnInf0)
Me.autoComplete2.Columns.Add(Me.autoCompleteDataColumnInfo2)
Me.autoComplete2.ShowColumnHeader = True
Me.autoComplete2.MatchMode = AutoCompleteMatchModes.Automatic

Me.autoCompleteDataColumnInf0.ColumnHeaderText = "Title"
Me.autoCompleteDataColumnInf0.MatchingColumn = True
Me.autoCompleteDataColumnInf0.Visible = True
```

### Visual Representation of AutoComplete with Multiple Columns

![AutoComplete Popup with Multiple Columns](https://via.placeholder.com/600x300?text=Figure+131%3A+AutoComplete+Popup+with+Multiple+Columns)

**Figure 131**: AutoComplete Popup with Multiple Columns

### Adding Columns from External Sources

Columns can be added to match external sources as well. A sample demonstrating this feature is available at the following location:

**Directory Path**  
`.` \\ My Documents \\ Syncfusion \\ EssentialStudio \\ **Version Number** \\ Windows \\ Tools.Windows \\ Samples \\ 2.0 \\ Editors Package \\ AutoCompleteDemo

## Cross References

See also:
- [Syncfusion WinForms Documentation](#)
- [AutoComplete Tools Overview](#)
- [External Data Source Integration](#)

<!-- tags: [syncfusion, windows forms, autocomplete, multiple columns, external sources] keywords: [autosuggest, multi-column autocomplete, vb.net, c#, syncfusion tools, data binding, external data integration, auto-complete dropdown, search, matching columns] -->
```
