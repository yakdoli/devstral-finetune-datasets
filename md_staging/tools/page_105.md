```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_105.jpeg
document_name: tools
page_number: 105
page_id: tools#page_105
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:24:04Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Provides serialization support for CommandBars.
- Describes the events and their behaviors when interacting with CommandBars.

## Content

### Serialization Support for CommandBars

#### Figure 39: Serialization support for CommandBars

The image illustrates the Serialization form for CommandBars, which includes:

- **ControlBar1**: A dropdown list and an X button for deletion or clearing.
- **Multiple CommandBars (CommandBar1, CommandBar2, CommandBar3)**: Indicating the ability to manage multiple command bars.
- **Persistence Type Options**:
  - XML
  - Binary Format
  - Isolated Storage
  - Binary Fmt Format
  - Windows Registry
  - XML Fmt Format

### 3.3.3.10 CommandBar Events

The list of events and a detailed explanation about each of them is given in the following sections.

#### CommandBar Events

| CommandBar Event          | Description                                                                                                                                                                      |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CommandBarDropDownClicked | This event occurs when the dropdown button on a CommandBar is clicked.                                                                                                         |
| CommandBarStateChanging   | This event occurs when a CommandBar's dock / float state is about to change.                                                                                                   |
| CommandBarStateChanged    | This event occurs after a CommandBar's dock / float state changes.                                                                                                              |
| CommandBarUserClosed      | This event occurs when a floating CommandBar is hidden by the user.                                                                                                             |

### Page-Level Navigation/TOC (if applicable)

#### See also:
- Serialization in Windows Forms
- Managing CommandBars in Windows Forms
- Events in Syncfusion WinForms

### Cross References

#### References:
- "Syncfusion.Windows.Forms.Tools.CommandBar"
- "Serialization in Syncfusion"
- "Managing Dock / Float States"

```