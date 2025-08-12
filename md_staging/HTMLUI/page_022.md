```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_022.jpeg
document_name: HTMLUI
page_number: 022
page_id: HTMLUI#page_022
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:04:14Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

The HTMLUI control displays a title bar at the top of the control. Set the title for this HTMLUI control to be "HTMLUI Tutorial".

## Content

### Setting Up Properties

Figure 8: Viewing Properties

The screenshot in Figure 8 shows the property grid for the HTMLUI control. Here's a brief summary of the important properties:

- **Title**: The title for the HTMLUI control has been set to "HTMLUI Tutorial".
- **Text**: This property is used to display or modify the content of the control based on the HTML document loaded into it.
- **Size**: The dimensions of the control are set to 552x353 pixels.

### Adding a New HTML Document

3. Add a new HTML document to the Windows Forms project. Edit the HTML document to define the user interface. In this case, you will have an HTML table with 3 rows and 1 column.

#### Sample HTML Content

```html
<html>
<head>
    <title>Creating User Interface</title>
</head>
<body bgcolor="#ffffff">
    <table id="Table1" height="360" cellspacing="1" cellpadding="1" width="392" border="1">
        <tr>
            <!-- More rows to be added here -->
        </tr>
    </table>
</body>
</html>
```

## API Reference

### Properties

- **Title**: Gets or sets the document title displayed in the control's title bar.
- **Text**: Gets or sets the content displayed in the HTMLUI control.
- **Size**: Gets or sets the dimensions of the HTMLUI control in pixels.

## Code Examples

Here is a sample code snippet demonstrating how to set up the HTMLUI control in a Windows Forms project:

```csharp
using Syncfusion.Windows.Forms.HTMLUI;

// Initialize the HTMLUI control
HTMLUI htmlControl = new HTMLUI();
htmlControl.Dock = DockStyle.Fill;

// Set the title for the control
htmlControl.Title = "HTMLUI Tutorial";

// Define the HTML content to display (e.g., in an HTML file)
string htmlContent = @"<html>
<head>
    <title>Creating User Interface</title>
</head>
<body bgcolor=""#ffffff"">
    <table id=""Table1"" height=""360"" cellspacing=""1"" cellpadding=""1"" width=""392"" border=""1"">
        <tr>
            <!-- More rows to be added here -->
        </tr>
    </table>
</body>
</html>";

htmlControl.Text = htmlContent;

// Add the control to the form
this.Controls.Add(htmlControl);
```

## Cross References

See also:
- **HTMLUI Control Overview**
- **Embedding HTML in Windows Forms**

### Note

For more detailed information on managing the HTML content and customizing the HTMLUI control, refer to the Syncfusion documentation on HTMLUI.

<!-- tags: HTMLUI, Windows Forms, Syncfusion, properties, title, text, size, HTML document, user interface, table, version: 11.4.0.26 -->
```