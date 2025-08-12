```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_226.jpeg
document_name: edit
page_number: 226
page_id: edit#page_226
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:07:53Z
fidelity: lossless
-->

## Overview

- This page discusses the implementation and customization of the Status Bar and its panels in the Syncfusion Windows Forms application.
- It includes code examples for defining namespaces and using various Syncfusion libraries.
- The Status Bar settings are elaborated with explanations of their properties, allowing developers to customize the appearance and visibility of the status bar panels.

## Content

### Status Bar and Status Bar Panels in Edit Control

```csharp
using System.Windows.Forms;
using System.Data;
using System.IO;
using Syncfusion.Windows.Forms.Edit;
using Syncfusion.Windows.Forms.Edit.Dialogs;
using Syncfusion.Windows.Forms.Edit.Implementation;
using Syncfusion.Windows.Forms.Edit.Interfaces;
using Syncfusion.Windows.Forms.Edit.Enums;

namespace StatusBarDemo
{
    // Additional code to be implemented here
}
```

**Figure 73: Status Bar and Status Bar Panels in Edit Control**

In addition to the above information, any custom text can also be displayed in the Status Bar Panels.

### Status Bar Settings

The `StatusBarSettings` property consists of the following sub-properties, which can be used to customize the appearance and visibility of the status bar and its panels.

| StatusBarSettings Property | Description |
|-----------------------------|-------------|
| **TextPanel** | Specifies `StatusBaPanelSettings` object for Text panel. |
| **StatusPanel** | Specifies `StatusBaPanelSettings` object for Status panel. |
| **EncodingPanel** | Specifies `StatusBaPanelSettings` object for Encoding panel. |
| **FileNamePanel** | Specifies `StatusBaPanelSettings` object for FileName panel. |
| **CoordsPanel** | Specifies `StatusBaPanelSettings` object for Coords panel. |
| **InsertPanel** | Specifies `StatusBaPanelSettings` object for Insert panel. |
| **Panels** | Gets the list of status bar panels settings. |
| **StatusBar** | Gets underlying status bar. |
| **GripVisibility** | Gets / sets visibility of status bar sizing grip. The options provided are as follows: |

### Summary

This section provides a detailed guide on setting up and customizing the Status Bar in a Syncfusion Windows Forms application. It includes examples of usage and a comprehensive list of properties that allow for flexible configuration.

<!-- tags: [winforms, status bar, syncfusion, edit control, customization] keywords: [status bar panels, text panel, status panel, encoding panel, file name panel, coordinates panel, insert panel, status bar settings, grip visibility] -->
```