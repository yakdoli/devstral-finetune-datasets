```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_152.jpeg
document_name: HTMLUI
page_number: 152
page_id: HTMLUI#page_152
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:11:56Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```csharp
child.Click += new EventHandler(child_Click);
}
}
}
}

private void child_Click(object sender, EventArgs e)
{
    BubblingEventArgs bargs = HTMLUIControl.GetBublingEventArgs(e);
    // Accessing the element that is sending the event
    BaseElement elem = bargs.RootSender as BaseElement;
    // Validating the element for execution
    if (elem.ID == "img1" && elem is IMGElementImpl)
    {
        if (elem.Attributes["src"].Value == "sync.jpg")
            elem.Attributes["src"].Value = "syncfusion.gif";
        else
            elem.Attributes["src"].Value = "sync.jpg";
            this.htmluiControl1.ScrollToElement(elem);
    }
}
}
```

## [VB.NET]

### Overview
- Adding event handlers to manage interactions with HTML elements in Syncfusion Winforms.
- Handling click events to modify the attributes of specific HTML elements dynamically.
- Implementing element validation and execution logic based on unique IDs and types.

## Content

### Event Handling in HTMLUI

The following code snippets demonstrate how to attach event handlers to HTML elements within an HTMLUI control in a Windows Forms application. These examples illustrate both the C# and VB.NET approaches.

#### C# Example

The C# code snippet demonstrates the process of attaching a click event handler to an HTML element and handling the event to alter the `src` attribute of an image.

#### VB.NET Example

```vb
Private Sub htmluiControl1_LoadFinished(ByVal sender As Object, ByVal e As System.EventArgs)
    ' Getting the body element in the HTML document
    Dim body As IHTMLElement() = _
        Me.htmluiControl1.Document.GetElementsByName("body")

    ' Collecting the children of the body element in a collection
    Dim elem As IHTMLElementsCollection = body(0).Children
    For Each child As IHTMLElement In elem

        ' Searching for the children containing the OnClick attribute
        If child.Attributes.Contains("OnClick") = True Then

            ' Click event declaration for current children
            AddHandler child.Click, AddressOf child_Click
        End If
    Next child
End Sub

Private Sub child_Click(ByVal sender As Object, ByVal e As EventArgs)
    Dim bargs As BubblingEventArgs = HTMLUIControl.GetBublingEventArgs(e)
    ' Accessing the element that is sending the event
    Dim elem As BaseElement = CType(IIf(TypeOf bargs.RootSender Is BaseElement, bargs.RootSender, Nothing), BaseElement)

    ' Validating the element for execution
    If elem.ID = "img1" AndAlso TypeOf elem Is IMGElementImpl Then
        ' ... Further logic to handle the element
    End If
```

## API Reference

- **HTMLUIControl**: Represents the HTMLUI control in the Windows Forms application.
- **BubblingEventArgs**: Houses parameters related to the bubbling event.
- **BaseElement**: Represents any element in the HTML document.
- **IMGElementImpl**: Represents an image element in the HTML document.

## Code Examples

The provided C# and VB.NET examples demonstrate the process of:

1. **Loading the HTMLUI Control**: The `LoadFinished` event is used to attach click event handlers to HTML elements.
2. **Attaching Event Handlers**: Using the `AddHandler` method to attach click events to elements containing the `OnClick` attribute.
3. **Event Handling Logic**: Implementing logic to dynamically modify attributes of specific HTML elements based on conditions.

## Cross References

See also:
- Additional details on HTMLUI controls and event handling in the Syncfusion Winforms documentation.
- Reference to specific APIs involved in element manipulation and validation.

<!-- tags: [Syncfusion Winforms, HTMLUI, Event Handling, C#, VB.NET] keywords: [HTMLUIControl, BubblingEventArgs, BaseElement, IMGElementImpl, LoadFinished, AddHandler, Click Event Handler] -->
```