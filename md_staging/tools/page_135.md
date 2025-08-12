```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_135.jpeg
document_name: tools
page_number: 135
page_id: tools#page_135
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:45:39Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the concept of tabbed docking in Windows Forms.
- Explains how to align tabs to the "Right" position.
- Introduces methods related to tabbed docking.

## Content

### Figure: Tabs Aligned to "Right"

![](image.png)

**Figure 53: Tabs aligned to "Right"**

### Methods related to Tabbed Docking

| DockingManager Property                  | Description                                                                                          |
|------------------------------------------|------------------------------------------------------------------------------------------------------|
| `IsSameTabbedGroup`                     | Determines whether the second control is under the same group of the first control. <br> `Ctrl1` - Indicates the first control. <br> `Ctrl2` - Indicates the second control. |
| `GetTabPosition`                        | Returns the tab position of the specified control among a tab group. An integer value will be returned indicating the tab position. The parameter is, <br> `Ctrl` - Indicates the docking window. |
| `GetTabbedSiblings`                     | Returns all the siblings of the specified control in a tabbed group or it returns the array of controls which are tabbed with the given control. The parameters are, <br> `Ctrl` - Instance of control whose tabbed siblings are to be returned. |
| `IsTabbed`                              | Returns whether the specified control is tabbed or not. The parameter is, |

## Notes
- The document provides a visual representation of tabbed docking with tabs aligned to the "Right."
- The methods listed under "DockingManager Property" are essential for managing tabbed docking functionalities.

<!-- tags: [tabbed docking, windows forms] keywords: [tabbed docking, alignment, right, DockingManager, control alignment, Crtl1, Ctrl2] -->
```