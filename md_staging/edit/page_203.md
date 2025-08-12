```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_203.jpeg
document_name: edit
page_number: 203
page_id: edit#page_203
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:11Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

The following methods can be used to split the Edit Control into two equal horizontal or vertical halves.

| **Edit Control Method** | **Description**                          |
|-------------------------|------------------------------------------|
| SplitHorizontally      | Splits the Edit Control into two equal horizontal halves. |
| SplitVertically        | Splits the Edit Control into two equal vertical halves.   |

### C#

```csharp
this.editControl1.ShowHorizontalSplitters = true;
this.editControl1.ShowVerticalSplitters = true;

this.editControl1.SplitHorizontally();
this.editControl1.SplitVertically();
```

### VB.NET

```vb
Me.editControl1.ShowHorizontalSplitters = True
Me.editControl1.ShowVerticalSplitters = True

Me.editControl1.SplitHorizontally()
Me.editControl1.SplitVertically()
```

## Positioning

The following properties can be used to position the horizontal and vertical splitters in the Edit Control.

| **Edit Control Property**              | **Description**                          |
|----------------------------------------|------------------------------------------|
| HorizontalSplitterPosition             | Gets / sets position of the horizontal splitter. |
| TopVerticalSplitterPosition            | Gets / sets position of the top vertical splitter. |
| BottomVerticalSplitterPosition         | Gets / sets position of the bottom vertical splitter. |

### C#

```csharp
this.editControl1.HorizontalSplitterPosition = 220;
```

<!-- tags: [Syncfusion, Windows Forms, Edit Control, Splitter, Horizontal, Vertical, Positioning] keywords: [Edit Control, Splitter, Horizontal Splitter, Vertical Splitter, Positioning, Windows Forms] -->
```