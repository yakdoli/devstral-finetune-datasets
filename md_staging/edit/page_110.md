```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_110.jpeg
document_name: edit
page_number: 110
page_id: edit#page_110
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:00:56Z
fidelity: lossless
-->

## Word Wrap Settings in Edit Control

### Overview
- Explanation of word wrap margin based on Edit Control's width and TextArea width.
- Different modes of text wrapping: Control and SpecifiedColumn.
- WordWrapColumnMeasuringFont property for font measuring.
- Specifying WordWrapColumn for wrapping text.
- TextAreaWidth property to control the text area width.
- WrappedLinesOffset for line wrapping offset.

### WinForms-specific Properties

| Property Name                        | Description                                                                 |
|---------------------------------------|-----------------------------------------------------------------------------|
| WordWrapMode                         | Determines where the text wraps. <br> <br> - `Control` - wraps at the edge of the Edit Control. <br> - `SpecifiedColumn` - wraps at the specified column in WordWrapColumn property. <br> The default is `Control`. |
| WordWrapColumnMeasuringFont          | Gets or sets the font used for calculating the position of WordWrapColumn. |
| WordWrapColumn                       | Specifies the column for wrapping text. Used when WordWrapMode is `SpecifiedColumn`. <br> Default value is 100. |
| TextAreaWidth                        | Gets or sets the width of the text area of the Edit Control. <br> Default value is 600. |
| WrappedLinesOffset                   | Specifies the offset of wrapped lines. |

### Code Example in C#

```csharp
// Sets the WordWrap mode.
this.editControl1.WordWrapMode = Syncfusion.Windows.Forms.Edit.Enums.WordWrapMode.WordWrapMargin;

// Sets font that is used while calculating the position of the WordWrap column.
this.editControl1.WordWrapColumnMeasuringFont = new System.Drawing.Font("Arial", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));

// Specifies column for wrapping text.
this.editControl1.WordWrapColumn = 125;
```

### Cross References
- Refer to Syncfusion documentation for detailed usage scenarios and additional properties related to the Edit Control.

<!-- tags: [syncfusion, winforms, edit control, word wrap, text area, line wrapping, c#] keywords: [wordwrapmode, wordwrapcolumn, textareawidth, wrappedlinesoffset, font measuring, text wrapping] -->
```