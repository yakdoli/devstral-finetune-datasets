```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_116.jpeg
document_name: HTMLUI
page_number: 116
page_id: HTMLUI#page_116
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:09:40Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```html
<html>
<head>
    <link rel=Stylesheet type="text/css"
          href="C:\MyProjects\StyleSheets\styleSheet.css" />
</head>
<body>
<p>Green color for paragraph.</p>
<div>Blue color for division</div>
</body>
</html>
```

## Applying Styles to the HTML Document

The HTMLUI control uses two modes of applying styles to the HTML document with the help of the external style sheets.

### Design Time

This type of setting is carried out in the document at design time. It is used in circumstances where only a standard style is applied for the documents.

- **C#**:
```csharp
htmluiControl.LoadHTML(@"C:\MyProjects\StyleSheets\external.html");
```

- **VB.NET**:
```vb
htmluiControl.LoadHTML(@"C:\MyProjects\StyleSheets\external.html")
```

### Run Time

HTMLUI is so flexible that the user can define styles for the HTML document at run time. The `LoadCSS` method of the HTMLUI control helps the user to load another CSS file to the current document at run time.

- **C#**:
```csharp
htmluiControl.LoadHTML(@"C:\MyProjects\StyleSheets\external.html");
htmluiControl.LoadCSS(@"C:\MyProjects\StyleSheets\NewStyleSheet.css");
```

- **VB.NET**:
```vb
htmluiControl.LoadHTML(@"C:\MyProjects\StyleSheets\external.html"
htmluiControl.LoadCSS(@"C:\MyProjects\StyleSheets\NewStyleSheet.css")
```

## API Reference

### Methods
- `LoadHTML(string filePath)`: Loads the HTML content from the specified file path.
- `LoadCSS(string filePath)`: Loads the CSS file from the specified file path.

## Code Examples

The examples above demonstrate how to apply external styles to an HTML document using both design-time and run-time configurations.

## Additional Notes

Ensure that the paths to external CSS files are correctly specified to apply the desired styles to the HTML content loaded in the HTMLUI control.

---

<!-- tags: [HTMLUI, Windows Forms, External Style Sheets, Design Time, Run Time] keywords: [HTMLUI, Windows Forms, Style Sheets, Design, Run Time, C#, VB.NET] -->
```