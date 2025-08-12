```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_030.jpeg
document_name: QTP
page_number: 030
page_id: QTP#page_030
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:00Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- This page demonstrates the integration of the Grid Control in applications and the use of the SwfConfig file to map controls to their respective DLLs.
- Focuses on user interactions with the Grid Control and the corresponding actions logged in the running application.
- Explains how method names from the Syncfusion namespace are recorded and displayed based on user interactions.

## Content

### Grid Control Usage
Figure 17 illustrates the use of the Grid Control in an application.

![Figure 17: Application using Grid Control](assets/figure17.png)

1. Perform required valid user-action in the application.

#### Note: SwfConfig File Mapping
- Whenever the user performs any action involving the Syncfusion control used in the application, the SwfConfig file maps the control to the corresponding DLL.
- The DLL renders the correct method names of the Syncfusion namespace that will be called respective to the user-actions performed.
- These method names are then recorded and displayed in the screen behind the running application, as shown below.

## API Reference
### Method Names Recording
- The Grid Control logs user-action methods from the Syncfusion namespace.
- Recorded method names reflect the actions performed, enabling testing and validation of control behavior.

## Code Examples
```csharp
// Example: Performing a user-action on the Grid Control
grid.PerformAction("SelectRow", rowIndex);

// Example: Recording user-action method names
recordedMethods.Add("SelectRow(rowIndex)");
```

## Page-level Navigation/TOC (if applicable)
- [Grid Control Usage]
- [SwfConfig File Mapping]
- [Method Names Recording]

### Cross References
- See also: [Essential QuickTest Professional Documentation](#essential-quicktest-professional-documentation)
- See also: [Syncfusion Grid Control Reference](#syncfusion-grid-control-reference)

<!-- tags: [syncfusion, winforms, grid control, qtp, swfconfig, method recording, dll mapping] keywords: [grid control, user-action, method names, swfconfig, dll, quicktest professional, essential qtp] -->
```