```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_319.jpeg
document_name: tools
page_number: 319
page_id: tools#page_319
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:06:05Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Initialization

```csharp
Dim autoComplete1 As Syncfusion.Windows.Forms.Tools.AutoComplete = New Syncfusion.Windows.Forms.Tools.AutoComplete
Dim richTextBox1 As MyRichTextBox = New MyRichTextBox
```

### Overview

- The AutoComplete control can take an external data source (any data source that implements IList or IListSource) for its history list. Here we have set a StringCollection as the DataSource.
- When this property is set, the AutoComplete control will initialize itself with the data source and use that as the basis for its matching routines. For example, if you have a DataSet with a list of names of the States in the US and if you specify that as the DataSource, then the AutoComplete control will display all the matches from within these names when the user types in the target edit control.

### Setting the DataSource

#### [C#]

```csharp
// Sets the DataSource.
StringCollection liste = new StringCollection();
    liste.Add("New Jersey");
    liste.Add("North Carolina");
    liste.Add("North Dakota");
    liste.Add("New York");
    liste.Add("New Mexico");
autoComplete1.DataSource = liste;
```

#### [VB.NET]

```vb
' Sets the DataSource.
Dim liste As StringCollection = New StringCollection
    liste.Add("New Jersey")
    liste.Add("North Carolina")
    liste.Add("North Dakota")
    liste.Add("New York")
    liste.Add("New Mexico")
autoComplete1.DataSource = liste
```

### Configuring AutoComplete Modes

- Set the AutoCompleteonAutoComplete1 property in the properties page to either AutoSuggest, AutoAppend or Both.
- SetAutoComplete is the extended property for the AutoComplete property which, will be called by the framework when the AutoComplete property is set on any control. When using the AutoComplete control programmatically, you need to use this method to add and remove auto completion for the RichTextBox control.

#### [C#]

```csharp
this.autoComplete1.SetAutoComplete(this.richTextBox1, Syncfusion.Windows.Forms.Tools.AutoCompleteModes.AutoSuggest);
```

### Cross References

- Related topics and controls can be found in the [Syncfusion WinForms documentation](https://www.syncfusion.com/products/windowsforms/documentation).
```