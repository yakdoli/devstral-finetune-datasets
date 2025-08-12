```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_257.jpeg
document_name: diagram
page_number: 257
page_id: diagram#page_257
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:30Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This page explains how to change the selection mode of the `SelectTool` in Syncfusion Diagrams for Windows Forms.
- It covers the properties and methods to modify the selection behavior during runtime.
- Includes examples demonstrating the implementation in C#.

## Content

### 5.4 How to Change the Selection Mode of the SelectTool

The Diagram `SelectTool` provides an enum property called `SelectMode` to change the selection mode. The following are the supported selection modes:

- **Containing** - Specific objects that are fully enclosed by the tracking rectangle will be selected by the tool.

- **Intersecting** - Specific objects that are intersecting the tracking rectangle will be selected by the tool.

**Figure 154: LineColor = "Red"**  

*Figure depicting the use of different selection modes with shapes connected by lines.*

**Containing** is the default selection mode.

The following code snippet illustrates how to change the selection mode at runtime:

```csharp
[C#]

((DiagramViewerEventSink)diagram1.EventSink).ToolActivated += new ToolEventHandler(Diagram_ToolActivated);

private void Diagram_ToolActivated(ToolEventArgs evtArgs)
{
    if (evtArgs.Tool is SelectTool)
    {
        // change the SelectionMode as "Intersecting" which specifies that objects intersecting the tracking rectangle will be selected by the tool.
    }
}
```

## API Reference

### Properties
- **SelectMode**  
  - Type: Enum (Selecting.Objects.Containing, Selecting.Objects.Intersecting)
  - Description: Determines the behavior of the selection tool when choosing objects in the diagram.
  - Default: Containing

### Events
- **ToolActivated**
  - Triggered when a tool is activated in the Diagram.
  - Parameters: `ToolEventArgs` containing the activated tool for handling specific actions.

## Code Examples

### Example: Changing Selection Mode at Runtime

The following example demonstrates how to modify the `SelectMode` property of the `SelectTool` at runtime in response to a tool activation event:

```csharp
using Syncfusion.Windows.Forms.Diagram;
using Syncfusion.Windows.Forms.Diagram.Controls;
using Syncfusion.Windows.Forms;
using System.Windows.Forms;

namespace DiagramDemo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            // Initialize Diagram
            diagram1 = new Diagram();

            // Attach Event Handler
            ((DiagramViewerEventSink)diagram1.EventSink).ToolActivated += new ToolEventHandler(Diagram_ToolActivated);
        }

        private void Diagram_ToolActivated(ToolEventArgs evtArgs)
        {
            if (evtArgs.Tool is SelectTool)
            {
                // Set Selection Mode to Intersecting
                ((SelectTool)evtArgs.Tool).SelectMode = Selecting.Objects.Intersecting;
            }
        }
    }
}
```

## Cross References

See also:
- [5.3 Working with Diagram Tools](#working-with-diagram-tools)

### Copyright Information
- © 2013 Syncfusion. All rights reserved.

<!-- tags: [Syncfusion, Diagram, Windows Forms, SelectTool, SelectionMode, Intersecting, Containing] keywords: [Selection, ToolActivated, Selecting, Objects, C#, Diagram, Windows Forms, Syncfusion, SelectionMode] -->
```