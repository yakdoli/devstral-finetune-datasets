```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_880.jpeg
document_name: tools
page_number: 880
page_id: tools#page_880
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:40:18Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses the configuration and properties of the NumericUpDownExt control in Windows Forms.
- Covers setting the `MaxLength`, enabling `ReadOnly` mode, and adjusting `Alignment` settings.
- Focuses on precise control over text alignment and input restrictions using specific properties.

## Content

### Setting `MaxLength`

```vb
Me.numericUpDownExt1.MaxLength = 32800
```

#### ReadOnly

The ReadOnly mode can be enabled for the NumericUpDownExt control using the below given property.

| NumericUpDownExt Property | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| ReadOnly                  | Gets / sets a value indicating whether the text can be changed by the use of the up or down buttons only. |

```csharp
this.numericUpDownExt1.ReadOnly = true;
```

```vb
Me.numericUpDownExt1.ReadOnly = True
```

### Alignment Settings: Text Alignment

The text of the NumericUpDownExt control can be aligned using the below given property.

#### Text Alignment

The text of the NumericUpDownExt control can be aligned using the below given property.

| NumericUpDownExt Property | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| TextAlign                 | Gets / sets the alignment of the text in the spin box (also known as an up-down control). <br> It includes the below given options: <br> Left <br> Right and |

---

```html
<!-- tags: [NumericUpDownExt, Windows Forms, maxLength, ReadOnly, Alignment] keywords: [numericUpDownExt, text alignment, readonly mode, up-down control] -->
```
```