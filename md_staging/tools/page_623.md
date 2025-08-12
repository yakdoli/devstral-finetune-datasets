```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_623.jpeg
document_name: tools
page_number: 623
page_id: tools#page_623
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:25:16Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Figure 382: Retrieving Columns other than Display and Value Members

#### 3.5.5.4.5.5 How to change the back color and text color of the selected item?

Using `PrepareViewStyleInfo` event of the Grid that is embedded in the MultiColumnComboBox, you can change the back color and text color of the selected item. This is illustrated in the following code.

#### C#

```csharp
GridControl gc = this.multiColumnComboBox1.ListBox.Grid;
gc.PrepareViewStyleInfo += new GridPrepareViewStyleInfoEventHandler(gc_PrepareViewStyleInfo);
gc.AlphaBlendSelectionColor = Color.Transparent;

void gc_PrepareViewStyleInfo(object sender,
                             GridPrepareViewStyleInfoEventArgs e)
{
    GridCurrentCell cc = this.gc.CurrentCell;
    if (e.RowIndex == cc.RowIndex)
    {
        e.Style.BackColor = SystemColors.Highlight;
        e.Style.TextColor = SystemColors.HighlightText;
    }
}
```

#### VB.NET

```vb
Private gc As GridControl = Me.multiColumnComboBox1.ListBox.Grid
gc.PrepareViewStyleInfo += New GridPrepareViewStyleInfoEventHandler(gc_PrepareViewStyleInfo)
```

## References

Cross References:
- [MultiColumnComboBox](#unclear)
- [GridPrepareViewStyleInfoEventHandler](#unclear)

## Page-level Navigation/TOC
- Essential Tools for Windows Forms
  - Figure 382: Retrieving Columns other than Display and Value Members
  - 3.5.5.4.5.5 How to change the back color and text color of the selected item?

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [MultiColumnComboBox, GridPrepareViewStyleInfoEventHandler, Color, SystemColors, Highlight, HighlightText, back color, text color, selected item] -->
```