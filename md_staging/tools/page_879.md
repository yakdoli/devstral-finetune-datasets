```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_879.jpeg
document_name: tools
page_number: 879
page_id: tools#page_879
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:41:18Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
Dim ud As NumericupdownnextDerived = New NumericupdownnextDerived
ud.Location = New Point(200, 200)
ud.Minimum = -100
ud.NegativeColor = Color.Red
Controls.Add(ud)
```

## Behavior Settings
The behavior settings of the NumericUpdownExt control are discussed below.

### Intercept Arrow Keys

The arrow keys can be used to select values using the below given property.

| NumericUpdownExt Property | Description |
| -------------------------- | ----------- |
| InterceptArrowKeys         | Gets / sets a value indicating whether the user can use the UP and DOWN ARROW keys to select values. |

```csharp
this.numericUpdownExt1.InterceptArrowKeys = true;
```

```vb
Me.numericUpdownExt1.InterceptArrowKeys = True
```

### MaxLength

The maximum length of the text can be set using the property given below.

| NumericUpdownExt Property | Description |
| -------------------------- | ----------- |
| MaxLength                  | Gets / sets the maximum length of the text that can be entered into the editable portion of the control. The default value is set to '32767'. |

```csharp
this.numericUpdownExt1.MaxLength = 32800;
```

## Page-level Navigation/TOC (if applicable)
- Essential Tools for Windows Forms
  - Behavior Settings
    - Intercept Arrow Keys
    - MaxLength

## Cross References
- See also: `NumericUpDownExt`, `InterceptArrowKeys`, `MaxLength`

<!-- tags: windows forms, numericupdownext, tool, behavior settings, arrow keys, max length, version: 11.4.0.26 -->
```