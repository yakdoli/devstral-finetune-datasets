```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_775.jpeg
document_name: tools
page_number: 775
page_id: tools#page_775
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:55Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Textbox Properties and Methods

- Demonstrates setting various properties of a textbox control in Windows Forms using both C# and VB.NET.

### Code Examples

#### C#

```csharp
this.percentTextBox1.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
this.percentTextBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
this.percentTextBox1.SelectedText = "34";
this.percentTextBox1.SelectAllOnFocus = true;
this.percentTextBox1.SwitchModeOnFocus = true;
this.percentTextBox1.HideSelection = true;
this.percentTextBox1.ClipText = "34";
this.percentTextBox1.DrawActiveWhenDisabled = true;
```

#### VB.NET

```vb
Me.percentTextBox1.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
Me.percentTextBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
Me.percentTextBox1.SelectedText = "34"
Me.percentTextBox1.SelectAllOnFocus = true
Me.percentTextBox1.SwitchModeOnFocus = True
Me.percentTextBox1.HideSelection = True
Me.percentTextBox1.ClipText = "34"
Me.percentTextBox1.DrawActiveWhenDisabled = True
```

### Figures

- **Figure 489: Character Case set to "Upper"**
  ![PERCENTTEXTBOX](image_link_for_489)

- **Figure 490: Text Aligned to the "Center"**
  ![34_installed](image_link_for_490)

- **Figure 491: "SelectAllOnFocus" property Set**
  ![34_activated](image_link_for_491)

### Associated Methods

The methods associated with the above properties are given below.

## API Reference

### Methods
- `CharacterCasing`: Sets the text to a specified case (Upper, Lower, or Normal).
- `TextAlign`: Aligns the text within the control (Left, Right, Center).
- `SelectedText`: Sets the text that is selected when the control is activated.
- `SelectAllOnFocus`: Selects all text when the control receives focus.
- `SwitchModeOnFocus`: Changes the control's mode when it receives focus.
- `HideSelection`: Hides the selected text when the control loses focus.
- `ClipText`: Clips the text to a specified substring.
- `DrawActiveWhenDisabled`: Draws the active state even when the control is disabled.

## Code Examples (cont.)

- The provided code snippets demonstrate how to set these properties programmatically in both C# and VB.NET, ensuring consistent behavior across different platforms.

## Page-level Navigation/TOC

- **1. Textbox Properties**
  - CharacterCasing
  - TextAlign
  - SelectedText
  - SelectAllOnFocus
  - SwitchModeOnFocus
  - HideSelection
  - ClipText
  - DrawActiveWhenDisabled

- **2. Figures Illustrating Properties**
  - Figure 489: Character Case
  - Figure 490: Text Alignment
  - Figure 491: SelectAllOnFocus

## Cross References

- See also:
  - Additional WinForms Controls
  - Advanced Usage of Textbox Controls
  - Event Handling in Textbox Controls

<!-- tags: [Syncfusion Winforms, Textbox, Properties, Methods, C#, VB.NET, CharacterCasing, TextAlign, SelectedText, SelectAllOnFocus, SwitchModeOnFocus, HideSelection, ClipText, DrawActiveWhenDisabled] keywords: [Windows Forms, Textbox Control, String Alignment, Selection, Focus, Character Case, Advanced WinForms Features] -->
```
