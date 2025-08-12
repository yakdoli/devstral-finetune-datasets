```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_147.jpeg
document_name: edit
page_number: 147
page_id: edit#page_147
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:02:57Z
fidelity: lossless
-->

## Overview

- Describes properties for handling horizontal and vertical scrollers in a Windows Forms environment.
- Explains how to set or retrieve values for visibility of scrollers.
- Provides examples in both C# and VB.NET to demonstrate configuring scrollers.

## Content

### Properties and Functionality

| Property                    | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| ShowHorizontalScroller      | Gets / sets value indicating whether the horizontal scroller can be shown. |
| AlwaysShowScrollers         | Gets / sets value indicating whether scrollers should be always visible.   |

### Code Examples

#### C#

```csharp
// Display the Horizontal Scroller.
this.editControl1.ShowHorizontalScroller = true;

// Display the Vertical Scroller.
this.editControl1.ShowVerticalScroller = true;

this.editControl1.AlwaysShowScrollers = true;
```

#### VB.NET

```vb
' Display the Horizontal Scroller.
Me.editControl1.ShowHorizontalScroller = True

' Display the Vertical Scroller.
Me.editControl1.ShowVerticalScroller = True

Me.editControl1.AlwaysShowScrollers = True
```

### Scroller Events

The Edit Control supports scroller events that are raised when the scroll arrows are clicked. These scroller events are used to synchronize the scrolling of multiple Edit Controls.

## Page-level Navigation/TOC (if applicable)

- No explicit Table of Contents shown in the image.

## Cross References

- Refer to other sections or pages related to Windows Forms and scrollers for additional information.

<!-- tags: [WinForms, scroller, Edit Control, Windows Forms, Syncfusion] keywords: [ShowHorizontalScroller, AlwaysShowScrollers, scroller events, synchronization, scroll arrows] -->
```