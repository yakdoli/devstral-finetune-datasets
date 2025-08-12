```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_597.jpeg
document_name: tools
page_number: 597
page_id: tools#page_597
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:22:08Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### ListBox

The following table describes two collection types used in the `ListBox` control:

| ListBox.SelectedObjectCollection | ListBoxSelectedIndexCollection |
| --- | --- |
| Contains a collection of the selected items which is a subset of the items contained in the ListBox control. | Contains a collection of the selected indexes, which is a subset of the indexes of the ListBox.ObjectCollection. These indexes specify items that are selected. |

### Implementation Guidelines

You should always implement an `Items` property and optionally implement an `IndexFromPoint` method and a `TopIndex` property. Implementing `IndexFromPoint` and `TopIndex` will enable QuickSelection capability for the combo box, where the user can click on the drop-down button and start selecting items in the list, all this without releasing the mouse. You can find more information regarding these requirements in the class reference.

### Event Handling

#### Selection Events

The `ComboBoxBase` fires different events for the different user interaction scenarios. The occurrence and order of the events are tabulated below:

| Scenarios                     | SelectionChangeCommitted | SelectedValueChanged | SelectedIndexChanged | Validating/Validated |
|-------------------------------|--------------------------|-----------------------|-----------------------|----------------------|
| Text Area Change Selection by Keys | Yes:1                  | Yes:2                 | Yes:3                 | No                   |
| Text Area On AutoComplete      | No                       | No                    | No                    | No                   |
| Drop-Down List Change Selection by Keys | No                     | Yes:1                 | Yes:2                 | No                   |
| Drop-Down List Change Selection by Mouse Move | No                   | No                    | No                    | No                   |
| Drop-Down Close by Enter Key  | Yes:1                  | No                    | No                    | No                   |

---

## RAG Annotations

<!-- tags: [syncfusion, winforms, listbox, comboboxbase, selectionevents, indices, validation, autosuggest, drop-down, selectionchange] keywords: [ListBox, SelectedObjectCollection, ListBoxSelectedIndexCollection, QuickSelection, SelectionEvents, ComboBoxBase, IndexFromPoint, TopIndex, SelectionChangeCommitted, SelectedValueChanged, SelectedIndexChanged, Validating, Validated, AutoComplete, AutoSuggest] -->
```