```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_360.jpeg
document_name: tools
page_number: 360
page_id: tools#page_360
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:07:55Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates associating a `TextBoxExt` control with a `ButtonEdit` control and configuring child buttons.
- Shows how to set the alignment and text for child buttons.
- Explains how to add `ButtonEditChildButtons` to the `ButtonEdit` control and add it to the form.

## Content

### Step 1: Associating the TextBoxExt Control

In this step, we associate the `TextBoxExt` control with the `ButtonEdit` control.

```csharp
Me.buttonEdit1.TextBox = Me.textBox1
```

### Step 2: Setting the Alignment and Text for the Buttons

#### [C#]

```csharp
// Setting Button alignment for Child Button 1
// By default the alignment for other buttons will be right
this.buttonEditChildButton1.ButtonAlign = ButtonAlignment.Left;

// Setting text for child Buttons.
this.buttonEditChildButton1.Text = "L";
this.buttonEditChildButton2.Text = "R";
this.buttonEditChildButton3.Text = "E";
```

#### [VB.NET]

```vb.net
' Setting Button alignment for Child Button 1.
' By default the alignment for other buttons will be right
Me.buttonEditChildButton1.ButtonAlign = ButtonAlignment.Left

' Setting text for child Buttons
Me.buttonEditChildButton1.Text = "L"
Me.buttonEditChildButton2.Text = "R"
Me.buttonEditChildButton3.Text = "E"
```

### Step 3: Add ButtonEditChildButtons to the ButtonEdit and Add it to the Form

#### [C#]

```csharp
this.buttonEdit1.Buttons.Add(this.buttonEditChildButton1);
this.buttonEdit1.Buttons.Add(this.buttonEditChildButton2);
this.buttonEdit1.Buttons.Add(this.buttonEditChildButton3);

this.Controls.Add(this.buttonEdit1);
```

#### [VB.NET]

```vb.net
Me.buttonEdit1.Buttons.Add(Me.buttonEditChildButton1)
Me.buttonEdit1.Buttons.Add(Me.buttonEditChildButton2)
Me.buttonEdit1.Buttons.Add(Me.buttonEditChildButton3)

Me.Controls.Add(Me.buttonEdit1)
```

## API Reference

- **Namespace**: Syncfusion.Windows.Forms
- **Class**: ButtonEdit
- **Properties**
  - **TextBox**: `System.Windows.Forms.TextBox`
    - Associates a TextBoxExt control with the ButtonEdit.
  - **ButtonAlign**: `ButtonAlignment`
    - Sets the alignment of the button relative to the text box.
  - **Text**: `string`
    - Sets the text displayed on the button.

## Code Examples

### C# Example

```csharp
// Associating the TextBoxExt control
Me.buttonEdit1.TextBox = Me.textBox1;

// Setting alignment and text for child buttons
this.buttonEditChildButton1.ButtonAlign = ButtonAlignment.Left;
this.buttonEditChildButton1.Text = "L";
this.buttonEditChildButton2.Text = "R";
this.buttonEditChildButton3.Text = "E";

// Adding child buttons and the ButtonEdit to the form
this.buttonEdit1.Buttons.Add(this.buttonEditChildButton1);
this.buttonEdit1.Buttons.Add(this.buttonEditChildButton2);
this.buttonEdit1.Buttons.Add(this.buttonEditChildButton3);
this.Controls.Add(this.buttonEdit1);
```

### VB.NET Example

```vb.net
' Associating the TextBoxExt control
Me.buttonEdit1.TextBox = Me.textBox1

' Setting alignment and text for child buttons
Me.buttonEditChildButton1.ButtonAlign = ButtonAlignment.Left
Me.buttonEditChildButton1.Text = "L"
Me.buttonEditChildButton2.Text = "R"
Me.buttonEditChildButton3.Text = "E"

' Adding child buttons and the ButtonEdit to the form
Me.buttonEdit1.Buttons.Add(Me.buttonEditChildButton1)
Me.buttonEdit1.Buttons.Add(Me.buttonEditChildButton2)
Me.buttonEdit1.Buttons.Add(Me.buttonEditChildButton3)
Me.Controls.Add(Me.buttonEdit1)
```

## Cross References

- See also:
  - [ButtonAlignment Enum](#buttonalignment-enum)
  - [ButtonEdit Control](#buttonedit-control)

<!-- tags: [Syncfusion Winforms, ButtonEdit, TextBoxExt, ButtonAlignment, ChildButtons] keywords: [ButtonEdit, TextBoxExt, ButtonAlignment, ButtonEditChildButtons, Windows Forms, Syncfusion] -->
```