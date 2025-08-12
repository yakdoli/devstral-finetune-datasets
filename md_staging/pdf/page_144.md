<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_144.jpeg
document_name: pdf
page_number: 144
page_id: pdf#page_144
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:32:29Z
fidelity: lossless
-->

## Overview
- Skip: Enables to skip the entire row
- MinimalHeight: Enables to specify the minimal row height, which is used to preserve space for images

## Content

### Setting Row Height

The following code example illustrates how to set the row height.

#### Code Example: C#

```csharp
// Subscribing the event
pdfLightTable.BeginRowLayout
    += new BeginRowLayoutEventHandler(pdfLightTable_BeginRowLayout);

// Setting row height for the second row
void pdfLightTable_BeginRowLayout(object sender, BeginRowLayoutEventArgs args)
{
    if (args.RowIndex == 1)
    {
        args.MinimalHeight = 25;
    }
}
```

#### Code Example: VB.NET

```vb
' Subscribing the event
Private pdfLightTable.BeginRowLayout
    += New BeginRowLayoutEventHandler(pdfLightTable_BeginRowLayout)

' Setting rowheight for the second row
Private Sub pdfLightTable_BeginRowLayout(ByVal sender As Object, ByVal args As BeginRowLayoutEventArgs)
    If args.RowIndex = 1 Then
        args.MinimalHeight = 25
    End If
End Sub
```

### 4.1.2.3.1.4.4 EndRowLayout

This event is raised when row layout finishes. The arguments of this event are as follows:

- **RowIndex (read-only):** Index of the row (zero-based)
- **Cancel:** Enables to cancel layout
- **LayoutCompleted (read-only):** Gets a value indicating whether the row was drawn completely.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, row layout, BeginRowLayout, EndRowLayout, MinimalHeight] keywords: [skip row, minimal row height, event handler, layout completed, syncfusion] -->