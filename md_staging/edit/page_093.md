```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_093.jpeg
document_name: edit
page_number: 093
page_id: edit#page_093
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:59:58Z
fidelity: lossless  
-->

# Essential Edit for Windows Forms

Consider the following example.

## Example Code

```csharp
public void Test()
{
    string str;
    str = "}";
}
```

If the cursor is positioned on the end curly brace, most editors will match to the open curly brace in the string. On the contrary, Edit Control matches to the open curly brace for the method.

## Bracket Highlighting and Indentation Guidelines

The Bracket Highlighting and Indentation Guidelines functionalities are supported using the following APIs in the Edit Control.

### Supported APIs

- ShowIndentationGuidelines
- HideIndentationGuidelines
- ShowIndentGuideline
- IndentLineColor
- IndentBlockHighlightingColor
- IndentationBlockBackgroundBrush
- IndentationBlockBorderColor
- IndentationBlockBorderStyle
- JumpToIndentBlockStart
- JumpToIndentBlockEnd
- OnlyHighlightMatchingBraces

### Description of APIs

The preceding APIs are explained below in detail.

#### Indentation Guidelines

The indentation guidelines are vertical lines that connect the matching brackets. This feature enhances the readability of code.

| Edit Control Property            | Description                                   |
|-----------------------------------|-----------------------------------------------|
| ShowIndentationGuidelines       | Gets / sets value indicating whether indentation guidelines should be shown. |

#### Turning Indentation Guidelines On/Off

The indentation guidelines can be turned on by setting the `ShowIndentationGuidelines` property to `True`. It can be turned off either by setting this property to `False`, or by invoking the `HideIndentationGuideline` method.

## Footer
**© 2013 Syncfusion. All rights reserved.**
Page 93
<!-- tags: [product, Indentation Guidelines, Bracket Matching, C#, Syncfusion Winforms] keywords: [Indentation Guidelines, ShowIndentationGuidelines, HideIndentationGuidelines, Bracket Matching, Editor Features] -->
```