```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_024.jpeg
document_name: HTMLUI
page_number: 024
page_id: HTMLUI#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:03:54Z
fidelity: lossless
-->


## Essential HTMLUI for Windows Forms

```csharp
this.button = html["btn"] as INPUTElementImpl;
this.textArea = html["txtArea"] as TEXTAREAELEMENTImpl;

// Click Event declaration for HTML button element
this.button.Click += new EventHandler(button_Click);
}

private void button_Click(object sender, EventArgs e)
{
    // Click Event definition and Text control UserInterface
    this.text.UserControl.CustomControl.Text = "HTML provides extensive means to layout and customize display elements.";
    this.textArea.UserControl.CustomControl.Text = "The HTMLUI control adds the ability to create user interfaces using HTML from within Windows Forms applications using managed code.";
}
```

### Overview
- Demonstrates how to use HTMLUI controls within Windows Forms applications to enhance the user interface by leveraging HTML for layout and customization.
- The example shows how to handle button click events and dynamically update textual content on the form using HTML-based controls.

### Content

#### Step-by-Step Guide

1. **HTMLUI Setup**: 
   - The `INPUTElementImpl` and `TEXTAREAELEMENTImpl` are used to define button and text area controls, respectively.
   - These controls are part of the HTMLUI framework, allowing flexible layout and customization using HTML.

2. **Event Handling**:
   - A click event handler is attached to the button (`btn`). 
   - When the button is clicked, the `button_Click` method is executed.

3. **Updating User Interface Elements**:
   - The `button_Click` method updates the text in the text area controls (`CustomControl`) to reflect specific informational messages about HTMLUI's capabilities.

#### Example Output

Now, run the sample which displays the text on clicking the button as shown below.

![User Interface using HTMLUI](https://i.imgur.com/.undefined.jpg)
*Figure 9: User Interface using HTMLUI*

### API Reference

#### Known Members
- `INPUTElementImpl`: Represents an HTML input element used for interactive controls.
- `TEXTAREAELEMENTImpl`: Represents an HTML textarea element used for multi-line text input.
- `EventHandler`: A delegate type used to represent methods that handle events. It typically includes a sender object and event arguments.

### Code Examples

The provided code excerpt shows how to integrate HTMLUI controls into a Windows Forms application:

```csharp
// Attach HTMLUI controls to form elements
this.button = html["btn"] as INPUTElementImpl;
this.textArea = html["txtArea"] as TEXTAREAELEMENTImpl;

// Add a click event listener to the button
this.button.Click += new EventHandler(button_Click);
```

#### Click Event Handler
```csharp
private void button_Click(object sender, EventArgs e)
{
    // Update the text area controls
    this.text.UserControl.CustomControl.Text = "HTML provides extensive means to layout and customize display elements.";
    this.textArea.UserControl.CustomControl.Text = "The HTMLUI control adds the ability to create user interfaces using HTML from within Windows Forms applications using managed code.";
}
```

### Notes
- HTMLUI provides a powerful way to integrate HTML layouts and styling into Windows Forms applications, making it easier to create responsive and visually appealing UIs.
- This example demonstrates a simple use case where HTMLUI controls are dynamically updated based on user interaction.

<!-- tags: [Syncfusion, Windows Forms, HTMLUI, UI Development, C#] keywords: [HTMLUI, Windows Forms, User Interface, Event Handling, Button Click, Text Area, Managed Code, Integration] -->
```