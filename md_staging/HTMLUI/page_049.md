```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_049.jpeg
document_name: HTMLUI
page_number: 049
page_id: HTMLUI#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:05:30Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview

- This page discusses events in the HTMLUI control, focusing on the `LoadFinished` and `LoadError` events.
- The code examples provided demonstrate handling these events in both C# and VB.NET.

## Content

### [C#]

```csharp
// Event that is to raised after the HTML document have been rendered in the control.
this.htmluiControl.LoadFinished += new
System.EventHandler(this.htmluiControl_LoadFinished);

private void htmluiControl_LoadFinished(object sender, System.EventArgs e)
{
    Console.WriteLine("Load successfully completed");
}
```

### [VB.NET]

```vbnet
' Event that is to raised after the HTML document have been rendered in the control.
Me.HtmluiControl1.LoadFinished += New
System.EventHandler(Me.htmluiControl_LoadFinished)

Private Sub htmluiControl_LoadFinished(ByVal sender As Object, ByVal e As
System.EventArgs)
    Console.WriteLine("Load successfully completed")
End Sub
```

### LoadError Event

**This event is raised when an error occurs during loading or rendering an HTML document from the specified resource. The LoadErrorEventArgs contains the following property that defines the data related to the action of this event.**

#### Document: Specifies the document whose rendering triggers the execution of the LoadError event

### [C#]

```csharp
// Event that is to be raised when an error occurs during HTML document is being
// rendered in the HTMLUI control.
this.htmluiControl.LoadError += new
Syncfusion.Windows.Forms.HTMLUI.LoadErrorEventHandler(this.htmluiControl_LoadError);

private void htmluiControl_LoadError(object sender,
Syncfusion.Windows.Forms.HTMLUI.LoadErrorEventArgs e)
{
    Console.WriteLine("Error loading due to" + e.ToString());
}
```

### [VB.NET]

```vbnet
' Event that is to be raised when an error occurs during HTML document is being
' rendered in the HTMLUI control.
```

## Page-level Navigation/TOC
- **LoadFinished Event** (Section explained)
- **LoadError Event** (Section explained with details and code examples)

## Cross References
- Refer to other sections in the documentation related to HTMLUI control and its properties/methods.

## RAG Annotations
<!-- tags: [Syncfusion, HTMLUI, WindowsForms, LoadFinished, LoadError, Events] keywords: [htmluiControl, LoadFinished, LoadError, EventHandler, LoadErrorEventArgs, error handling, document rendering] -->
```