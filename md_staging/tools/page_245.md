```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_245.jpeg
document_name: tools
page_number: 245
page_id: tools#page_245
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:00:29Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This page explains how to manage docking and tab groups for controls in a Windows Forms application using Syncfusion's docking manager.
- Includes code examples to determine the docking state of controls and display relevant status messages.

## Content

The following code snippet demonstrates how to check the docking state of a control and determine whether it is part of a tab group or floating independently. It also identifies the primary control in the tab group if applicable.

### Example Code

```csharp
if (this.dockingManager1.IsFloating(dockedControl))
{
    statusMessage = dockedControl.Name + " is floating and in a tab group.";
    targetControl = baseController.HostControl.Parent.Controls[0].Controls[0];
}
else
{
    statusMessage = dockedControl.Name + " is in a tab group.";
    targetControl = baseController.HostControl.Controls[0];
}

if (targetControl.Name != dockedControl.Name)
    statusMessage += "The tab group primary control is " + targetControl.Name + ".";
else
    statusMessage += "This control is the primary control in the tab group.";

Console.WriteLine(statusMessage);
```

This code is part of a method that checks the docking state of a control and outputs the status message regarding its docking configuration. The method `getControlsRelationToolstripMenuItem_Click` indicates that this logic is triggered by a toolstrip menu item click event. Below is the continuation of the method:

### Further Implementation

```csharp
ArrayList dockedctrls;
int count;
private void getControlsRelationToolstripMenuItem_Click(object sender, EventArgs e)
{
    count = 0;
    IEnumerator ienum = this.dockingManager1.Controls;
    dockedctrls = new ArrayList();
}
```

This segment initializes an `ArrayList` to store docked controls and sets up an enumerator to iterate through the controls managed by the docking manager. The code continues to process the controls and their docking states.

### Purpose

This functionality is useful for developing Windows Forms applications where dynamic docking and tab grouping of controls are required. It enables developers to manage and display information about the docking behavior of controls, enhancing user interaction and application configuration.

## API Reference

### Methods
- `IsFloating(dockedControl)`: Checks if the specified control is floating.
- `HostControl`: Provides access to the host control for a docking controller.
- `Controls`: Provides a collection of controls managed by the docking manager.

### Properties
- `Name`: Gets the name of a control.
- `Parent`: Gets the parent control of a control.

## Code Examples

### Full Example

```csharp
using System;
using System.Collections;
using Syncfusion.Windows.Forms;

public partial class MainForm : Form
{
    private void MainForm_Load(object sender, EventArgs e)
    {
        // Initialize docking manager
        dockingManager1.IsModified = true;
    }

    private void getControlsRelationToolstripMenuItem_Click(object sender, EventArgs e)
    {
        ArrayList dockedctrls = new ArrayList();
        IEnumerator ienum = dockingManager1.Controls;
        string statusMessage = string.Empty;

        while (ienum.MoveNext())
        {
            IDockControl dockedControl = (IDockControl)ienum.Current;
            if (dockingManager1.IsFloating(dockedControl))
            {
                statusMessage = dockedControl.Name + " is floating and in a tab group.";
                IDockController baseController = dockingManager1.GetDockController(dockedControl);
                Control targetControl = baseController.HostControl.Parent.Controls[0].Controls[0];

                if (targetControl.Name != dockedControl.Name)
                    statusMessage += "The tab group primary control is " + targetControl.Name + ".";
                else
                    statusMessage += "This control is the primary control in the tab group.";
            }
            else
            {
                statusMessage = dockedControl.Name + " is in a tab group.";
                IDockController baseController = dockingManager1.GetDockController(dockedControl);
                Control targetControl = baseController.HostControl.Controls[0];

                if (targetControl.Name != dockedControl.Name)
                    statusMessage += "The tab group primary control is " + targetControl.Name + ".";
                else
                    statusMessage += "This control is the primary control in the tab group.";
            }

            Console.WriteLine(statusMessage);
        }
    }
}
```

This example demonstrates how to iterate through all docked controls, determine their docking state, and display relevant status messages using the Syncfusion docking manager.

<!-- tags: [WinForms, controls, docking, tab groups, Syncfusion] keywords: [docking manager, tab group, floating controls, status message, host control, enumeration] -->
```