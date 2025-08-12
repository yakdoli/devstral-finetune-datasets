```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_202.jpeg
document_name: tools
page_number: 202
page_id: tools#page_202
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:30:31Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the use of Nested Docking Layouts using UserControls.
- Explains the concept of Linked Managers for transferring docking windows between forms or user controls.
- Provides sample installation path to a demonstration of Nested Docking Layouts.

## Content

### Nested Docking Layouts

You can create Nested Docking Layouts using UserControls. A sample demonstrating this is available in the below sample installation path.

```
..\My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Tools.Windows\Samples\2.0.Docking Package\NestedDockingLayouts
```

#### Linked Managers
The Linked Manager concept allows the transfer of a docking window from one form to another form or user control. This is done with a single method call.

Method `AddToTargetManagersList` enables you to add the DockingManager to the Target DockingManagers list, thereby transferring the docking window to the selected target form.

Method `RemoveFromTargetManagersList` removes the DockingManager from the TargetManagers List.

#### Method Descriptions

| Method                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| AddToTargetManagersList    | Adds the DockingManager to the Target DockingManagers list, transferring the docking window to the selected form. |
| RemoveFromTargetManagersList| Removes the DockingManager from the TargetManagers List.                  |

## API Reference
- `AddToTargetManagersList` method adds the DockingManager to the Target DockingManagers list.
- `RemoveFromTargetManagersList` method removes the DockingManager from the TargetManagers List.

## Cross References
- For more information on Docking Layouts and their usage, refer to the related documentation sections or samples.

<!-- tags: [essential tools, windows forms, nested docking, user controls, linked managers, docking windows, forms, user controls, target managers] keywords: [nested docking layouts, usercontrols, linked manager, addtotargetmanagerslist, removetargetmanagerslist, dock manager] -->
```