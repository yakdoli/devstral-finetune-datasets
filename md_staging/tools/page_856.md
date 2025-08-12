```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_856.jpeg
document_name: tools
page_number: 856
page_id: tools#page_856
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:38:58Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

|  |  |
| --- | --- |
| PassivePromptCharacter. |

## Implementation Details

### [C#]

```csharp
this.maskedEditBox1.AllowPrompt = true;
this.maskedEditBox.PaddingCharacterInt = 0;
this.maskedEditBox1.PromptCharacterInt = 37;
this.maskedEditBox1.PassivePromptCharacterInt = 47;
```

### [VB.NET]

```vb
Me.maskedEditBox1.AllowPrompt = True
Me.maskedEditBox.PaddingCharacterInt = 0
Me.maskedEditBox1.PromptCharacterInt = 37
Me.maskedEditBox1.PassivePromptCharacterInt = 47
```

**Note:** We can trim the additional spaces present in the mask by setting the `PaddingCharacterInt` property to `0`.

## MaxLength

The maximum length of the text can be set using the property given below.

### MaskedEditBox Property

| MaskedEditBox Property | Description |
| --- | --- |
| MaxLength | Specifies the maximum number of characters that can be entered into the edit control. The default value is set to `32767`. |

### [C#]

```csharp
this.maskedEditBox1.MaxLength = 32800;
```

### [VB]

```vb
Me.maskedEditBox1.MaxLength = 32800
```

## ReadOnly

The ReadOnly mode can be enabled for the MaskedEditBox control using the below given property.

---

<!-- tags: [winforms, maskededitbox, property, maxlength, readonly] keywords: [maskeditbox, allowprompt, paddingcharacterint, promptcharacterint, passivepromptcharacterint, max length, read only] -->
```