```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_799.jpeg
document_name: grid
page_number: 799
page_id: grid#page_799
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:41:11Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Overview of the ForeignKey DropDown feature in Essential Grid.
- Description of the Edit Button (button with Pencil Icon) present in the ForeignKey DropDown.
- Instructions on how to edit the list by clicking the Edit Button.

## Content

### ForeignKey DropDown Edit Button

Foreign Key DropDown showing Edit Button (button with Pencil Icon) clicking which allows you to edit the list.

#### Figure 319: Edit button in the ForeignKey DropDown

![](images/placeholder.png)

**Explanation:**
- The image depicts a GridView control showing a ForeignKey DropDown list.
- The Edit Button (marked with a Pencil Icon) is visible in the ForeignKey DropDown.

#### State after clicking the Edit Button

**Below image shows the state after clicking the Edit button.**

#### Figure 320: Editing Records by clicking the Edit Button in the ForeignKey DropDown

![](images/placeholder.png)

**Explanation:**
- The image illustrates the state after the Edit Button is clicked.
- The editable record within the ForeignKey DropDown is highlighted for editing.

## API Reference

This section describes the key API elements involved in the ForeignKey DropDown and the Edit Button functionality.

### Methods

#### `EditForeignKeyDropdown()`

**Description:**
- Initiates the editing process for the selected ForeignKey DropDown record.

**Parameters:**
- None

**Returns:**
- Status of the editing operation.

#### `SelectRecord()`

**Description:**
- Finalizes the edited record and updates the GridView.

**Parameters:**
- None

**Returns:**
- Status of the record selection operation.

#### `CloseEditor()`

**Description:**
- Closes the editing UI without saving changes.

**Parameters:**
- None

**Returns:**
- Status of the editor closure.

## Code Examples

### Example: Using the Edit Button in ForeignKey Dropdown

```csharp
// Enable the Edit Button for the ForeignKey DropDown in the GridView
gridView1.ForeignKeyDropDownSettings.EditButtonVisible = true;

// Handle the Edit Button click event to initiate editing
gridView1.ForeignKeyDropDownSettings.EditButtonAction += (sender, args) =>
{
    // Perform necessary actions to edit the list or record
    // Example:
    var dropdownRecord = (DropDownRow)args.Row;
    dropdownRecord.BeginEdit();
};
```

## Cross References

- Refer to the main documentation for more details on GridView and ForeignKey DropDown functionality.
- Related topics: GridView customization, ForeignKey configuration, DataBinding.

<!-- tags: [syncfusion, winforms, grid, essential-grid, foreign-key, dropdown, edit-button, version:11.4.0.26] keywords: [grid, dropdown, edit, foreignkey, winforms, syncfusion] -->
```