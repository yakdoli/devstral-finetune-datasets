```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_298.jpeg
document_name: edit
page_number: 298
page_id: edit#page_298
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:12:24Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```vb
foreground = radioButton6.BackColor
ElseIf radioButton5.Checked Then
    foreground = radioButton5.BackColor
ElseIf radioButton4.Checked Then
    foreground = radioButton4.BackColor
End If
Dim bUseHatchFile As Boolean = comboBox1.SelectedIndex > 0
Dim style As HatchStyle
If bUseHatchFile = True Then
    style = CType([Enum].Parse(GetType(HatchStyle), comboBox1.SelectedItem.ToString()), HatchStyle)
Else
    style = HatchStyle.Min
End If
Dim format As IBackgroundFormat = editControl1.RegisterBackgroundColorFormat(background, foreground, style, bUseHatchFile)
Return format
End Function 'RegisterFormat

' code to set background color for the entire line
Private Sub button1_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles button1.Click
    Dim temp As IDynamicFormat() = editControl1.GetLineBackColorFormats(editControl1.CurrentLine)
    Dim format As IBackgroundFormat = RegisterFormat()
    editControl1.SetLineBackColor(editControl1.CurrentLine, True, format)
End Sub 'button1_Click

Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Load
    comboBox1.Items.Clear()
    comboBox1.Items.Add("Solid")
    Dim name As String
    For Each name In [Enum].GetNames(GetType(HatchStyle))
        comboBox1.Items.Add(name)
    Next name
    comboBox1.SelectedText = "Percent05"
    comboBox1.SelectedIndex = 0
    editControl1.Text += vbCrLf
    editControl1.CurrentLine = 1
End Sub 'Form1_Load

' Code to set background color for the selected text
Private Sub button2_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles button2.Click
    Dim format As IBackgroundFormat = RegisterFormat()
End
```

## Overview
- Configures and registers the background color format for an edit control.
- Handles setting the background color for the entire line and the selected text.
- Populates a combo box with HatchStyle options for selection.

## Content

The provided code demonstrates how to register and apply different background color formats for text within an edit control in a Windows Forms application. It includes components such as radio buttons to select background and foreground colors, a combo box for choosing hatch styles, and buttons to apply these formats to the entire line or the selected text.

### Key Components
- **RegisterFormat Function:**
  - Determines the background and foreground colors based on radio button selections.
  - Specifies whether to use a hatch style and which hatch style to apply.
  - Registers the background color format with the edit control.

- **button1_Click Event:**
  - Sets the background color for the entire current line using the dynamically registered format.

- **Form1_Load Event:**
  - Initializes the combo box with HatchStyle options.
  - Sets default values and configurations for the combo box and edit control.

- **button2_Click Event:**
  - Applies the registered background format to the selected text within the edit control.

## API Reference

### Namespaces and Classes
- **System.Drawing**: Provides the `Color` class for background and foreground colors.
- **System.Windows.Forms**: Includes the `ComboBox` and `RadioButton` controls.
- **Syncfusion.Windows.Forms.Edit**: Contains the `EditControl` class for advanced text editing functionalities.

### Properties and Methods
- **ComboBox.SelectedItem**: Gets or sets the currently selected item in the combo box.
- **RadioButton.Checked**: Gets a value indicating whether the radio button is checked.
- **EditControl.CurrentLine**: Gets or sets the number of the current line within the edit control.
- **EditControl.RegisterBackgroundColorFormat**: Registers a new background color format for use in the edit control.
- **EditControl.SetLineBackColor**: Applies the specified background color to the entire line.

## Code Examples

The examples demonstrate the integration of various UI controls and the application of background color formats within an edit control. These examples show how to dynamically apply styles based on user input and predefined settings.

```vb
' Example: Setting Background Color for Selected Text
Private Sub button2_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles button2.Click
    Dim format As IBackgroundFormat = RegisterFormat()
    editControl1.SetSelectionBackColor(editControl1.SelectionStart, editControl1.SelectionLength, True, format)
End Sub
```

## Cross References
- Refer to the Syncfusion documentation for more details on `EditControl` properties and methods.
- See also the `HatchStyle` enumeration documentation for available styles.

<!-- tags: [editcontrol, hatchstyle, backgroundcolor, windowsforms, syncfusion] keywords: [edit, text, line, background, color, style, format] -->
```