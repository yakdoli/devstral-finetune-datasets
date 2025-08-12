```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: QTP
page_number: 053
page_id: QTP#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:59Z
fidelity: lossless
-->

## Overview
- Provides details on the methods and descriptions for various UI components in Syncfusion WinForms.
- Covers DropDown(), Select(), SetDockState(), SetFloatState(), and other methods relevant to UI controls.
- Includes examples for CommandBar, DataListView, and DateTimePickerAdv controls.

## Content

### Control Methods
This section outlines the methods and their corresponding usage for different controls in the Syncfusion WinForms framework.

#### DropDown
| Method | Description |
|--------|-------------|
| `DropDown()` | Shows the drop-down list. |

#### ComboDropDown
| Method | Description |
|--------|-------------|
| `DropDown()` | Shows the drop-down list. |
| `Select(object item)` | Selects the item in the list. |

#### CommandBar
| Method | Description |
|--------|-------------|
| `DropDown()` | Shows the drop-down list. |
| `SetDockState(string dockState)` | Changes the dock state. |
| `SetFloatState(int x, int y)` | Sets the CommandBar to float. |

#### DataListView
| Method | Description |
|--------|-------------|
| `Select(string item)` | Selects the specified item. |
| `Return()` | Performs click on the focused item. |

#### DateTimePickerAdv
| Method | Description |
|--------|-------------|
| `void CheckEnabled(object on, string checkState);` | Interface to check the enabled state of the DateTimePickerAdv. |
| `void ChangeValue(object on, string dateTime);` | Interface to change the value of the DateTimePickerAdv. |

---

## API Reference

### DateTimePickerAdv Methods
- **`void CheckEnabled(object on, string checkState);`**
  - **Description:** Interface to check the enabled state of the DateTimePickerAdv.
- **`void ChangeValue(object on, string dateTime);`**
  - **Description:** Interface to change the value of the DateTimePickerAdv.

---

<!-- tags: [syncfusion, winforms, controls, commandbar, dataview, datetimepickeradv, methods] keywords: [dropdown, select, floatstate, dockstate, interface, enabledstate, changevalue] -->
```