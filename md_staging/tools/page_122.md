```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_122.jpeg
document_name: tools
page_number: 122
page_id: tools#page_122
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:36:09Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview

- Extender provider architecture
  - The DockingManager class is the central component of the docking windows framework.
  - DockingManager extends controls via .NET's SetEnableDocking property, simplifying docking window addition to applications with just setting the property on the control.
- Context menu
  - Docked controls can display context menus on the caption bar.
  - Auto-hide tabs also have unique context menus.
- Docking Ability
  - Previously, diamond docking indicators lacked the ability to hide docking arrows, limiting docking to specific sides.
  - Now, DockAbility / OuterDockAbility features allow hiding docking arrows for selective docking options.

### Content

#### Extender provider architecture
The central component of the docking windows framework is the DockingManager class. The DockingManager is implemented as a .NET Extender Provider component that extends the SetEnableDocking property to any control instance on the form or ContainerControl hosting the DockingManager. This makes the addition of docking windows to applications an extremely simple one-step process of just setting the extended property on the control without need for complex initialization.

#### Context menu
The docked controls can display context menu on right clicking the caption bar. An unique context menu is available for auto hide tabs also.

#### Docking Ability
Previously, the diamond docking indicators did not have the ability to hide certain docking arrows, and hence it could be docked to certain sides only and we have to handle events to achieve this.

Now, DockAbility / OuterDockAbility features allow to hide docking arrows so that we can dock a window only to certain sides of a form / usercontrol.

#### See Also
- [Getting Started, Concepts and Features](#getting-started)

### 3.4.2 Getting Started

This section will provide step by step procedure to design a docking window layout through designer and through programmatical approach in a .NET application.

#### 3.4.2.1 Through Designer

The docking window's WYSIWYG designer makes the implementation of a docking windows layout a highly intuitive process. Complex layouts can be designed by dragging-and-dropping the docking manager, without having to write a single line of code.

The following steps outline the sequence of steps involved in setting up a simple docking windows (listbox for ex) layout using the designer.

1. Open the host form within the windows forms designer and add the controls that should be implemented as docking windows.

## Code Examples

### Page-level Navigation/TOC
- [Getting Started](#getting-started)
- [Docking Ability](#docking-ability)
- [Context menu](#context-menu)
- [Extender provider architecture](#extender-provider-architecture)

## Cross References
See Also:
- [Getting Started, Concepts and Features](#getting-started)

### RAG Annotations
<!-- tags: [DockingManager, Extender Provider, DockAbility, OuterDockAbility, WYSIWYG, Designer] keywords: [Docking windows, SetEnableDocking property, auto hide tabs, context menu, WYSIWYG designer, Windows Forms, Syncfusion Winforms] -->
```
