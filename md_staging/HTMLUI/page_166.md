```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_166.jpeg
document_name: HTMLUI
page_number: 166
page_id: HTMLUI#page_166
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:13:06Z
fidelity: lossless
-->

## Overview
- Explains how to handle interactivity using HTMLUI in a Windows Forms application.
- Demonstrates binding the InnerHTML property of a div element to a button click event.
- Highlights the ease of use and designer integration of HTMLUI in creating rich interfaces with minimal coding.

## Content

### Handling InnerHTML Changes

The following code snippet demonstrates how to handle changes to the `InnerHTML` property of a `div` element within a Windows Forms application.

#### Code Example
```vb
AddHandler div.InnerHTMLChanged, AddressOf div_InnerHTMLChanged
End Sub

Private Sub button_Click(ByVal sender As Object, ByVal e As EventArgs)
    ' Gets or sets text, the inner part of the element. Inner part includes
    ' children of the current element.
    Me.div.InnerHTML = "HTMLUI is very easy to use with complete designer" &
                       ControlChars.CrLf & _
                       "integration. The control is very powerful and rich interfaces can be created" &
                       ControlChars.CrLf & _
                       "with " & ControlChars.CrLf & "minimal coding."
End Sub

Private Sub div_InnerHTMLChanged(ByVal sender As Object, ByVal e As ValueChangedEventArgs)
    ' Returns the HTML text including inner and current element text; also current
    ' element is added in to
    ' the output
    Me.div.Children.Parent.Parent.InnerHTML = Me.div.OuterHTML & "<p/><img src='HTMLUI.gif'/>"
End Sub
```

#### Explanation
1. **Event Binding**: The `InnerHTMLChanged` event of the `div` element is bound to the `div_InnerHTMLChanged` event handler using `AddHandler`.
2. **Button Click Event**: When the button is clicked, the `InnerHTML` property of the `div` is updated with a message. This message includes text formatted for demonstration purposes, showing how HTML content can be dynamically updated.
3. **InnerHTML Changed Event**: When the `InnerHTML` of the `div` changes, the `div_InnerHTMLChanged` event is triggered. This event updates the parent element of the `div` by appending an additional image tag (`<img src='HTMLUI.gif'/>`) to the existing `InnerHTML`.

### Workflow Description
- **Button Click**: The text inside the `div` element is dynamically updated when the button is clicked.
- **InnerHTML Change**: When the text inside the `div` is modified, an image element is appended to the `div` to demonstrate interactivity and dynamic content updates.

This example showcases how HTMLUI can be used to create interactive and visually rich interfaces with minimal coding effort, leveraging the designer integration and powerful features of HTMLUI in Windows Forms.

## API Reference

### Namespace: Syncfusion.Windows.Forms.HTMLUI

#### Members
- `InnerHTML`: Gets or sets the inner HTML content of the element.
- `OuterHTML`: Returns the complete HTML string including the node itself and its children.
- `InnerHtmlChanged`: Event triggered when the `InnerHTML` property of the element changes.

#### Remarks
- The `InnerHTML` property controls the content within the element, including any child elements.
- The `OuterHTML` property returns the complete HTML string, including the element's start and end tags.
- The `InnerHtmlChanged` event is useful for detecting changes in the element's content.

## Code Examples

### Dynamically Updating the Content
In this example, clicking a button updates the `InnerHTML` of a `div` element, and an image tag is appended dynamically when the content changes.

#### VB.NET
```vb
Public Class Form1
    Private Sub button_Click(ByVal sender As Object, ByVal e As EventArgs)
        Me.div.InnerHTML = "Updated content. <br/> This is a new line." &
                           ControlChars.CrLf & _
                           "Image will be appended on changes."
    End Sub

    Private Sub div_InnerHTMLChanged(ByVal sender As Object, ByVal e As ValueChangedEventArgs)
        Me.div.Children.Parent.Parent.InnerHTML &= "<p/><img src='updated.gif'/>"
    End Sub
End Class
```

### JSON
In a larger context, the `InnerHTML` might be dynamically replaced or updated based on JSON data or other external sources, providing a responsive and interactive user interface.

```json
{
    "Message": "Updated content with dynamic content.",
    "ImageSrc": "updated.gif"
}
```

#### Explanation
- The `innerHTML` property is updated with new content and a line break for formatting.
- When the content changes, an additional image tag is appended to the `div` element, demonstrating dynamic content updates.

<!-- tags: [syncfusion, windowsforms, htmlui, innerhtml, eventhandler, integration, designer, minimalcoding] keywords: [htmlui, innerhtml, outerhtml, interactivity, windowsforms, designertime, runtime, contentupdates, eventbinding] -->
```