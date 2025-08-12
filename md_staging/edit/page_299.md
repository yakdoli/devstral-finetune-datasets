```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_299.jpeg
document_name: edit
page_number: 299
page_id: edit#page_299
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:11:47Z
fidelity: lossless
-->

## Overview
- Demonstrates how to suspend and resume painting of the `EditControl`.
- Provides examples in both C# and VB.NET.

## Content

### 5.18 How To Suspend And Resume Painting Of the Edit Control

The following code snippet illustrates how to suspend and resume painting of the `EditControl`.

```csharp
this.editControl1.SuspendPainting();
this.editControl1.ResumePainting();
```

```vb
Me.editControl1.SuspendPainting()
Me.editControl1.ResumePainting()
```

## API Reference
- **Method**: `SuspendPainting()`
  - Stops the `EditControl` from repainting during property changes.
- **Method**: `ResumePainting()`
  - Resumes the `EditControl` repainting, updating the display.

## Code Examples

#### C#
```csharp
this.editControl1.SuspendPainting();
// Perform multiple property changes.
this.editControl1.ResumePainting();
```

#### VB.NET
```vb
Me.editControl1.SuspendPainting()
' Perform multiple property changes.
Me.editControl1.ResumePainting()
```

<!-- tags: [editcontrol, suspendpainting, repaint, winforms, syncfusion] keywords: [suspend painting, resume painting, edit control, c#, vb.net, performance optimization, page 299] -->
```