```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_212.jpeg
document_name: tools
page_number: 212
page_id: tools#page_212
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:35:40Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Focuses on the AutoHideTabContextMenu event handling in Syncfusion Winforms.
- Describes the context menu event related to autohidden tab controls.
- Explains handling the AutoHideTabContextMenuEventArgs object with properties like ContextMenu and DockBorder.
- Includes C# and VB.NET code examples for event implementation.

## Content

### 3.4.3.8.3 Context Menu

This section covers the following events:

#### 3.4.3.8.3.1 AutoHideTabContextMenu Event

This event occurs when the right mouse button is clicked over a autohidden tab control.

#### Event Data

The event handler receives an argument of type `AutoHideTabContextMenuEventArgs` containing data related to this event. The following `AutoHideTabContextMenuEventArgs` properties provide information specific to this event.

| Members           | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `ContextMenu`     | Gets / sets the context menu to be displayed.                             |
| `DockBorder`      | This returns the side to where the AutoHideTab is aligned.               |

#### Code Examples

- **C#**

```csharp
private void dockingManager1_AutoHideTabContextMenu(object sender, Syncfusion.Windows.Forms.Tools.AutoHideTabContextMenuEventArgs arg)
{
	// You can see the below line in output window during runtime.
	Console.WriteLine("AutoHideTabContextMenu event is raised");
}
```

- **VB.NET**
```vb

```

## Page-level Navigation/TOC (if applicable)
- 3.4.3.8.3 Context Menu
  - 3.4.3.8.3.1 AutoHideTabContextMenu Event
    - Event Data
    - Code Examples

## Cross References
- Refer to documentation on context menus and event handling in Syncfusion Winforms.

## RAG Annotations
<!-- tags: [windows forms, context menu, event handling, autohide tab, syncfusion, visual basic net] keywords: [AutoHideTabContextMenu, AutoHideTabContextMenuEventArgs, context menu, event, right mouse button, tab control, C#, VB.NET] -->
```