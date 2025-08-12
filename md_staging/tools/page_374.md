```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_374.jpeg
document_name: tools
page_number: 374
page_id: tools#page_374
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:09:50Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Figure 182: TaskWindow of ButtonEdit Control

### Overview

The ButtonEdit control provides various options to customize its appearance and behavior. Below are the options and events discussed.

### The Options

- **Show TextBox** - Shows or hides embedded textbox.
- **Text Alignment** - Sets alignment of the text.
- **Button Styles** - Sets the button styles.
- **UseVisualStyle** - Enables or disables visual style for the control.
- **Character Casing** - Sets the case settings for the text in the textbox.
- **ButtonCollection** - Opens Button Collection Editor.
- **Name** - Sets the name of the ButtonEdit control.

### ButtonEdit Events

The below events are discussed in the event section.

#### ButtonClicked Event

This event is handled whenever a child button of a ButtonEdit control is clicked. It gives `ClickedButton` member which lets you customize the button that is clicked.

The below code changes the alignment of the button that is clicked at runtime.

#### Code Example in C#

```csharp
this.buttonEdit2.ButtonClicked += new
ButtonClickedEventHandler(buttonEdit2_ButtonClicked);
private void buttonEdit2_ButtonClicked(object sender, ButtonClickedEventArgs e)
{
    //Changing the button alignment of the clicked button
    e.ClickedButton.ButtonAlign = ButtonAlignment.Left;
}
```

#### Code Example in VB.NET

```vb.net
AddHandler Me.buttonEdit2.ButtonClicked, AddressOf
buttonEdit2_ButtonClicked
Private Sub buttonEdit2_ButtonClicked(ByVal sender As Object, ByVal e As ButtonClickedEventArgs)
    'Changing the button alignment of the clicked button
End Sub
```

## API Reference

### Events

- **ButtonClicked** - Event fired when a child button is clicked.

### Parameters

- **sender** - The object that triggered the event.
- **e** - The `ButtonClickedEventArgs` containing the event data.

### Event Handling

- **Changing Button Alignment** - Demonstrates how to dynamically change the alignment of the clicked button.

## Code Examples

### C# Code Example

```csharp
this.buttonEdit2.ButtonClicked += new
ButtonClickedEventHandler(buttonEdit2_ButtonClicked);
private void buttonEdit2_ButtonClicked(object sender, ButtonClickedEventArgs e)
{
    e.ClickedButton.ButtonAlign = ButtonAlignment.Left;
}
```

### VB.NET Code Example

```vb.net
AddHandler Me.buttonEdit2.ButtonClicked, AddressOf
buttonEdit2_ButtonClicked
Private Sub buttonEdit2_ButtonClicked(ByVal sender As Object, ByVal e As ButtonClickedEventArgs)
    e.ClickedButton.ButtonAlign = ButtonAlignment.Left
End Sub
```
```