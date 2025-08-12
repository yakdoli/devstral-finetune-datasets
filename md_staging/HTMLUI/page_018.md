```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_018.jpeg
document_name: HTMLUI
page_number: 018
page_id: HTMLUI#page_018
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:03:58Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Content

### 3.1 Lesson 1: Creating an HTML Display Application

The HTMLUI control can be used for displaying HTML documents with standard HTML / CSS formatting.

In this lesson, you will learn about the following:

#### 3.1.1 Displaying HTML By Using the HTMLUI Control

1. **Create a new Windows Forms application and open the main form for the application in the designer. Add the Syncfusion controls to your VS.NET toolbox if you haven't done so already. Drag an HTMLUI control onto the form.**
2. **HTML can be loaded into the HTMLUI control from the following sources:**
   - From a HTML file
   - From a URI (Uniform resource Identifier)
   - From a Stream
3. **Add a MainMenu component from the toolbox onto the form. Also add a OpenFileDialog component to the form and name it as "openDlg".**

---

![HTMLUI Control and Menu for Loading HTML Files](https://i.imgur.com/anonymous.png)

**Figure 5: HTMLUI Control and Menu for Loading HTML Files**

4. **Add a handler for the Open menu item by double-clicking on the menu.**

---

## API Reference

### Syncfusion.Windows.Forms.HtmlUI Namespace

- **HTMLUI Control:**
  - Properties:
    - `Html` (string): Sets or gets the HTML content to be displayed.
    - `Css` (string): Sets or gets the CSS content.
  - Methods:
    - `LoadFromFile(string filePath)`: Loads HTML content from a file.
    - `LoadFromUri(Uri uri)`: Loads HTML content from a URI.
    - `LoadFromStream(Stream stream)`: Loads HTML content from a stream.

## Code Examples

```csharp
using Syncfusion.Windows.Forms.HtmlUI;

public partial class MainForm : Form
{
    public MainForm()
    {
        InitializeComponent();
    }

    private void openMenuItem_Click(object sender, EventArgs e)
    {
        if (openDlg.ShowDialog() == DialogResult.OK)
        {
            htmlUI1.Html = File.ReadAllText(openDlg.FileName);
        }
    }
}
```

---

## See also

- [HTMLUI for WinForms Documentation](https://www.syncfusion.com/documentation/windows-forms/htmlui)
- Syncfusion WinForms Quick Start Guide
- Syncfusion HTMLUI Control API Reference

---

<!-- tags: [Syncfusion, Windows Forms, HTMLUI, control, HTML display, WinForms, tutorial] keywords: [HTMLUI, Windows Forms, HTML display, tutorial, Syncfusion, control, main form, HTML file, URI, stream, OpenFileDialog, menu, handler] -->
```