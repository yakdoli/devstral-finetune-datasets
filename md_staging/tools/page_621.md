```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_621.jpeg
document_name: tools
page_number: 621
page_id: tools#page_621
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:23:40Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Displaying a Single Column in a ListBox

#### How to display single column in a ListBox?

To turn off showing multiple columns in a ListBox, follow the below given steps.

1. Access the `GridListControl` and set its `MultiColumn` property to `False`.

   ```csharp
   // Turns off multiple columns display.
   this.multiColumnBoundCombo.ListBox.MultiColumn = false;
   ```

   ```vb.net
   ' Turns off multiple columns display.
   Me.multiColumnBoundCombo.ListBox.MultiColumn = False
   ```

2. The dropdown will then simply show the first column in the bound datasource (the combo's `DisplayMember` property will not be consulted here). Make sure that in your SQL query, the desired column to be shown in the drop-down is the first one.

### How to hide an unnecessary column from the multiple columns

MultiColumnComboBox allows us to hide unnecessary columns. If you want to hide a particular column, follow this method anywhere in code but before displaying the dropdown.

```csharp
Syncfusion.Windows.Forms.Grid.GridColHidden gch = new
Syncfusion.Windows.Forms.Grid.GridColHidden(3); // Hides column number '3'
multiColumnComboBox1.ListBox.Grid.ColHiddenEntries.Add(gch);
```

```vb.net
Dim gch As Syncfusion.Windows.Forms.Grid.GridColHidden = New
Syncfusion.Windows.Forms.Grid.GridColHidden(3) 'Hides column number '3'
multiColumnComboBox1.ListBox.Grid.ColHiddenEntries.Add(gch)
```

This will hide the 3rd column. If you want to disable more columns, repeat this step by the respective column number.

### How to retrieve the columns other than Display and Value members in a MultiColumnComboBox

Handle the `SelectedIndexChanged` Event of `MultiColumnComboBox` as shown below in order to retrieve respective column values.

## Footer
© 2013 Syncfusion. All rights reserved.  
Page 621
```

<!-- tags: [product, module, control, api, version?] keywords: [Essential Tools, Windows Forms, GridListControl, MultiColumn, ListBox, MultiColumnComboBox, DisplayMember, SelectedIndexChanged] -->
```