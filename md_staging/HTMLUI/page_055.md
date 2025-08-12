```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_055.jpeg
document_name: HTMLUI
page_number: 055
page_id: HTMLUI#page_055
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:05:42Z
fidelity: lossless
-->

### Overview
- Demonstrates how to handle the `MouseLeave` event in an HTML control.
- Explains converting `EventArgs` to `BubblingEventArgs` for event handling in Windows Forms.

## Content

### Handling MouseLeave Event in C#
```csharp
[C#]

private void htmluiControl1_LoadFinished(object sender, System.EventArgs e)
{
    IHTMLElement[] htmlElement = this.htmluiControl1.Document.GetElementsByName("body");
    htmlElement[0].MouseLeave += new EventHandler(body_MouseLeave);
}

// Event occurs when the mouse pointer leaves the control.
private void body_MouseLeave(object sender, EventArgs e)
{
    // Converts the EventArgs object to BubblingEventArgs type if possible.
    BubblingEventArgs bargs = HTMLUIControl.GetBubblingEventArgs(e);

    // Returns the first sender of the event.
    BaseElement elem = bargs.RootSender as BaseElement;

    if (elem != null && elem is INPUTElementImpl)
    {
        if (elem.ID == "button1")
        {
            this.label1.Text = "Mouse just left Button 1";
        }
        else if (elem.ID == "button2")
        {
            this.label1.Text = "Mouse just left Button 2";
        }
    }
}
```

### Handling MouseLeave Event in VB.NET
```vb
[VB.NET]

' Event occurs when the mouse pointer leaves the control.
Private Sub htmluiControl1_LoadFinished(ByVal sender As Object, ByVal e As System.EventArgs)
    Dim htmlElement() As IHTMLElement = Me.htmluiControl1.Document.GetElementsByName("body")
    AddHandler htmlElement(0).MouseLeave, AddressOf body_MouseLeave
End Sub

Private Sub body_MouseLeave(ByVal sender As Object, ByVal e As EventArgs)

    ' Converts the EventArgs object to BubblingEventArgs type if possible.
    Dim bargs As BubblingEventArgs = HTMLUIControl.GetBubblingEventArgs(e)

    ' Returns the first sender of the event.
    Dim elem As BaseElement = CType(IIf(TypeOf bargs.RootSender Is BaseElement, bargs.RootSender, Nothing), BaseElement)
End Sub
```

## API Reference

### Methods
- `GetElementsByName(String name)`: Retrieves elements by their name.
- `GetBubblingEventArgs(EventArgs e)`: Converts `EventArgs` to `BubblingEventArgs`.

### Classes
- `BubblingEventArgs`: Represents bubbling event arguments.
- `BaseElement`: Represents a base class for HTML elements.

### Constants
- `INPUTElementImpl`: Represents input element implementations.

## Code Examples

The examples provided show how to:
1. Attach a `MouseLeave` event to an HTML element.
2. Handle `MouseLeave` events by converting `EventArgs` to `BubblingEventArgs`.
3. Identify the source of the `MouseLeave` event (e.g., specific buttons).

## Cross References
- For more details on event bubbling and handling, see the "JavaScript Event Handling" section.
- For additional information on HTML UI controls, refer to the "HTMLUI Control Overview" in the documentation.

<!-- tags: [syncfusion-sdk, winforms, htmlui, event-handling, mouseleave] keywords: [event handling, html element, bubbling event arguments, mouseleave, windows forms] -->
```