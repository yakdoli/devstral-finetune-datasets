```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_008.jpeg
document_name: HTMLUI
page_number: 008
page_id: HTMLUI#page_008
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:02:53Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

* **Overview**
  - This page provides an introduction to using HTMLUI controls within Windows Forms applications.
  - Focuses on leveraging HTML and CSS capabilities in traditional desktop applications.
  - Covers basics and usage scenarios for HTMLUI components.

* **Content**
  - HTMLUI in Windows Forms enables developers to integrate HTML and CSS content into desktop applications.
  - Integration of modern web technologies enhances the user experience with visually appealing and dynamic interfaces.

* **Implementation**

    HTMLUI can be utilized to create rich, styled user interfaces in desktop applications. Here's a basic example to demonstrate this functionality:

    ```csharp
    // Loading and displaying HTML in a Windows Form
    string htmlContent = @"<html>
                            <body>
                                <h1>Hello, Windows Forms!</h1>
                                <p>This is an example using HTMLUI in Windows Forms.</p>
                                <style>
                                    h1 {
                                        color: #0071c5;
                                        font-family: 'Arial', sans-serif;
                                    }
                                    body {
                                        background-color: #f5f5f5;
                                        font-family: 'Georgia', serif;
                                    }
                                </style>
                            </body>
                          </html>";

    htmlUIControl1.LoadFromString(htmlContent);
    ```

    - The above code snippet demonstrates how to load and display HTML content directly within an HTMLUI control embedded in a Windows Forms application.

* **Customization**

    - **Styling**: Use CSS to style HTML content dynamically.
    - **Interactivity**: Leverage client-side scripting (e.g., JavaScript) for enhanced user interactions.
    - **Dynamic Updates**: Update the HTML content at runtime to reflect changes in your application.

* **Advantages**

    - Provides a bridge between desktop and web-based UI technologies.
    - Enables the use of modern web standards in desktop applications.
    - Facilitates richer and more customizable user interfaces.

* **Limitations**

    - Requires a proper understanding of HTML and CSS to take full advantage.
    - Deployment involves the inclusion of necessary web-related dependencies with the desktop application.

* **Compatibility**

    - Compatible with various versions of Windows Forms applications.
    - Works across different platforms with minor adjustments in setup.

## API Reference

- **Namespace**: Syncfusion.WinForms.HTMLUI
- **Class**: HTMLUIControl

### Fields
- `Document`: Represents the HTML document currently loaded in the control.

### Methods
- `LoadFromFile(string fileName)`  
  - **Description**: Loads an HTML file into the control.
  - **Parameters**:
    - `fileName` (string): Path of the HTML file to load.
  - **Returns**: void

- `LoadFromString(string htmlContent)`  
  - **Description**: Loads an HTML string into the control.
  - **Parameters**:
    - `htmlContent` (string): The HTML content to display.
  - **Returns**: void

### Events
- `LoadCompleted`: Triggered when the HTML content is fully loaded in the control.

## Code Examples

### Example 1: Loading an HTML File

```csharp
htmlUIControl1.LoadFromFile("path/to/html/file.html");
```

### Example 2: Displaying Dynamic HTML

```csharp
string htmlContent = @"<html>
                        <body>
                            <h1>Welcome to HTMLUI!</h1>
                            <p>TODAY'S DATE: " + DateTime.Now.ToString("MMMM dd, yyyy") + @"</p>
                            <style>
                                h1 {
                                    color: #2e7d32;
                                    font-family: 'Roboto', sans-serif;
                                }
                                p {
                                    background-color: #e0f7fa;
                                    font-family: 'Courier New', monospace;
                                }
                            </style>
                        </body>
                      </html>";

htmlUIControl1.LoadFromString(htmlContent);
```

### Example 3: Handling JavaScript Interactions

```csharp
// Injecting JavaScript functionality
string jsCode = @"
    document.body.onload = function() {
        alert('HTMLUI control is ready for interaction!');
    }
";
htmlUIControl1.InjectJavaScript(jsCode);
```

## Page-level Navigation/TOC

- **Introduction**
- **Implementation**
- **Customization**
- **Advantages**
- **Limitations**
- **Compatibility**

## Cross References

See also:
- [HTMLUI Samples for Windows Forms](#)
- [CSS Styling in WinForms](#)
- [JavaScript Integration](#)

<!-- tags: [product, module, control, api, version?] keywords: [htmlui, windows forms, html, css, desktop applications] -->
```