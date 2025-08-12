```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_015.jpeg
document_name: HTMLUI
page_number: 015
page_id: HTMLUI#page_015
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:03:19Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Explore the UI Edition Windows Forms Sample Browser and its features.
- Learn how to display HTML UI samples and browse through their features.

## Content

### UI Edition Windows Forms Sample Browser

- **Introduction:**
  Syncfusion Essential Tools provides a collection of UI components for rapid application development. These components support a variety of interfaces, including .NET-style docking, tabbed-MDI interfaces, customizable menus, and Office-like UIs such as task menus, Outlook-like group bars, and text editors.

#### Figure: User Interface Edition Windows Forms Sample Browser
![User Interface Edition Windows Forms Sample Browser](image_url_for_Figure_3)

- **Features:**
  - **Featured Samples:**
    - Ribbon ControlAdv
    - MDI Demo
    - VS 2008 Tab Splitter
    - Group Bar Demo
    - Editor Control
    - Office Style Custom Colors
    - VS 2008 Drag Provider

### Exploring HTMLUI

#### Step-by-Step Instructions

1. **Click HTML UI from the bottom-left pane.** HTML samples will be displayed.

#### Figure: HTMLUI Windows Samples
![HTMLUI Windows Samples](image_url_for_Figure_4)

- **Introduction:**
  Syncfusion HTMLUI is a .NET Windows Forms control that renders HyperText Markup Language (HTML). It can be used as a HTML viewer or a layout engine to display and customize rich application interfaces.

#### Featured Samples:
- **HTMLUI Chat** displays real-time text messages.
- **HTMLUI Dialog** shows a task completion interface.
- **Tic Tac Toe** demonstrates game functionality.

---

## API Reference

### Syncfusion Windows Forms HTMLUI

#### HTMLUI Properties
- **Appearance**: Configures the visual aspects of HTMLUI.
- **Layout**: Manages the layout of HTML elements.
- **Renderer**: Controls how HTML is rendered.
- **Data Binding**: Connects data sources to HTMLUI for dynamic content.

#### HTMLUI Events
- **Loading HTML**: Triggered when HTML content is being loaded.
- **User Interaction**: Captures user interactions with HTML elements.

### Supported Features
- **Custom Controls**: Extends HTMLUI with specialized controls.
- **Export HTML**: Exports HTML content for use in other applications.

---

## Code Examples

```csharp
using Syncfusion.Windows.Forms.HTMLUI;

HTMLUI htmlUI = new HTMLUI();
htmlUI.Dock = DockStyle.Fill;
this.Controls.Add(htmlUI);

// Load HTML content
htmlUI.Html = "<h1>Welcome to HTMLUI</h1>";
```

---

## Browser Through the Features

#### Step 4: Select any sample and browse through the features.
- Use the sample browser to explore various HTMLUI functionalities.

## Page-level Navigation/TOC

- **Figure 3: User Interface Edition Windows Forms Sample Browser**
- **Figure 4: HTMLUI Windows Samples**

## RAG Annotations
<!-- tags: [Syncfusion Windows Forms, HTMLUI, Windows Forms Sample Browser] keywords: [user interface, UI components, HTML viewer, layout engine, custom controls, data binding, events, export HTML, Syncfusion HTMLUI, figure browser, sample exploration] -->
```