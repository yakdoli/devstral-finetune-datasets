```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_918.jpeg
document_name: grid
page_number: 918
page_id: grid#page_918
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:52:04Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Guide to configuring the SelectionMode property in the grid for multi-item selection scenarios.
- Explains how to use the "MultiExtended" selection mode for selecting multiple items using keyboard shortcuts.

## Content

### SelectionMode - MultiExtended

This selection type allows multiple items selection through Shift, Ctrl, and Arrow keys.

#### Figure 334: Selection Mode set to "MultiSimple"

![Figure: Selection Mode set to "MultiSimple"]()

**SelectionMode - MultiExtended**

This selection type allows multiple items selection through Shift, Ctrl, and Arrow keys.

#### Code Examples

- **C#**
  ```csharp
  this.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.MultiExtended;
  ```

- **VB.NET**
  ```vb
  Me.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.MultiExtended
  ```

## API Reference
- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Class:** GridGroupingControl
  - **Property:** TableOptions.ListBoxSelectionMode
    - **Type:** SelectionMode
    - **Description:** Specifies the selection mode for the list box.
    - **Possible Values:** 
      - Simple
      - MultiSimple
      - MultiExtended
    - **Default:** Simple

## Page-level Navigation/TOC (if applicable)
- SelectionMode - MultiExtended
  - Overview
  - Code Examples
  - API Reference

### Cross References
- Refer to the documentation on other selection modes for additional details.

<!-- tags: [grid, windows-forms, selection-mode, multiextended, syncfusion] keywords: [multi-item selection, shift, ctrl, arrow keys, gridgroupingcontrol, listboxselectionmode, winforms] -->
```