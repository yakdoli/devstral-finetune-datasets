```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_215.jpeg
document_name: tools
page_number: 215
page_id: tools#page_215
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:40:03Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explanation of context menu items and their significance in Windows Forms development.
- Focus on the DockMenuClick event and its behavior when performing docking adjustments.

## Content

### Figure 104: Context Menu Items Added
The image illustrates a Windows Forms interface showing the application of context menu items. It displays a form with a list box and a floating dockable control, where the context menu includes options like "Dockable," "Hide," "Floating," "Auto-Hide," and "Dock to." The user interface showcases a typical Windows Forms scenario with a clear depiction of how context menu items are associated with specific controls.

### See Also
- **Context Menu**

### 3.4.3.8.3.3 DockMenuClick Event

The DockMenuClick event is triggered when the redock context menu item has been clicked. The menu button available for docked controls provides options to change the docking position. Whenever a user attempts to redock a control to a different position, the DockMenuClick event is triggered. The options for redocking include left, top, right, and bottom. The redocked style can be displayed using the following code:

#### Event Data
The DockMenuClickEventHandler receives an argument of type DockMenuClickEventArgs containing data related to the event. The DockMenuClickEventArgs properties provide specific information about the event:

| **Members**       | **Description**                   |
|-------------------|-----------------------------------|
| DockingStyle      | Returns the docking of the window. |

### Copyright Notice
© 2013 Syncfusion. All rights reserved.

## RAG Annotations
<!-- tags: [tools, windows-forms, context-menu, dockmenuclick-event, version-11.4.0.26] keywords: [context menu, DockMenuClick event, redocking, DockingStyle, DockMenuClickEventArgs] -->
```