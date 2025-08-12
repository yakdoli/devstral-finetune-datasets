```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_204.jpeg
document_name: diagram
page_number: 204
page_id: diagram#page_204
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:18:54Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Tool Events

### Overview

Events are triggered when UI tools such as Zoom, Pan, and Select are activated or deactivated in the diagram. The following table lists all the Tool Events.

- **Tool Activated**: Triggered when a UI tool is activated.
- **Tool Deactivated**: Triggered when a UI tool is deactivated.

### Content

The below table shows all the Tool Events.

| DiagramViewerEventSink         | Description                              |
|---------------------------------|------------------------------------------|
| ToolActivated                   | Triggered when UI tool is activated.     |
| ToolDeactivated                 | Triggered when UI tool is deactivated.   |

Data can be retrieved or set using the following members.

#### ToolActivated / Deactivated Event Args Members

| ToolActivated / Deactivated Event Args Members | Description |
|-----------------------------------------------|-------------|
| Tool                                         | Returns the tools object that generated the event. It has the following properties: |
|                                             | - **Name**: Name of the Tool. |

In the below code sample, when a tool is activated or deactivated, the corresponding event will be raised, and the tool name along with the status will be displayed.

#### Code Example (C#)

```csharp
private void Form1_Load(object sender, EventArgs e)
{
    ((DiagramViewerEventSink)diagram1.EventSink).ToolActivated += new ToolEventHandler(DiagramForm_ToolActivated);

    ((DiagramViewerEventSink)diagram1.EventSink).ToolDeactivated += new ToolEventHandler(Form1_ToolDeactivated);

    diagram1.Controller.ActivateTool("ZoomTool");
}

void Form1_ToolDeactivated(ToolEventArgs e)
{
    MessageBox.Show("Deactivated Tool Name: " + e.Tool.Name);
}
```

## API Reference

### Events

- **ToolActivated**: Triggered when a UI tool is activated.
- **ToolDeactivated**: Triggered when a UI tool is deactivated.

## Code Examples

### C#

The example demonstrates how to handle ToolActivated and ToolDeactivated events.

```csharp
private void Form1_Load(object sender, EventArgs e)
{
    ((DiagramViewerEventSink)diagram1.EventSink).ToolActivated += new ToolEventHandler(DiagramForm_ToolActivated);

    ((DiagramViewerEventSink)diagram1.EventSink).ToolDeactivated += new ToolEventHandler(Form1_ToolDeactivated);

    diagram1.Controller.ActivateTool("ZoomTool");
}

void Form1_ToolDeactivated(ToolEventArgs e)
{
    MessageBox.Show("Deactivated Tool Name: " + e.Tool.Name);
}
```

## Page-level Navigation/TOC

- **Tool Events**
  - Overview
  - Content
    - ToolActivated / Deactivated Event Args Members
    - Code Example (C#)
  - API Reference
  - Code Examples

### Tags and Keywords

<!-- tags: [diagram, tool events, UI tools, activation, deactivation, C# example, Windows Forms] keywords: [ToolActivated, ToolDeactivated, DiagramViewerEventSink, ToolEventHandler, MessageBox, ToolEventArgs, ActivateTool] -->
```