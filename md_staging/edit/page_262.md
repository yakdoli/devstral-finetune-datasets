```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_262.jpeg
document_name: edit
page_number: 262
page_id: edit#page_262
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:43Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview

- Discussion of the OutliningTooltipBeforePopup Event.
- Explanation of the OutliningTooltipClose Event and its handling.
- Description of the OutliningTooltipPopup Event and its parameters.

## Content

### 4.14.15.5 OutliningTooltipBeforePopup Event

This event is discussed in the **Outlining ToolTip** topic.

### 4.14.15.6 OutliningTooltipClose Event

#### Overview

This event is raised when the outlining tooltip is closed.

#### Event Handler Arguments

The event handler receives an argument of type **CollapseEventArgs**. The following **CollapseEventArgs** members provide information specific to this event.

| Member         | Description                |
|----------------|-----------------------------|
| CollapsedText  | Gets / sets collapsed text. |
| CollapseName   | Gets / sets collapse name.  |
| Collapser      | Gets / sets collapser.     |

#### Implementation

##### C#

```csharp
private void editControl1_OutliningTooltipClose(object sender,
    Syncfusion.Windows.Forms.Edit.CollapseEventArgs e)
{
    Console.WriteLine(" OutliningTooltipClose event is raised ");
}
```

##### VB.NET

```vb
Private Sub editControl1_OutliningTooltipClose(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.CollapseEventArgs)
    Console.WriteLine(" OutliningTooltipClose event is raised ")
End Sub
```

### 4.14.15.7 OutliningTooltipPopup Event

#### Overview

This event is raised when the outlining tooltip is shown.

#### Event Handler Arguments

The event handler receives an argument of type **CollapseEventArgs**. The following **CollapseEventArgs** members provide information specific to this event.

## API Reference

### CollapseEventArgs Members

| Member         | Description                |
|----------------|-----------------------------|
| CollapsedText  | Gets / sets collapsed text. |
| CollapseName   | Gets / sets collapse name.  |
| Collapser      | Gets / sets collapser.     |

## Code Examples

Refer to the C# and VB.NET code examples above for handling the **OutliningTooltipClose** event.

## Cross References

See also:
- **Outlining ToolTip**
- Event handling for outlining tooltips

<!-- tags: [syncfusion, windows forms, edit, outliningtooltipbeforepopup event, outliningtooltipclose event, outliningtooltippopup event, collapseeventargs, event handling, tooltip, outlining] keywords: [outlining tooltip, event handler, collapse eventargs, tooltip close, tooltip popup, windows forms, syncfusion edit control] -->
```