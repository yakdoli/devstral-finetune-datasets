```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_204.jpeg
document_name: edit
page_number: 204
page_id: edit#page_204
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:05:44Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
this.editControl.TopVerticalSplitterPosition = 260;
this.editControl.BottomVerticalSplitterPosition = 260;
```

```vb
Me.editControl.HorizontalSplitterPosition = 220
Me.editControl.TopVerticalSplitterPosition = 260
Me.editControl.BottomVerticalSplitterPosition = 260
```

## SplitFourQuadrants Method

The `SplitFourQuadrants` method is used to split the Edit Control into four equal parts.

```csharp
this.editControl.SplitFourQuadrants();
```

```vb
Me.editControl.SplitFourQuadrants()
```

![Split Views Demo](./Split_VIEWS_DEMO.png)

## Overview

- Configures the Edit Control to split into four equal parts.
- Allows simultaneous editing in four separate sections.

## Content

### Split Views

The `SplitFourQuadrants` method provides a layout that divides the Edit Control into four sections for efficient multitasking and dual-screen functionality. This is particularly useful in scenarios requiring parallel code editing or multi-file management.

### Screenshot Explanation

The provided screenshot illustrates the usage of `SplitFourQuadrants` with four sections split:
- Top-left: Code snippet related to `menuItem7` and `menuItem8`.
- Top-right: Code snippet related to `menuItem8` and `menuItem9`.
- Bottom-left: Initialization code for form properties like `ClientSize`, `Controls`, and form appearance.
- Bottom-right: Main entry point of the application, including the `Main` method.

## Cross References

See also:
- Properties of `editControl`
- Other split methods like `SplitHorizontal` and `SplitVertical`

<!-- tags: [Syncfusion, Winforms, EditControl, SplitFourQuadrants, Windows Forms] keywords: [EditControl, Quadrants, Split, Windows Forms, Multitasking, Code Editing, Layout] -->
```