```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_897.jpeg
document_name: tools
page_number: 897
page_id: tools#page_897
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:41:02Z
fidelity: lossless
-->

## Overview
- This page discusses essential tools for Windows Forms, focusing on properties such as `CharacterCasing`, `TextAlign`, `RightToLeft`, `SelectedText`, `HideSelection`, and `DrawActiveWhenDisabled`.
- It provides code examples in both C# and VB.NET, demonstrating how to configure these properties for a `TextBox` control.

## Content

### Properties Summary

| Property                    | Description                                                                           |
|-----------------------------|---------------------------------------------------------------------------------------|
|                             | `selected text in the control.`                                 |
| `HideSelection`            | Indicates that the selection should be hidden when the edit control loses focus.        |
| `DrawActiveWhenDisabled`   | Specifies if the text should be drawn active, even when disabled.                      |

### Code Examples

#### C#
```csharp
this.textBoxExt1.CharacterCasing = System.Windows.Forms.CharacterCasing.Lower;
this.textBoxExt1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
this.textBoxExt1.RightToLeft = System.Windows.Forms.RightToLeft.Yes;
this.textBoxExt1.SelectedText = "TextBoxExt";
this.textBoxExt1.HideSelection = true;
this.textBoxExt1.DrawActiveWhenDisabled = true;
```

#### VB.NET
```vb
Me.textBoxExt1.CharacterCasing = System.Windows.Forms.CharacterCasing.Lower
Me.textBoxExt1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
Me.textBoxExt1.RightToLeft = System.Windows.Forms.RightToLeft.Yes
Me.textBoxExt1.SelectedText = "TextBoxExt"
Me.textBoxExt1.HideSelection = True
Me.textBoxExt1.DrawActiveWhenDisabled = True
```

### Visual Examples

#### Figure 570: Character Case set to "Lower"
![Figure 570: Character Case set to "Lower"](https://via.placeholder.com/200x100?text=Figure%20570)

#### Figure 571: Text Aligned to the "Center"
![Figure 571: Text Aligned to the "Center"](https://via.placeholder.com/200x100?text=Figure%20571)

#### Figure 572: RightToLeft property set to "True"
![Figure 572: RightToLeft property set to "True"](https://via.placeholder.com/200x100?text=Figure%20572)

## Page-Level Navigation/TOC (if applicable)
- [Overview]
- [Content]
    - [Properties Summary]
    - [Code Examples]
        - [C#]
        - [VB.NET]
    - [Visual Examples]

## Cross References
- Related sections or topics may include detailed explanations of each property and their usage scenarios.

<!-- tags: [Essential Tools, Windows Forms, TextBox, Properties, C#, VB.NET, SelectedText, HideSelection, DrawActiveWhenDisabled] keywords: [CharacterCasing, TextAlign, RightToLeft, TextBoxExt, Lower, Center, True, Essential Tools, Windows Forms] -->
```