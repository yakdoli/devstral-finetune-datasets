```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_051.jpeg
document_name: QTP
page_number: 051
page_id: QTP#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:28Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview

- Describes methods to interact and manipulate tab controls in WinForms applications.
- Lists essential tools and controls supported by Syncfusion WinForms.
- Provides a reference for setting and retrieving properties of tab-related controls.

## Content

### 4.2 Essential Tools

The following controls are supported by Essential Tools.

- ButtonAdv
- CalculatorControl
- CheckBoxAdv
- ColorPickerUIAdv
- ComboBoxAutoComplete
- ComboDropDown
- CommandBar
- DataListView
- DateTimePickerAdv
- DockingManager
- GroupBar
- GroupView
- MultiColumnComboBox
- PopUpMenu
- ProgressBarAdv
- RadioButtonAdv
- RibbonControlAdv
- ScrollerFrame
- TabbedMDI
- TabControlAdv
- XPTaskBar
- TextBoxExt
- ThemedCheckedButton
- TreeViewAdv
- XPMenus
- XPToolBar
- SplitContainerAdv
- TabSplitterContainer
- TrackBarEx
- RangeSlider

### Table of Tab Control Methods

| Method                      | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| GetTabName(int index)      | The label in the tab page can be known by passing the index.                 |
| Select(string tab)         | The name of the selected tab.                                               |
| SetSplitterPosition(string tab, int vSplit, int hSplit) | The splitter position in the tab bar page. |

## Code Examples

```csharp
// Example: Selecting a tab by name
tabControl1.Select("Settings");

// Example: Getting the name of a tab using index
string tabName = tabControl1.GetTabName(0);

// Example: Setting the splitter position of a tab
tabControl1.SetSplitterPosition("Design", 250, 150);
```

## Cross References

- Refer to the **User Guide** for detailed information on setting up and configuring tabs and controls in WinForms applications.
- For more details on the SplitContainerAdv and TabSplitterContainer controls, see the respective sections in the **Controls Documentation**.

<!-- tags: [Syncfusion, Winforms, tab control, essential tools] keywords: [tabControl, GetTabName, Select, SetSplitterPosition, ButtonAdv, CheckBoxAdv, ComboDropDown, TabbedMDI, TrackBarEx, RangeSlider] -->
``` 
