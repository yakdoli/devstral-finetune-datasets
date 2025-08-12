```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_460.jpeg
document_name: grid
page_number: 460
page_id: grid#page_460
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:12Z
fidelity: lossless
-->

## WinForms Grid Property Examples

### ScrollViewTipFormat Property

This property specifies the text to be displayed in the ScrollTip window, allowing for a placeholder to indicate scroll position.

#### Examples

1. **Using C#**
   
   ```csharp
   this.gridControl1.ScrollTipFormat = "Position {0}";
   ```

2. **Using VB.NET**
   
   ```vb
   ' Set the text to be displayed in the ScrollTip window with a placeholder for scroll position.
   Me.gridControl1.ScrollTipFormat = "Position {0}"
   ```

---

### AutoScrolling Property

This property specifies whether to enable or disable automatic scrolling.

#### Examples

1. **Using C#**
   
   ```csharp
   // Enable AutoScrolling.
   this.gridControl1.AutoScrolling = true;
   ```

2. **Using VB.NET**
   
   ```vb
   ' Enable AutoScrolling.
   Me.gridControl1.AutoScrolling = True
   ```

---

### HScroll Property

This property specifies whether to enable or disable the horizontal scroll bar.

#### Examples

1. **Using C#**
   
   ```csharp
   // Enable horizontal scroll bar.
   this.gridControl1.HScroll = true;
   ```

2. **Using VB.NET**
   
   ```vb
   [VB.NET]
   ```
   <!-- tags: [grid, scroll, tip, autoscrolling, hscroll, property, examples, syncfusion, windowsforms] keywords: [scrolling, position, placeholder, horizontal, scrollbar, Enable, Disable, C#, VB.NET, property settings, gridcontrol, scrolltip, grid control] -->
```