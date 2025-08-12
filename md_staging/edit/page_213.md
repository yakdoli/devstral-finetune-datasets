```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_213.jpeg
document_name: edit
page_number: 213
page_id: edit#page_213
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:07:40Z
fidelity: lossless
-->

## Overview
- Describes the customization of the User Margin in the Syncfusion Windows Forms Edit Control with background settings and customized text.
- Highlights the use of the `DrawUserMarginText` event for setting custom text on a line-by-line basis.
- Demonstrates how to customize font settings for User Margin text using C# and VB.NET examples.

## Content

### Customizing the User Margin

It is possible to set custom text in the User Margin on a line-by-line basis by handling the `DrawUserMarginText` event of the Edit Control. Moreover, it is also possible to customize the font settings for the text of the User Margin.

#### Figure 67: User Margin with Background Settings and Customized Text

![Figure: User Margin with Background Settings and Customized Text](#)

**Figure 67: User Margin with Background Settings and Customized Text**

#### Implementation in C#

```csharp
private void editControl1_DrawUserMarginText(object sender, Syncfusion.Windows.Forms.Edit.DrawUserMarginTextEventArgs e)
{
    // Set text to be rendered at the user margin area.
    e.Text = "Line " + e.Line.LineIndex.ToString() + " contains " + e.Line.LineLength.ToString() + " characters";
    // Set text font.
    e.Font = new Font("Garamond", 11);
    if (e.Line.LineIndex % 2 == 0)
    {
        // Set color of the text.
        e.Color = Color.Blue;
    }
}
```

#### Implementation in VB.NET

```vb
Private Sub editControl1_DrawUserMarginText(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.DrawUserMarginTextEventArgs) Handles EditControl1.DrawUserMarginText
    ' Set text to be rendered at the user margin area.
    e.Text = "Line " + e.Line.LineIndex.ToString() + " contains " + e.Line.LineLength.ToString() + " characters"
    ' Set text font.
    e.Font = New Font("Garamond", 11)
    If e.Line.LineIndex Mod 2 = 0 Then
        ' Set color of the text.
        e.Color = Color.Blue
    End If
End Sub
```

### APIs Used
- `Syncfusion.Windows.Forms.Edit.DrawUserMarginTextEventArgs`
- `Font`
- `Color`

### Notes
- The `DrawUserMarginText` event allows dynamic customization of the User Margin, enabling the display of specific information like character counts.
- Font and color customization can enhance the usability and visual appeal of the User Margin.

<!-- tags: [Syncfusion Winforms, Edit Control, User Margin, DrawUserMarginText] keywords: [custom text, font settings, line-by-line customization, character count, Garamond font, Blue color] -->
```