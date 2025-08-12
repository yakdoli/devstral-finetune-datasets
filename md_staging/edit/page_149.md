```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_149.jpeg
document_name: edit
page_number: 149
page_id: edit#page_149
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:03:47Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Scrollbar Buttons

### C#

```csharp
this.editControl1.ScrollbarLeftButtons.AddRange(new System.Windows.Forms.Control[] { this.scrollBarButton2 });
this.editControl1.ScrollbarRightButtons.AddRange(new System.Windows.Forms.Control[] { this.scrollBarButton3 });
this.editControl1.ScrollbarTopButtons.AddRange(new System.Windows.Forms.Control[] { this.scrollBarButton4 });
```

### [VB.NET]

```vb
Me.editControl1.ScrollbarBottomButtons.AddRange(New System.Windows.Forms.Control() { Me.scrollBarButton1 })
Me.editControl1.ScrollbarLeftButtons.AddRange(New System.Windows.Forms.Control() { Me.scrollBarButton2 })
Me.editControl1.ScrollbarRightButtons.AddRange(New System.Windows.Forms.Control() { Me.scrollBarButton3 })
Me.editControl1.ScrollbarTopButtons.AddRange(New System.Windows.Forms.Control() { Me.scrollBarButton4 })
```

## Scroll Position and Offsets

The scroll position and offsets of the Edit Control are set by using the below given properties.

| Edit Control Property      | Description                       |
|---------------------------|------------------------------------|
| ScrollPosition            | Gets / sets scroll position of Edit Control. |
| ScrollOffsetBottom        | Gets / sets the bottom scroll offset. |
| ScrollOffsetLeft          | Gets / sets the left scroll offset. |
| ScrollOffsetRight         | Gets / sets the right scroll offset. |
| ScrollOffsetTop           | Gets / sets the top scroll offset. |

### C#

```csharp
this.editControl1.ScrollPosition = new Point(1, 5);

this.editControl1.ScrollOffsetBottom = 5;
this.editControl1.ScrollOffsetLeft = 10;
this.editControl1.ScrollOffsetTop = 5;
this.editControl1.ScrollOffsetTop = 10;
```

### [VB.NET]

```vb
' Code will be provided here if available
```

## Page-level Navigation/TOC (if applicable)
- [Content]
  - [Scrollbar Buttons]
  - [Scroll Position and Offsets]

<!-- tags: [Windows Forms, Edit Control, Scrollbar Buttons, Scroll Position, Offsets] keywords: [scroll position, scroll offset, edit control, Windows Forms, Syncfusion] -->
```