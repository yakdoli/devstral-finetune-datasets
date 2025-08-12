<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_023.jpeg
document_name: HTMLUI
page_number: 023
page_id: HTMLUI#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:03:50Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- An HTML document containing a textbox, textarea, and button control is provided.
- The objective is to create a user interface with a button click event to display text in the controls.
- Handle the LoadFinished event for the HTML Control to access HTML elements.

## Content

### HTML Document

```html
<TD align="center" height="72" valign="middle">
<INPUT id="txt" type="text" size="40" name="Text1"></INPUT>
</TD>
</TR>

<TR>
<TD align="center" height="209" valign="middle">
<TEXTAREA id="txtArea" name="TextArea" rows="9" cols="35"></TEXTAREA>
</TD>
</TR>

<TR>
<TD align="center" valign="middle">
<INPUT id="btn" type="button" size="" value="Button" name="Button1"></INPUT>
</TD>
</TR>

</TABLE>
</BODY>
</HTML>
```

### Instructions

#### 4. Adding Click Event to Button
- As shown in the HTML document, a **textbox**, a **textarea**, and a **button control** have been added.
- The objective is to create a user interface by adding a **Click** event to the button element.
- On clicking the button, the text controls are made to display some text.

#### 5. Handling LoadFinished Event
- The **LoadFinished** event is executed when the HTML document is loaded in the HTMLUI control.
- Add a handler for the LoadFinished event of the HTMLUI control.
- Access the HTML elements inside the managed code using objects created for each element as defined in the HTMLUI namespace.

### C# Code Example

```csharp
// Objects declaration made global
INPUTElementImpl text;
INPUTElementImpl button;
TEXTAREAElementImpl textarea;

// HTMLUI control LoadFinishedEvent handler declaration
this.htmluiControl.LoadFinished += new System.EventHandler(this.htmluiControl_LoadFinished);

// HTMLUI control LoadFinishedEvent definition
private void htmluiControl_LoadFinished(object sender, System.EventArgs e)
{
    Hashtable html = this.htmluiControl.Document.GetElementsByUseridHash();

    this.text = html["txt"] as INPUTElementImpl;
}
```

## API Reference
- **Namespace**: HTMLUI
- **Control**: HTMLUI
- **Event**: LoadFinished

## Code Examples
- The provided C# code demonstrates how to handle the `LoadFinished` event for the HTMLUI control and access HTML elements using their unique IDs.

## Tags and Keywords
<!-- tags: [HTMLUI, WinForms, LoadFinished, Button, ClickEvent, ElementAccess] keywords: [textbox, textarea, button, LoadFinished, EventHandler, GetElementsByUseridHash] -->