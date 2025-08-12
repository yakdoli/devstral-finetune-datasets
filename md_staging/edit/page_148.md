```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_148.jpeg
document_name: edit
page_number: 148
page_id: edit#page_148
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:02:37Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Content

### Scroll Bar Buttons

**Figure 51: Scrolling support in Edit Control**

Buttons can be displayed at the top, bottom, left, or right of the scroll bars by using the following properties:

| Edit Control Property             | Description                                      |
|-----------------------------------|--------------------------------------------------|
| ScrollbarBottomButtons           | Gets buttons at the bottom of the vertical scrollbar. |
| ScrollbarLeftButtons             | Gets buttons on the left of the vertical scrollbar. |
| ScrollbarRightButtons            | Gets buttons on the right of the vertical scrollbar. |
| ScrollbarTopButtons              | Gets buttons at the top of the vertical scrollbar.  |

### Code Example

```csharp
this.editControl1.ScrollbarBottomButtons.AddRange(new System.Windows.Forms.Control[] { this.scrollbarButton1 });
```

## API Reference

### Properties
- **ScrollbarBottomButtons**: Gets buttons at the bottom of the vertical scrollbar.
- **ScrollbarLeftButtons**: Gets buttons on the left of the vertical scrollbar.
- **ScrollbarRightButtons**: Gets buttons on the right of the vertical scrollbar.
- **ScrollbarTopButtons**: Gets buttons at the top of the vertical scrollbar.

<!-- tags: [syncfusion, winforms, edit control, scrolling, buttons, api] -->
```