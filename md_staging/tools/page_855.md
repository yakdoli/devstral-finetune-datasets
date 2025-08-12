```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_855.jpeg
document_name: tools
page_number: 855
page_id: tools#page_855
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:39:57Z
fidelity: lossless
-->

## Overview
- Demonstrates the Foreground Settings of the MaskedEditBox control.
- Explains the behavior settings and configuration of prompt and padding characters in MaskedEditBox.

## Content

### Foreground Color Setting for MaskedEditBox

A Sample which demonstrates the Foreground Settings of MaskedEditBox control is available in the below sample installation path.

..My Documents\\Syncfusion\\EssentialStudio\\**Version Number**\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\EditorControls

#### Behavior Settings

The behavior settings of the MaskedEditBox control are discussed below.

#### Prompt and Padding Character Settings

MaskedEditBox control allows you to add prompt characters in the input.

| MaskedEditBox Properties             | Description                                                                                                                                                                                     |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AllowPrompt                           | Specifies if the prompt character can be allowed to be entered as an input character.                                                                                                          |
| PaddingCharacter                      | Specifies the character that will be used instead of mask characters when the mask position has not been filled when the text property is used.                                             |
| PaddingCharacterInt                   | Gets / sets the integer version of the padding character.                                                                                                                                     |
| Prompt Character                      | Gets / sets the character that will be used instead of the mask characters when the mask position has not been filled.                                                                      |
| PromptCharacterInt                    | Gets / sets the integer version of the PromptCharacter.                                                                                                                                       |
| PassivePromptCharacter                | Gets / sets the character that will be used instead of the mask characters when the mask position has not been filled (when the control does not have the focus).                            |
| PassivePromptCharacterInt             | Gets / sets the integer version of the                                                                                                                                                        |

---
© 2013 Syncfusion. All rights reserved. | Page

### API Reference

- Focus on the MaskedEditBox properties related to prompt and padding character settings.
- Include descriptions for setting and getting characters for prompt and padding functionality.

### Code Examples

- C# example demonstrating the use of MaskedEditBox with prompt and padding characters.

```csharp
MaskedEditBox maskedEditBox = new MaskedEditBox();
maskedEditBox.AllowPrompt = true;
maskedEditBox.PaddingCharacter = ' ';
maskedEditBox.PromptCharacter = '_';
```

## Cross References
- Refer to earlier sections for foundational information on MaskedEditBox controls.

### RAG Annotations
<!-- tags: [maskededitbox, foregoned-color, prompt-characters, padding-characters] keywords: [maskeditbox control, foreground settings, prompt, padding, character configuration, winforms] -->
```