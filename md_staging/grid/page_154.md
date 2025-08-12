```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_154.jpeg
document_name: grid
page_number: 154
page_id: grid#page_154
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:57:40Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Properties Table

| Property    | Description                                                                 | Type        | Data Type | Reference links |
|-------------|-----------------------------------------------------------------------------|-------------|-----------|-----------------|
| AutoComplete | Gets the a <br> suggestion from <br> the list based on <br> the entered text. <br> The suggestion <br> will be <br> highlighted. | Enumerator   | N/A         | N/A             |
| AutoSuggest | Dynamically <br> populate a list <br> based on the <br> entered text.         | Enumerator   | N/A         | N/A             |
| Both        | Enables normal <br> editable behavior.                                       | Enumerator   | N/A         | N/A             |
| None        | No operations will <br> be performed in <br> the text box and <br> list box areas. | Enumerator   | N/A         | N/A             |

### Enabling AutoComplete in EditMode for a Combo Box Celltype

The following steps illustrates enabling AutoComplete in EditMode for a combo Box celltype:

1. Declare the Celltype as Combo Box as given in the following code:

#### [C#]

```csharp
this.gridControl1[RowIndex, ColIndex].CellType = GridCellTypeName.ComboBox;
```

#### [VB]

```vb
Me.gridControl1(RowIndex, ColIndex).CellType = GridCellTypeName.ComboBox
```

---

### Footer

© 2013 Syncfusion. All rights reserved. | Page 154

<!-- tags: [Essential Grid, Windows Forms, Syncfusion Winforms, celltype, AutoComplete, EditMode, GridCellTypeName, ComboBox] keywords: [Essential Grid, AutoComplete, EditMode, GridCellTypeName, ComboBox, combo box celltype] -->
```