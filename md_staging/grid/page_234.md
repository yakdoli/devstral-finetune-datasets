```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_234.jpeg
document_name: grid
page_number: 234
page_id: grid#page_234
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:03:11Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the event behavior for the PaneClosing event in a Windows Forms grid.

## Content

| PaneClosing |
|-------------|
| This event is triggered either when the splitter is moved to the end/beginning or when it cannot be located on the worksheet. |

### Creating a Splitter in a Worksheet

The splitter can be created in a worksheet by using the following code:

#### 1. Using C#

```csharp
this.splitterControl.Controls.Add(this.gridControl1);

// PaneCreated event.
private void splitterControl1_PaneCreated(object sender, Syncfusion.Windows.Forms.SplitterPaneEventArgs e)
{
    Console.WriteLine("Created: " + e.ToString());
}

// PaneClosing event.
private void splitterControl1_PaneClosing(object sender, Syncfusion.Windows.Forms.SplitterPaneEventArgs e)
{
    Console.WriteLine("Closed: " + e.ToString());
}
```

#### 2. Using VB.NET

```vb
Me.splitterControl1.Controls.Add(Me.gridControl1)

' PaneCreated event.
private void splitterControl1_PaneCreated(Object sender, Syncfusion.Windows.Forms.SplitterPaneEventArgs e)
Console.WriteLine("Created: " & e.ToString())

' PaneClosing event.
private void splitterControl1_PaneClosing(Object sender, Syncfusion.Windows.Forms.SplitterPaneEventArgs e)
Console.WriteLine("Closed: " & e.ToString())
```

## Cross References
- For more information on splitter interactions and events, refer to the documentation on Splitter controls in the Syncfusion Windows Forms Grid.

## RAG Annotations
<!-- tags: [splitter, paneclosing, event, windowsforms, grid, essentialgrid] keywords: [splitter, pane, closing, event, panecreated, paneclosing, windows forms] -->
```
