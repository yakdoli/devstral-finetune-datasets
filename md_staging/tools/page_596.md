```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_596.jpeg
document_name: tools
page_number: 596
page_id: tools#page_596
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:23:06Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The following topics will help you become more familiar in using the ComboBoxBase control.

## Appearance and Behavior Settings

### Overview
- Discusses the Appearance and Behavior Settings of ComboBoxBase.
- Focuses on customizing border drawing features and advanced styling options.
- Highlights properties like Style and FlatStyle.

### Content

#### Appearance and Behavior Settings
This section includes the discussion of Appearance and Behavior Settings of ComboBoxBase.

The ComboBoxBase control provides Style, FlatStyle and other properties to enable advanced border drawing features. Written using native .NET Controls, this control lets you customize everything in the combo box from the text box to the drop-down window. Refer **ComboBoxAdv** user guide, which contains properties included in ComboBoxBase.

You will also notice that some of the properties you can find in the framework combo box (like IntegralHeight, ItemHeight, MaxDropDownItems, datasource and events like SelectedIndexChanged) are missing in the ComboBoxBase. These properties and events are meant to be set / handled in the plugged-in ListControl.

#### Creating ListControl - Derived Controls

When you create custom ListControl - derived controls for use with the ComboBoxBase class, it is essential that you provide certain properties and methods to avail all the capabilities of the ComboBoxBase class.

The ListBox control enables you to display a list of items, it can be selected by clicking. A ListBox control can provide single or multiple selections using the **SelectionMode** property. The ListBox also provides the **MultiColumn** property to enable the display of items in columns instead of a straight vertical list of items. This allows the control to display more visible items and prevents the need for the user to scroll to an item.

In addition to display and selection functionality, the ListBox also provides features that enable you to efficiently add items to the ListBox and to find text within the items of the list.

The **BeginUpdate** and **EndUpdate** methods enable you to add a large number of items to the ListBox without the control being repainted each time an item is added to the list.

The Items, SelectedItem and SelectedIndices properties provide access to the three collections that are used by the ListBox.

#### Collection Class vs. Use Within the ListBox

| Collection Class         | Use Within the List Box                          |
|--------------------------|--------------------------------------------------|
| ListBox.ObjectCollection | Collection of all items contained in the ListBox control. |

### API Reference
- **ComboBoxBase** and its properties like Style and FlatStyle are crucial for customization.
- **ListBox** properties such as SelectionMode and MultiColumn are key to enabling advanced functionalities.

### Code Examples
- Example usage of ComboBoxBase and ListBox to demonstrate the discussed functionalities.

<!-- tags: [winforms, comboboxbase, listbox, selectionmode, multicolun]* -->
```