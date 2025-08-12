```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_083.jpeg
document_name: HTMLUI
page_number: 083
page_id: HTMLUI#page_083
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:22Z
fidelity: lossless
-->

## Essential HTMLUI for Windows Forms

### Overview
- Demonstrates how to apply an external style sheet to modify the background color of a document.
- Explains the usage of the Ordered List (<ol>) tag to create numbered lists with different numbering schemes.
- Code examples detailing the HTML structure for applying external stylesheets and creating ordered lists with specific attributes.

### Content

#### HTML Structure and External Styles
```html
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="background.css"/>
  </head>
  <body>
    <p>The document receives its background color from the external style sheet.</p>
  </body>
</html>
```

##### Stylesheet
**File Location and Name:** `C:\MyProjects\link\background.css`

```css
body {
  background-color: #dae5f5;
}
```

#### Loading HTML in C# and VB.NET
```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\link\link.html");
```

```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\link\link.html")
```

#### Ordered List Tag

**4.6.18 OL - Ordered List Tag**

The **Ordered List** tag defines the start of an ordered list. The ordered list is numbered in the following scheme as '1', 'i', 'I', 'a', 'A' based on the requirements of the user. The ordered list contains the `<li>` items as its child elements. Each `<li>` element defines a list item. The type attribute is used to choose the required numbering style.

##### HTML Example
**File Location and Name:** `C:\MyProjects\listItem\ol.html`

```html
<html>
  <body>
    <ol type="i">
      <li>Essential Tools</li>
      <li>Essential Chart</li>
      <li>Essential HTMLUI</li>
    </ol>
  </body>
</html>
```

### API Reference

#### Methods

- `LoadHTML(string fileLocation)`
  - **Parameters:**
    - `fileLocation`: Specifies the path to the HTML file to be loaded.
  - **Description:** Loads an HTML file into the HTMLUI control.

### Code Examples

**C# Example:**
```csharp
this.htmluiControl.LoadHTML(@"C:\MyProjects\link\link.html");
```

**VB.NET Example:**
```vb
Me.htmluiControl.LoadHTML(@"C:\MyProjects\link\link.html")
```

### RAG Annotations
<!-- tags: [HTMLUI, Ordered List, External Stylesheet, LoadHTML, WinForms] keywords: [ordered list, numbered list, type attribute, styles sheet, background color, file location, C#, VB.NET, loadHTML] -->
```