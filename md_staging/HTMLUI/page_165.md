```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_165.jpeg
document_name: HTMLUI
page_number: 165
page_id: HTMLUI#page_165
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:12:38Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- This page demonstrates how to use the HTMLUI control in Windows Forms to create rich interfaces with minimal coding.
- Demonstrates handling events such as button clicks and changes in the `InnerHTML` property.
- Shows examples in both C# and VB.NET.

## Content

###HTML C# Example

```csharp
{
    Hashtable html = this.htmluiControl1.Document.GetElementsByUserIdHash();
    this.button = html["btn"] as INPUTElementImpl;
    this.div = html["div"] as DIVElementImpl;
    this.button.Click += new EventHandler(button_Click);

    // Event raised when InnerHtml property changed
    this.div.InnerHTMLChanged += new
    ValueChangedEventHandler(div_InnerHTMLChanged);
}

private void button_Click(object sender, EventArgs e)
{
    // Gets or sets text, the inner part of the element. Inner part includes
    // children of the current element.
    this.div.InnerHTML = "HTMLUI is very easy to use with complete designer
    integration. The control is very powerful and rich interfaces can be created
    with minimal coding.";
}

private void div_InnerHTMLChanged(object sender, ValueChangedEventArgs e)
{
    // Returns the HTML text including inner and current element text; also
    // current element is added in to
    // the output.
    this.div.Children.Parent.Parent.InnerHTML = this.div.OuterHTML + "<p/><img
    src='HTMLUI.gif'/>";
}
```

###HTML VB.NET Example

```vb
' Class that is responsible for <input> tag
Private button As INPUTElementImpl

' Class that is responsible for <div> tag
Private div As DIVElementImpl

Private Sub htmluiControl_LoadFinished(ByVal sender As Object, ByVal e As
System.EventArgs)

    Dim html As Hashtable = Me.htmluiControl.Document.GetElementsByUserIdHash()
    Me.button = CType(IIf(TypeOf html("btn") Is INPUTElementImpl, html("btn"),
    Nothing), INPUTElementImpl)
    Me.div = CType(IIf(TypeOf html("div") Is DIVElementImpl, html("div"),
    Nothing), DIVElementImpl)
    AddHandler button.Click, AddressOf button_Click

    '// Event raised when InnerHtml property changed
```

## API Reference

### Methods/Events
- **Click**: Event raised when the button is clicked.
- **InnerHTMLChanged**: Event raised when the inner HTML of an element changes.

### Elements
- **INPUTElementImpl**: Represents an `<input>` element.
- **DIVElementImpl**: Represents a `<div>` element.

### Properties
- **InnerHTML**: Gets or sets the inner HTML of an element.
- **OuterHTML**: Returns the HTML text including inner and current element text.

## Code Examples

### C# Example

```csharp
// Example of handling button click to change the content of a <div>
this.button.Click += (sender, e) =>
{
    this.div.InnerHTML = "Dynamic content loaded via HTMLUI.";
};
```

### VB.NET Example

```vb
' Example of handling button click to change the content of a <div>
AddHandler button.Click, Sub(sender, e)
                          this.div.InnerHTML = "Dynamic content loaded via HTMLUI."
                          End Sub
```

## Cross References
- Refer to the main documentation of HTMLUI for further details on using advanced features and properties.

<!-- tags: [WinForms, HTMLUI, Control, Event Handling, C# VB.NET] keywords: [innerhtml, outerhtml, element, input, div, event, click] -->
``` 
