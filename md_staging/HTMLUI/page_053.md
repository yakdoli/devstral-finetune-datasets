```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_053.jpeg
document_name: HTMLUI
page_number: 053
page_id: HTMLUI#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:05:47Z
fidelity: lossless
--> 

# Essential HTMLUI for Windows Forms

## Scope
- Demonstrates how to handle HTML events in a Windows Forms application.
- Highlights the integration of HTML elements within Windows Forms.
- Provides a sample location and introduces element events like Click, DoubleClick, MouseMove, and KeyPress.

### Introduction
By default, this sample can be found under the following location:

`C:\Documents and Settings\username\My Documents\Syncfusion\EssentialStudio\Version Number\Windows\HTMLUI.Windows\Samples\2.0\HTMLUI Events\HTMLUIControlEvents`

## 4.4 Element Events

### Overview
Each HTML element in an HTML document is made to support events, such as Click, DoubleClick, MouseMove, KeyPress, and so on, just like the Windows forms controls.

#### HTML Structure
```html
[HTML]

<html>
<body>
    <input type="text" id="text1"/>
</body>
</html>
```

#### C# Code Implementation
```csharp
[C#]

// Object declaration for the textarea element in the html document rendered in the control.
private void htmluiControl1_LoadFinished(object sender, System.EventArgs e)
{
    Hashtable htmlElements = this.htmluiControl1.Document.GetElementsByIdHash();
    BaseElement textElement = htmlElements["text1"] as BaseElement;

    // Event handlers declaration for the events on the html elements.
    textElement.Click += new EventHandler(textElement_Click);
    textElement.KeyDown += new EventHandler(textElement_KeyDown);
    textElement.MouseEnter += new EventHandler(textElement_MouseEnter);
}

// HTML element Click event definition.
private void textElement_Click(object sender, EventArgs e)
{
    Console.WriteLine("Click Event Handled");
}

// HTML element KeyDown event definition.
private void textElement_KeyDown(object sender, EventArgs e)
{
    Console.WriteLine("KeyDown Event Handled");
}
```

## API Reference
- `HtmlUIControl.Document.GetElementsByIdHash()`: Retrieves all elements by their ID hash.
- `BaseElement`: Represents the base for all HTML elements.
- `EventHandler`: Represents the method that will handle the events.

## Code Examples
The code examples provided show how to:
1. Access HTML elements by their ID within a Windows Forms environment.
2. Attach event handlers (Click, KeyDown, MouseEnter) to the HTML elements.
3. Handle the events with custom actions, such as logging messages.

## Conclusion
This section demonstrates the integration of HTML event handling into Windows Forms applications using Syncfusion HTMLUI components. It provides a practical example of linking HTML elements to event-driven behavior similar to native Windows Forms controls.

<!-- tags: [Syncfusion, Winforms, HTMLUI, Events, Windows Forms] keywords: [HTMLUI, Windows Forms, Element Events, HTML Elements, Click, DoubleClick, MouseMove, KeyPress, EventHandler] -->
```