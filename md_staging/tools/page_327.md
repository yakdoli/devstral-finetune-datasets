```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_327.jpeg
document_name: tools
page_number: 327
page_id: tools#page_327
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:06:32Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

The behavior settings of a ComboBoxAutoComplete control includes the below properties.

| ComboAutoComplete Properties                       | Description                                                                 |
|----------------------------------------------------|-----------------------------------------------------------------------------|
| AllowNewText                                       | Specifies whether the user is allowed to enter new text. User can be allowed to enter new text in the ComboBoxAutoComplete by setting AllowNewText to true. AllowNewText is mainly used to prevent items that are not in the list while validating. |
| ReadOnly                                           | Gets or Sets value indicating whether changes can be done to the combobox.                                                        |
| UpdateComboSelectionProperties                    | UpdateComboSelectionProperties set to true means the Property SelectedItem will return the AutoCompleteControl's SelectedItem. Else if it is set to false, then SelectedItem property should return the base class SelectedItem ie., the Windows ComboBox SelectedItem value. |

```csharp
this.comboBoxAutoCompletel.AllowNewText= true;
this.comboBoxAutoCompletel.ReadOnly = true;
this.comboBoxAutoCompletel.UpdateComboSelectionProperties = false;
```

```vb.net
Me.comboBoxAutoCompletel.AllowNewText= True
Me.comboBoxAutoCompletel.ReadOnly = True
Me.comboBoxAutoCompletel.UpdateComboSelectionProperties = False
```

### Refreshing the Columns

When the datasource of the AutoComplete control is set to a valid datasource through the designer, the "Refresh Columns" verb can be clicked to automatically populate the Columns collection. This option is available in the context menu of the ComboBoxAutoComplete control and also as property grid command.

<!-- tags: [Syncfusion Winforms, ComboBoxAutoComplete, AutoCompleteControl, Designer, PropertyGrid] keywords: [ComboBoxAutoComplete, AllowNewText, ReadOnly, UpdateComboSelectionProperties, Refresh Columns, Designer, PropertyGrid, Control, AutoComplete, Behavior, Settings] -->
```