```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_745.jpeg
document_name: tools
page_number: 745
page_id: tools#page_745
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:31:06Z
fidelity: lossless
-->

## 3.5.8.4.3.3

### Text Settings

This section discusses the text settings of the IntegerTextBox control.

The text associated with the IntegerTextBox control can be set and customized using the below given settings.

| IntegerTextBox Properties | Description                                                                         |
|---------------------------|--------------------------------------------------------------------------------------|
| Text                      | Specifies the text associated with the control.                                     |
| TextAlign                 | Indicates how the text should be aligned for edit controls.                         |
| SelectedText              | Gets / sets the selected text in the IntegerTextBox.                                |
| SelectAllOnFocus          | Specifies if the text should be selected when the control gets the focus.          |
| ClipText                  | Returns the clipped text without the formatting.                                   |

#### [C#]

```csharp
this.integerTextBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
this.integerTextBox1.SelectedText = "-12345678";
this.integerTextBox1.SelectAllOnFocus = true;
this.integerTextBox1.ClipText = "12";
```

#### [VB.NET]

```vb
Me.integerTextBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
Me.integerTextBox1.SelectedText = "-12345678"
Me.integerTextBox1.SelectAllOnFocus = true
Me.integerTextBox1.ClipText = "12"
```

![text_aligned_center](attachment:Figure_471_Text_Aligned_to_the_"Center".png)  
*Figure 471: Text Aligned to the "Center"*

![text_box_content](attachment:content_text_box.png)

<!-- end of page content -->
<!-- tags: [Syncfusion Winforms, IntegerTextBox, text settings, C#, VB.NET, text alignment] keywords: [IntegerTextBox, TextAlign, SelectedText, SelectAllOnFocus, ClipText] -->
```