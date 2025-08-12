```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_598.jpeg
document_name: tools
page_number: 598
page_id: tools#page_598
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:23:04Z
fidelity: lossless
--> 

## Drop-Down Close on Click Event

This section focuses on the behavior of drop-down controls in Windows Forms, particularly how they respond to user interactions such as losing focus or closing via clicks or the escape key. The accompanying table provides insights into how different drop-down styles and text properties interact under these conditions.

### Table: Drop-Down Control Behavior

| Feature               | No | Yes:2 | Yes:3 | No |
|-----------------------|----|-------|-------|----|
| Drop-Down Close by Escape Key | No | No | No | No |
| Drop-Down Close by Click | Yes:1 | Yes:2 | Yes:3 | No |
| Losing Focus | Yes:2 (in DropDownStyle.DropDownList mode only) | No | No | Yes:1 |
| Changing Text Property in Code | Yes:1 | No | No | No |

---

### Detailed Handling of Drop-Down Close on Click Event

The following section explains how to associate a `CheckedListBox` with the `DropDownCloseOnClick` event. This process ensures that checked items are displayed correctly after the dropdown closes.

#### Overview

- **Objective**: Associate a `CheckedListBox` to handle events when the dropdown is closed via a click.
- **Outcome**: After the dropdown closes, the checked items are displayed in the dropdown text area.

---

#### Steps to Associate a CheckedListBox and Handle the DropDownCloseOnClick Event

1. **Create a CheckedListBox and Populate It**

   Begin by creating a `CheckedListBox` and populating it with items. This step is foundational for handling dropdown events.

---

## Summary

This section outlines the process of associating a `CheckedListBox` with the `DropDownCloseOnClick` event in Windows Forms. It provides clear instructions for handling the event, ensuring that checked items are displayed correctly upon the dropdown closing.

---

### References

- For further details on `CheckedListBox` and dropdown controls in Windows Forms, refer to the official Microsoft documentation or specific Syncfusion Winforms guidelines.

---

### Notes

- Ensure that the `DropDownCloseOnClick` event is appropriately handled to maintain user interface consistency and functionality.

---

<!-- tags: [windowsforms, dropdown, checkedlistbox, eventhandling, syncfusion] keywords: [dropdowncloseonclick, checkedlistbox, userinterface, event, interactiveness] -->
```