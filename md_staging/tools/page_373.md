```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_373.jpeg
document_name: tools
page_number: 373
page_id: tools#page_373
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:08:12Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Sets the SelectionStart property of the ButtonEdit control.
- Programming examples in C# and VB.NET.
- Notes on modifying the height of the ButtonEdit control.
- Overview of Smart Tag features in the ButtonEdit control.

## Content

### SelectionStart

| **SelectionStart** | **Description** |
| --- | --- |
| Sets the SelectionStart property of the ButtonEdit control which is the same as the TextBoxBase.SelectionStart of the embedded TextBox. This property setting can be reset to default by calling the ResetSelectionStart method. |  |

#### C#

```csharp
this.buttonEdit1.SelectionLength = 1;
this.buttonEdit1.SelectionStart = 3;
this.buttonEdit1.ShowTextBox = true;
```

#### VB.NET

```vb
Me.buttonEdit1.SelectionLength = 1
Me.buttonEdit1.SelectionStart = 3
Me.buttonEdit1.ShowTextBox = True
```

**Note:** To increase the height of the ButtonEdit control, make the text as multiline textbox.

### 3.5.2.2.3.4 Design Time Features

The ButtonEdit control has Smart Tag, which lets you set the properties easily.

#### Smart Tag Options

![](attachment://image.png)

## Smart Tag Options

- **Appearance**
  - Show TextBox
  - Text Alignment: Left
  - Button Styles: WindowsXP
  - UseVisualStyle

- **Behavior**
  - Character Casing: Normal
  - Buttons Collection: (Collection)

- **Design**
  - Name: buttonEdit1

## API Reference

### Properties
- **SelectionStart**: Sets the SelectionStart property.

### Methods
- **ResetSelectionStart**: Resets the SelectionStart property to default.

## Code Examples

#### C#

```csharp
this.buttonEdit1.SelectionLength = 1;
this.buttonEdit1.SelectionStart = 3;
this.buttonEdit1.ShowTextBox = true;
```

#### VB.NET

```vb
Me.buttonEdit1.SelectionLength = 1
Me.buttonEdit1.SelectionStart = 3
Me.buttonEdit1.ShowTextBox = True
```

## Notes

- To modify the height of the ButtonEdit control, make the text as a multiline textbox.

## Smart Tag Features

The Smart Tag on the ButtonEdit control provides easy access to set properties such as text alignment, button styles, and character casing.

### Figure: ButtonEdit Smart Tag Options
![](attachment://image.png)

## See also

- [ButtonEdit Documentation](https://www.syncfusion.com/documentation/windowsforms/buttonedit)
- [Essential Tools for Windows Forms](https://www.syncfusion.com/documentation/windowsforms/)

<!-- tags: [ButtonEdit, SmartTag, SelectionStart, Windows Forms, Design Time Features] keywords: [SelectionStart, TextBox, ButtonEdit, Smart Tag, Windows Forms, Design Time] -->
```