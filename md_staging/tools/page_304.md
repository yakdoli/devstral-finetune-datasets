```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_304.jpeg
document_name: tools
page_number: 304
page_id: tools#page_304
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:04:23Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The Columns property can be refreshed using an external data source in the designer.
- Adding images to dropdown items using internal or external sources is possible.
- Detailed information on image settings and AutoCompleteControl is provided.

## Content

### Refreshing Columns Property
Initially, when using an external data source, the Columns property can be refreshed by clicking on the **Refresh Columns** verb visible in the designer.

#### Note: Adding Images to Dropdown Items
Images can be added to dropdown items using either internal or external sources. For more details, refer to **Image Settings**.

#### See Also
- [Source for AutoComplete Control](#)
- [How to match items in all the columns using AutoCompleteControl?](#)

---

### Image Settings

#### Adding Dropdown Items with Images
To add a dropdown item with an image to the AutoComplete popup, use the **AutoComplete.AddHistoryItem** method. An imagelist must be associated with the AutoComplete control for this purpose. The method requires the item text and the image index.

#### AutoComplete Method Description
| AutoComplete Method       | Description                                                                                   |
|---------------------------|-----------------------------------------------------------------------------------------------|
| AddHistoryItem            | Adds an item to the internal history of the AutoComplete control. Parameters are:<br>- newItemText - Text for the dropdown item.<br>- ImageIndexValue - Index of the image for the particular item. |

---

### Code Example

```csharp
[C#]

this.autoCompleteDataColumnInfo1.ColumnHeaderText = "Title";
this.autoCompleteDataColumnInfo1.ImageColumn = false;
this.autoCompleteDataColumnInfo1.MatchingColumn = true;
this.autoCompleteDataColumnInfo1.Visible = true;

this.autoCompleteDataColumnInfo2.ColumnHeaderText = "Size";
this.autoCompleteDataColumnInfo2.ImageColumn = true;
this.autoCompleteDataColumnInfo2.MatchingColumn = false;
this.autoCompleteDataColumnInfo2.Visible = true;

this.autoComplete1.AddHistoryItem("User Guide", 3);
this.autoComplete1.AddHistoryItem("User Item", 2);
```

## API Reference
### Methods
- **AddHistoryItem**
  - **Parameters**
    - newItemText: `string` - Text for the dropdown item.
    - ImageIndexValue: `int` - Index of the image for the particular item.

## Code Examples

#### Example: Adding History Items with Images
```csharp
this.autoComplete1.AddHistoryItem("User Guide", 3);
this.autoComplete1.AddHistoryItem("User Item", 2);
```

### Cross References
- [Image Settings](#)
- [AutoCompleteControl](#)
- [Source for AutoComplete Control](#)
- [How to match items in all the columns using AutoCompleteControl?](#)

<!--
tags: [Syncfusion Winforms, AutoCompleteControl, Image Settings, Columns Property, Data Source, Designer, Refresh Columns, dropdown items, imagelist]
keywords: [AutoComplete, AddHistoryItem, ImageIndexValue, newItemText, Columns, AutoComplete pop-up, imagelist association, Windows Forms, control history, dropdown item text, dropdown item image]
-->
```