```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_254.jpeg
document_name: edit
page_number: 254
page_id: edit#page_254
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:22Z
fidelity: lossless
-->

## Essentia ledit for Windows Forms

```vb.net
Private Sub editControl1_IndicatorMarginDoubleClick(ByVal sender As Object, ByVal e Syncfusion.Windows.Forms.Edit.IndicatorClickEventArgs)
    Console.WriteLine(" IndicatorMarginDoubleClick event is raised ")
End Sub
```

### 4.14.10.3 DrawLineMark Event

This event occurs when a custom line mark should be drawn.

The event handler receives an argument of type `DrawLineMarkEventArgs`. The following `DrawLineMarkEventArgs` members provide information specific to this event.

| Member       | Description                                                                 |
|--------------|------------------------------------------------------------------------------|
| CustomDraw   | If set to `True`, user handles drawing of the bookmark.                   |
| Graphics     | Graphics object.                                                           |
| MarkRect     | Rectangle where line mark should be drawn.                                |
| PhysicalLine | Virtual line number.                                                       |
| VirtualLine  | Physical line number.                                                      |

```csharp
private void editControl1_DrawLineMark(object sender, Syncfusion.Windows.Forms.Edit.DrawLineMarkEventArgs e)
{
    if (e.VirtualLine % 2 == 0)
    {
        Brush brush = new LinearGradientBrush(e.MarkRect, Color.Red, Color.Yellow, LinearGradientMode.Vertical);
        e.Graphics.FillRectangle(brush, e.MarkRect);
        e.Graphics.DrawRectangle(Pens.IndianRed, e.MarkRect);
    }
}
```

```vb.net

```

<!-- tags: [WinForms, line mark, DrawLineMarkEventArgs] keywords: [event, draw, line mark, custom drawing, bookmark, virtual line number, physical line number] -->
```