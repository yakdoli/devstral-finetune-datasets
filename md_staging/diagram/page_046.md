```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_046.jpeg
document_name: diagram
page_number: 046
page_id: diagram#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:11:24Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- Demonstrates how to integrate the `OverviewControl` in a Windows Forms application using the Syncfusion Diagram control.
- Explains steps to create an `OverviewControl` instance and associate it with a diagram.
- Describes how to add the `OverviewControl` to the form with proper docking settings.

## Content

### Using Syncfusion Diagram in C#

```csharp
//Imports the Diagram control's namespace
using Syncfusion.Windows.Forms.Diagram.Controls;

//Creates an OverviewControl instance
OverviewControl overviewControl = new OverviewControl();
overviewControl.Dock = DockStyle.Left;

//Set the diagram reference to overviewControl
overviewControl.Diagram = diagram1;

//Add overviewControl to the form
this.Controls.Add(overviewControl);
```

### Using Syncfusion Diagram in VB

```vb
'Imports the Diagram control's namespace
Imports Syncfusion.Windows.Forms.Diagram.Controls

'Creates an OverviewControl instance
Dim overviewControl As New OverviewControl()
overviewControl.Dock = DockStyle.Left

'Set the diagram reference to overviewControl
overviewControl.Diagram = Diagram1

'Add overviewControl to the form
Me.Controls.Add(overviewControl)
```

### Explanation of Key Steps

- **Import Namespace**: Import the necessary namespace to use the Diagram control features.
- **Create Instance**: Instantiate the `OverviewControl` and configure its properties, such as docking.
- **Set Diagram Reference**: Associate the `OverviewControl` with the main diagram (`diagram1` in C#, `Diagram1` in VB).
- **Add to Form**: Add the `OverviewControl` to the form's controls list to display it.

## API Reference

### Namespace: Syncfusion.Windows.Forms.Diagram.Controls

#### OverviewControl
- **Properties**
  - `Dock`: Sets the docking style of the control (e.g., `DockStyle.Left`).
  - `Diagram`: The diagram to which the `OverviewControl` is associated. This property must be set to properly display the overview.

## Code Examples

The provided code examples demonstrate the integration of the `OverviewControl` with a diagram in both C# and VB respectively. By setting the `Diagram` property and adding the control to the form, the overview of the diagram will be displayed as per the docking configuration.

## See Also

- [Syncfusion Diagram Documentation](https://www.syncfusion.com/documentation/windowsforms/diagram)
- Additional resources on `OverviewControl` customization and configuration.

<!-- tags: [Syncfusion, WindowsForms, Diagram, OverviewControl, integrate, namespace, instance, diagram, add, form] keywords: [OverviewControl, Diagram, Windows Forms, docking, Syncfusion, diagram1, Diagram1] -->
```