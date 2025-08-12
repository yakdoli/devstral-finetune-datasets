```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_056.jpeg
document_name: tools
page_number: 056
page_id: tools#page_056
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:18:10Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The CommandBarController component serves as a form scope controller for the CommandBar and ControlBar, providing essential design-time support and APIs for working with CommandBars and ControlBars.
- A CommandBar is similar to the Win32 / MFC ControlBars and is purely a container control responsible for its layout state.
- A ControlBar enables developers to add dockable/floatable controls to a form's toolbar layout, with examples like task pane windows in Microsoft Office 2003. Refer to the 'Detached ControlBars' topic for more details.
- ReBar controls act as containers with one or more bands, each holding a combination of controls such as gripper bars, bitmaps, text labels, etc. They are also known as CoolBars and are not included in the .NET framework but are available in VB 6.0 and MFC frameworks.

## Content

### 3.3.1 Features

This section lists the features available in the CommandBar control.

#### Features

##### CommandBar States

The CommandBar can be:

- **Floated** by setting the `DisableFloating` property to 'False'.
- **Docked** to the form by setting the `DisableDocking` property to 'False'.
- Docked to the Bottom, Left, Right, and Top of the form using the `AllowedDockBorders` property of the CommandBar. The `EnableDockBorders` property of the CommandBarController must be set to 'True' for this to take effect.

##### Button Settings

The CommandBar is usually displayed with close and dropdown buttons, which can be enabled or disabled as needed.

##### Interactive Features

The interactive features of the CommandBar allow for various user interactions.

## API Reference (if applicable)
- [No specific API reference content provided in this section.]

## Code Examples (multi-language supported)
- [No specific code examples provided in this section.]

## Cross References
- Refer to the 'Detached ControlBars' topic under the Menus Package for more detailed explanations of ControlBars.
- For implementing XP style menus and toolbars, refer to the Essential Tools Menus Package.

<!-- tags: [syncfusion, winforms, commandbar, controlbar, rebars, xpstylemenus, toolbars, alloweddockborders, enabledockborders, disablefloating, disabledocking, buttonsettings, interactivefeatures] keywords: [commandbarcontroller, containercontrol, dockablecontrols, taskpane, msoffice2003, coolbar, .netframework, vb6.0, mfcframework, floating, docking, buttonsettings, interactivefeatures] -->
```