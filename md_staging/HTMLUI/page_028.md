```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_028.jpeg
document_name: HTMLUI
page_number: 028
page_id: HTMLUI#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:04:13Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Implements HTML-based custom controls within Windows Forms.
- Loads a specified manifest resource (`customcontrol.s.htm`) from the assembly.
- Handles errors gracefully by displaying error messages in a dialog.

## Content

### Code Example: Loading HTML from an Assembly Resource
The following code demonstrates how to load an HTML file from an assembly's manifest resources and display it in a custom HTMLUI control.

```csharp
// Loads the specified manifest resource from the Assembly
htmlStream = (Stream) assembly.GetManifestResourceStream("HTMLUICustomControls.customcontrol.s.htm");
if (htmlStream != null)
{
    this.htmluiControl.LoadHTML(htmlStream);
    success = true;
}
catch (Exception ex)
{
    MessageBox.Show(ex.ToString());
}
return success;
```

### Custom Controls in HTMLUI
The image below illustrates the use of custom controls displayed within an HTMLUI interface. A calendar control is embedded within the HTML layout, showing the month of November 2004.

![](image.png)

**Caption:** Custom controls displayed inside HTML UI.

### Key Features
- **Embedding HTML:** Demonstrates embedding HTML content within a Windows Forms application.
- **Custom Controls Integration:** Highlights the integration of custom controls like calendars within the HTMLUI framework.
- **Error Handling:** Provides robust error handling to ensure smooth operation.

---

### Page-level Navigation/TOC (if applicable)
This section describes the key functionality of using HTMLUI in Windows Forms applications.

### Cross References
- Related topics on embedding HTML and working with custom controls can be found in the Syncfusion WinForms documentation.

## API Reference (if applicable)
- **Namespace:** HTMLUICustomControls
- **Class:** CustomControls
- **Methods:**
  - `LoadHTML(Stream stream)`: Loads HTML content from a stream into the HTMLUI control.
- **Events:**
  - `LoadCompleted`: Triggered when the HTML content has been successfully loaded.

## Code Examples (multi-language supported)
The provided code snippet loads an HTML file from an assembly's resources and displays it in an HTMLUI control. Error handling ensures that exceptions are presented to the user.

## RAG Annotations
<!-- tags: [syncfusion, winforms, htmlui, custom controls, html, calendar control] keywords: [HTMLUI, Windows Forms, customcontrols.s.htm, error handling, calendar, embedding html, resources, manifest] -->
```