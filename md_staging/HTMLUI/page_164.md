```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_164.jpeg
document_name: HTMLUI
page_number: 164
page_id: HTMLUI#page_164
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:12:49Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```csharp
    End If
    End Sub

Private Sub htmluiControl1_DragDrop(ByVal sender As Object, ByVal e As System.Windows.Forms.DragEventArgs)
    'Specifying the drop format and collecting the file name
    Dim files As String() = CType(e.Data.GetData("FileDrop", False), String())
    For Each fileName As String In files
        'Loading the specified file in to the HTMLUI control
        Me.htmluiControl1.LoadHTML(fileName)
    Next fileName
End Sub
```

## 5.10 How To Enable User Interaction With the HTML Elements

The HTMLUI control supports a rich set of interactivity with the elements displayed. The HTML elements in the HTML document are accessed with the object variables of the respective classes. HTMLUI control gives a free hand to the user in deciding each and every factor of the element's display. Some include selecting the position of the control, attaching the attributes at run time, attaching events with the element, changing the text inside it at run time, and so on.

The following snippet shows how the elements interact with each other on the execution of their respective events.

### HTML Code

```html
<html>
<head>
    <title>HTMLUI Element Interactivity</title>
</head>
<body bgcolor="#D8E2F2">
    <p><input type="button" id="btn" value="HTMLButton"/></p>
    <p><div id="div">HTMLUI supports a wide variety of HTML tags that can be used to display very rich HTML documents.</div></p>
</body>
</html>
```

### C# Code

```csharp
// Class that is responsible for <input> tag
INPUTElementImpl button;

// Class that is responsible for <div> tag
DIVElementImpl div;

private void htmluiControl1_LoadFinished(object sender, System.EventArgs e) {}
```

## Content
- The HTMLUI control is a powerful tool for enhancing user interaction within Windows Forms applications.
- Elements within the HTML document are directly accessible and modifiable using object variables associated with each HTML element.
- Users have comprehensive control over the display and functionality of HTML elements, including but not limited to:
  - Manipulating the control's position dynamically.
  - Adding attributes to elements at runtime.
  - Attaching event handlers to trigger actions.
  - Updating the content of elements in response to user actions.

## API Reference
The provided code snippet demonstrates the usage of `INPUTElementImpl` and `DIVElementImpl` to interact with `<input>` and `<div>` HTML tags within the `htmluiControl1` control. The `LoadFinished` event is used to interact with these elements once the HTML content has been fully loaded.

## Code Examples

### HTML Example
```html
<html>
<head>
    <title>HTMLUI Element Interactivity</title>
</head>
<body bgcolor="#D8E2F2">
    <p><input type="button" id="btn" value="HTMLButton"/></p>
    <p><div id="div">This HTML content can be interacted with using the control.</div></p>
</body>
</html>
```

### C# Example
```csharp
// Example of attaching an event to an <input> button
INPUTElementImpl button = htmluiControl1.Document.GetElementById("btn") as INPUTElementImpl;
button.Click += (sender, e) => {
    MessageBox.Show("HTML Button Clicked!");
};

// Example of modifying text within a <div>
DIVElementImpl div = htmluiControl1.Document.GetElementById("div") as DIVElementImpl;
div.NodeValue = "Text updated dynamically!";
```

### Notes
- The `htmluiControl1` must have the HTML content loaded before accessing or modifying its elements.
- Ensure that the necessary namespaces and references are included to utilize `INPUTElementImpl` and `DIVElementImpl`.
- Always verify that the elements exist before attempting to access or modify them to avoid exceptions.

## Cross References
For more information on how to use HTML elements within the HTMLUI control, refer to the [HTMLUI documentation](#). Additional examples and best practices are available in the [Syncfusion WinForms User Guide](#).

<!-- tags: [syncfusion, winforms, htmlui, user interaction, event handling, control manipulation] keywords: [htmlui control, windows forms, html elements, dynamic content, events, attributes, runtime changes] -->
```