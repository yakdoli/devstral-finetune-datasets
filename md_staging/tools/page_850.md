<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_850.jpeg
document_name: tools
page_number: 850
page_id: tools#page_850
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:38:50Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

|  | when the edit control loses focus. |
| --- | --- |
| ClipText | Returns the clipped text without the formatting. |
| DrawActiveWhenDisabled | Specifies if the text should be drawn active, even when disabled. |

```csharp
[this.maskedEditBox1.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
this.maskedEditBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
this.maskedEditBox1.SelectedText = "34";
this.maskedEditBox1.HideSelection = true;
this.maskedEditBox1.ClipText = "34";
this.maskedEditBox1.DrawActiveWhenDisabled = true;
]
```

```vbnet
[Me.maskedEditBox1.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
Me.maskedEditBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
Me.maskedEditBox1.SelectedText = "34"
Me.maskedEditBox1.HideSelection = True
Me.maskedEditBox1.ClipText = "34"
Me.maskedEditBox1.DrawActiveWhenDisabled = True
]
```

[![Syncfusion](https://via.placeholder.com/150 "Character Case set to 'Upper'")](https://via.placeholder.com/150)
**Figure 542: Character Case set to "Upper"**

[![Syncfusion](https://via.placeholder.com/150 "Text Aligned to the 'Center'")](https://via.placeholder.com/150)
**Figure 543: Text Aligned to the "Center"**

The methods associated with the above properties are given below.

| Methods | Description |
| --- | --- |
| AppendText | Appends the text to the current text of a |

### Page-level Navigation/TOC (if applicable)

- Properties
  - ClipText
  - DrawActiveWhenDisabled
- Methods
  - AppendText

### Code Examples (multi-language supported)

C#:

```csharp
this.maskedEditBox1.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
this.maskedEditBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
this.maskedEditBox1.SelectedText = "34";
this.maskedEditBox1.HideSelection = true;
this.maskedEditBox1.ClipText = "34";
this.maskedEditBox1.DrawActiveWhenDisabled = true;
```

VB.NET:

```vbnet
Me.maskedEditBox1.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
Me.maskedEditBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
Me.maskedEditBox1.SelectedText = "34"
Me.maskedEditBox1.HideSelection = True
Me.maskedEditBox1.ClipText = "34"
Me.maskedEditBox1.DrawActiveWhenDisabled = True
```

### RAG Annotations
<!-- tags: [WinForms, properties, methods, CharacterCasing, TextAlign, SelectedText, HideSelection, ClipText, DrawActiveWhenDisabled] keywords: [Character Case, Text Alignment, Selected Text, Hide Selection, Clipped Text, DrawActive] -->