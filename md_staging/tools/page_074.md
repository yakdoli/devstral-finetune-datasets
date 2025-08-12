```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_074.jpeg
document_name: tools
page_number: 074
page_id: tools#page_074
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:19:30Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains the properties and methods related to the CommandBar control.
- Demonstrates how to manage the DropDown Button and Close Button in both Float and Dock states.
- Discusses the interactive features available in the CommandBar control.

## Content

### CommandBar Control Details

```vb
Me.commandBar1.HideDropdownButton = True
```

#### Figure 21: "DropDown Button" and "Close Button" of CommandBar in Float State

![Figure 21: "DropDown Button" and "Close Button" of CommandBar in Float State](<image_link_for_Figure_21>)

#### Figure 22: "DropDown Button" of CommandBar in Dock State

![Figure 22: "DropDown Button" of CommandBar in Dock State](<image_link_for_Figure_22>)

The methods associated with the above properties are given below.

### Table 9: Button Settings - Methods

| Methods              | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| GetCloseButtonState  | Gets visual state for the close button of the floating CommandBar.          |
| GetDropdownState     | Gets visual state for the dropdown button of the CommandBar.               |

#### Sample for Demonstration

A sample which demonstrates the DropDown Button settings of the CommandBar control is available in the below sample installation path:

```
.My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Tools.Windows\Samples\2.0\CommandBars Package\CommandBars
```

### 3.3.3.3 Interactive Features

#### Overview
This section discusses the interactive features available in the CommandBar control.

### Chevrons

The term "chevron" is used for a menu that contains the toolbar icons that do not fit in the space available on the toolbar.

## API Reference

- **GetCloseButtonState**: Gets visual state for the close button of the floating CommandBar.
- **GetDropdownState**: Gets visual state for the dropdown button of the CommandBar.

## Code Examples

The VB.NET code snippet provided demonstrates how to hide the dropdown button of the CommandBar control:

```vb
Me.commandBar1.HideDropdownButton = True
```

::: tip
Ensure proper property settings to achieve the desired UI behavior for the CommandBar control.
:::

## RAG Annotations
<!-- tags: [windowsforms, commandbar, control, userinterface, dropdownbutton, closebutton, floatstate, dockstate] keywords: [dropdownbutton, closebutton, visualstate, commandbar, floatstate, dockstate, chevron, toolbar, interactivefeatures] -->
```