```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_144.jpeg
document_name: edit
page_number: 144
page_id: edit#page_144
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:02:20Z
fidelity: lossless
-->

## Overview

- Default key bindings for dialogs can be customized as explained in **Keystroke - Action Combinations Binding**.
- The **History Properties** section details how to manage search and replace histories in dialogs using properties like `FindHistory`, `ReplaceHistory`, and `ReplaceSearchHistory`.
- Documentation covers methods associated with the `FindHistory` property, including `Insert`, `Remove`, `Sort`, and `Clear`.

## Content

### History Properties

The `FindHistory` property is used to add or remove items from the find history in the Find dialog box. The `ReplaceHistory` property is used to add or remove items from the replace history in the Replace dialog box. Similarly, the `ReplaceSearchHistory` property is used to add or remove items from the find history in the Replace dialog box.

#### Edit Control Properties

| Edit Control Property | Description                               |
|-----------------------|-------------------------------------------|
| FindHistory          | Gets history of Find dialog.              |
| ReplaceHistory       | Gets history of Replace dialog.           |
| ReplaceSearchHistory | Gets search history of Replace dialog.   |

#### Methods Associated with FindHistory Property

The methods associated with the `FindHistory` property are used to perform the following operations.

| FindHistory Method | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| Insert             | Inserts an element into the System.Collections.ArrayList at the specified index. |
| Remove             | Removes an element or the first occurrence from the System.Collections.ArrayList of the specified index. |
| Sort               | Sorts all the elements in the System.Collections.ArrayList.                 |
| Clear              | Clears all the items in the FindHistory.                            |

#### Code Examples

- **C#**
  ```csharp
  this.editControl1.FindHistory.Insert(0, (object)ATH.addedItem);
  this.editControl1.FindHistory.Remove(0);
  this.editControl1.FindHistory.Sort();
  this.editControl1.FindHistory.Clear();
  ```

- **VB.NET**
  ```vb
  ' VB.NET code to be added here
  ```

<!-- tags: [syncfusion, winforms, edit control, findhistory, replacehistory, replacesearchhistory, history properties, methods] keywords: [find dialog, replace dialog, search history, default key bindings, keystroke action combinations, insert, remove, sort, clear] -->
```