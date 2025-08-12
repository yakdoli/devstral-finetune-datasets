```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en 
source_filename: page_030.jpeg
document_name: HTMLUI
page_number: 030
page_id: HTMLUI#page_030
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:04:50Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## 4 Concepts And Features

The HTMLUIClientControl is the main control of the HTMLUI library. The control exposes several properties, methods, and events to load, display, and interact with rich HTML-based user interfaces.

### Creating the HTMLUI Control

The HTMLUI control can be created by dragging it from the Visual Studio .NET toolbox, just like any other Windows Forms control.

The following code snippet illustrates how to create a HTMLUIClientControl programmatically.

```csharp
// Initialize a HTMLUIClientControl.
this.htmluicontrol1 = new Syncfusion.Windows.Forms.HTMLUI.HTMLUIClientControl();
```

### Important Properties

The following properties help you get started with the HTMLUIClientControl.

| Property        | Description                                                                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StartupDocument | This is the path to the HTML document that will be loaded when the HTMLUIClientControl is called. Using this property to set a document is the simplest means to load an HTML document.                     |
| Text            | The HTMLUIClientControl does not display the Text property as text. This is the HTML that will be rendered as in the HTMLUIClientControl. This is the equivalent of the View Source option in a traditional web browser. |
| Document        | This property provides access to all the display HTML elements programmatically.                                                                                                                          |

### Important Methods

The following methods help you to get started with the HTMLUIClientControl.

| Method   | Description                                                                                                                                                                                                           |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LoadHTML | This method is used to load the HTML document.                                                                                                                                                                      |
| LoadCSS  | This method is used to load CSS styles from file and refresh current                                                                                                                                               |

<!-- tags: [product, syncfusion, winforms, HTMLUIClientControl, windows forms, library, properties, methods, events, HTML-based user interfaces, startupdocument, text property, document property, loadhtml, loadcss] keywords: [HTMLUIClientControl, Visual Studio, .NET, Windows Forms, HTML document, document loading, text rendering, View Source, CSS styles, programmatic access] -->
```