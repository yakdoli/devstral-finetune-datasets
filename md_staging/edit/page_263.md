```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_263.jpeg
document_name: edit
page_number: 263
page_id: edit#page_263
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:29Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Describes the properties and events for collapse functionality in Windows Forms.
- Includes code examples for handling the "OutliningTooltipPopup" event in both C# and VB.NET.
- Discusses print events such as `PrintHeader` and `PrintFooter`.

## Content

### Table: Collapsible Members

| Member         | Description                       |
|----------------|------------------------------------|
| CollapsedText  | Gets / sets collapsed text.       |
| CollapseName   | Gets / sets collapse name.       |
| Collapser      | Gets / sets collapser.           |

#### C# Code Example

```csharp
private void editControl_OutliningTooltipPopup(object sender, Syncfusion.Windows.Forms.Edit.CollapseEventArgs e)
{
    Console.WriteLine(" OutliningTooltipPopup event is raised ");
}
```

#### VB.NET Code Example

```vb
Private Sub editControl_OutliningTooltipPopup(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.CollapseEventArgs)
    Console.WriteLine(" OutliningTooltipPopup event is raised ")
End Sub
```

### 4.14.16 Print Events

It has the following events:

#### 4.14.16.1 PrintHeader Event

This event is discussed in the Printing topic.

#### 4.14.16.2 PrintFooter Event

This event is discussed in the Printing topic.

## API Reference
- Discusses the properties and events related to collapse functionality and print events.

## Code Examples
- Provides examples in C# and VB.NET for handling the "OutliningTooltipPopup" event.

## Page-level Navigation/TOC
- The document is organized into sections, subsections, and code examples for easy navigation.

## Cross References
- The PrintHeader and PrintFooter events are discussed in the Printing topic, which can be referenced separately.

### RAG Annotations
<!-- tags: Windows Forms, Events, Printing, C#, VB.NET, Collapse, Tooltips, Outlining, Syncfusion, Winforms keywords: PrintHeader, PrintFooter, OutliningTooltipPopup, Collapse, Collapser, CollapsedText, CollapseName, Print Events, C#, VB.NET, Event Handling -->
```