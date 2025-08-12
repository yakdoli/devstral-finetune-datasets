```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_170.jpeg
document_name: edit
page_number: 170
page_id: edit#page_170
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:04:40Z
fidelity: lossless
-->

## Content

### Context Prompt

#### [C#]

```csharp
private void editControl1_ContextPromptOpen(object sender, Syncfusion.Windows.Forms.Edit.ContextPromptUpdateEventArgs e)
{
    // Populate the Context Prompt.
    e.AddPrompt("Control.Items.Add(string text, string tooltipText, int imageIndex, int selectedIndex)", "Specify the text of the item, its tooltip text, image index and selected image index");
    e.AddPrompt("Control.Items.Add(string text, string tooltipText, int imageIndex)", "Specify the text of the item, its tooltip text, and image index");
    e.AddPrompt("Control.Items.Add(string text, string tooltipText)", "Specify the text of the item, and its tooltip text");
}
```

#### [VB.NET]

```vb
Private Sub editControl1_ContextPromptOpen(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.ContextPromptUpdateEventArgs) Handles EditControl1.ContextPromptOpen
    ' Populate the Context Prompt.
    e.AddPrompt("Control.Items.Add(string text, string tooltipText, int imageIndex, int selectedIndex)", "Specify the text of the item, its tooltip text, image index and selected image index")
    e.AddPrompt("Control.Items.Add(string text, string tooltipText, int imageIndex)", "Specify the text of the item, its tooltip text, and image index")
    e.AddPrompt("Control.Items.Add(string text, string tooltipText)", "Specify the text of the item, and its tooltip text")
End Sub
```

### Customization

#### Background Brush

The brush for the Context Prompt background is set by using the `ContextPromptBackgroundBrush` property of the Edit Control.

```csharp
this.editControl1.ContextPromptBackgroundBrush = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.BackwardDiagonal, System.Drawing.Color.PapayaWhip, System.Drawing.Color.LemonChiffon);
```

---

## Index

### Tags
- Syncfusion Winforms
- context prompt
- customization
- background brush
- ContextPromptBackgroundBrush
- C#
- VB.NET
- GradientStyle

### Keywords
- context prompt open
- add prompt
- string text
- tooltip text
- image index
- selected image index
- background brush
- brush info
- gradient style
- lemon chiffon
- papaya whip

<!-- tags: [Syncfusion Winforms, context prompt] keywords: [context prompt open, add prompt, string text, tooltip text, image index, selected image index, background brush, brush info, gradient style, lemon chiffon, papaya whip] -->
```