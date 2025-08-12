```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_676.jpeg
document_name: tools
page_number: 676
page_id: tools#page_676
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:27:50Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The GradientPanelExt offers the following unique events, to make it more flexible to work with.

## Overview
- The GradientPanelExt provides Event support for managing changes in Corner Radius and Primitives.
- These events, `CornerRadiusChanged` and `PrimitivesChanged`, help in handling UI updates dynamically.

## Content

### CornerRadiusChanged Event

This event is raised every time the Corner Radius value is changed.

#### C#
```csharp
private void gradientPanelExt1_CornerRadiusChanged(object sender, EventArgs e)
{
    imagePrimitivel.Position = 100;
}
```

#### VB.NET
```vb.net
Private Sub gradientPanelExt1_CornerRadiusChanged(ByVal sender As Object, ByVal e As EventArgs)
    imagePrimitivel.Position = 100
End Sub
```

### PrimitivesChanged Event

This event is raised when the value of the primitives property is changed.

#### C#
```csharp
private void gradientPanelExt1_PrimitivesChanged(object sender, EventArgs e)
{
    MessageBox.Show("Primitive Value Changed");
}
```

#### VB.NET
```vb.net
Private Sub gradientPanelExt1_PrimitivesChanged(ByVal sender As Object, ByVal e As EventArgs)
    MessageBox.Show("Primitive Value Changed")
End Sub
```

### 3.5.6.4 SplitContainerAdv

## API Reference (if applicable)

## Code Examples (multi-language supported)

### WinForms-specific conventions

## Page-level Navigation/TOC (if applicable)

## Cross References

## RAG Annotations
<!-- tags: [Syncfusion Winforms, GradientPanelExt, Events, CornerRadiusChanged, PrimitivesChanged, SplitContainerAdv] keywords: [GradientPanelExt, Corner Radius, Primitives, Event Support, UI Updates, C#, VB.NET] -->
```