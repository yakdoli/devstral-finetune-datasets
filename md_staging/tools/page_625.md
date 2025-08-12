```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_625.jpeg
document_name: tools
page_number: 625
page_id: tools#page_625
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:23:54Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This page describes the usage of the `ShowPopup` function to display popups in Windows Forms applications.
- Highlights features of the `PopupControlContainer`, including its ability to align popups beside controls or show them at a specific point.
- Discusses integration with Syncfusion's XP Menus and CommandBars frameworks.

## Content

In code, call `ShowPopup` to show the popup anywhere in an application. It also allows you to align a popup beside a control (like in combo boxes) or popup at any given point (like in context menus).

![PopupControlContainer during Run Time](image.png)
*Figure 384: PopupControlContainer during Run Time*

The `PopupControlContainer` also exposes its top-level parent host (a form-derived class) that lets you configure the parent form (to make the parent's borders resizable, for example).

The Syncfusion XP Menus framework lets users associate a `PopupControlContainer` with a menu item and show it from within a menu or toolbar. The Syncfusion CommandBars also let you associate a `PopupControlContainer` with it to be shown when the user clicks on the command bar drop-down button.

### 3.5.6.1.1 Features

`PopupControlContainer` is used to create custom control-rich popups and show them besides a popup-parent, such as a context menu. It has the following features:

- **Control Populations:** This panel-derived control allows users to populate it with various user interface child controls to popup in the desired position.
- **Parent Control Integration:** Allows the user to populate the popup with the desired parent control.
- **Design-Time Configuration:** It can be configured with ease during design time. The popup can be shown anywhere on the screen like a context menu.

## See Also

- [Concepts and Features](#concepts-and-features)

## Cross References

- See also: `Concepts and Features` for additional information.

<!-- tags: [Syncfusion, Windows Forms, PopupControlContainer, XP Menus, CommandBars, control-rich popups, design-time configuration] keywords: [ShowPopup, alignment, parent host, customizable, XP Menus framework, CommandBars, control-rich, design time] -->
```