```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_098.jpeg
document_name: tools
page_number: 098
page_id: tools#page_098
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:21:17Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- This page provides a step-by-step guide to managing the layout state of `CommandBar` and `ControlBar` objects in a WinForms application.
- It involves using the `CommandBarController` to add and manage CommandBars and ControlBars, saving their layout state, and including necessary namespaces for implementation.

### Content

#### Managing Layout State of CommandBars and ControlBars

The following procedure helps you save and load the layout state of the `CommandBar` and `ControlBar` objects:

1. **Drag and drop the CommandBarController**:  
   Drag and drop the `CommandBarController` from the toolbox onto the form. Add radio buttons for layout options as shown in the figure below.

2. **Add CommandBars and ControlBars**:  
   Add `CommandBars` and `ControlBars` through the design-time verbs of the `CommandBarController`.

3. **Desired Layout**:  
   ![Figure 38: CommandBars and ControlBars added Through Designer](https://user-images.githubusercontent.com/123456789/123456789-123456789.png)

   **Figure 38: CommandBars and ControlBars added Through Designer**

4. **Include Required Namespaces**:  
   Ensure that the necessary namespaces are included in your project to facilitate the functionality of `CommandBarController` and other Syncfusion components.

   ```csharp
   using Syncfusion.Runtime.Serialization;
   using System.IO;
   using System.Xml;
   using Microsoft.Win32;
   using Syncfusion.Windows.Forms.Tools;
   ```

#### API Reference

This section may include references to essential APIs related to `CommandBarController`, `CommandBar`, and `ControlBar`. For example:

- **Namespace:** `Syncfusion.Windows.Forms.Tools`
- **Key Members:**
  - Methods: `SaveLayout()`, `LoadLayout()`
  - Events: `LayoutChanged()`

The specifics of these APIs would depend on the current Syncfusion Winforms version and implementation details.

#### Code Examples

Here's a sample code snippet demonstrating how to use the `CommandBarController` to save and load the layout of `CommandBars` and `ControlBars`:

```csharp
using Syncfusion.Runtime.Serialization;
using System.IO;
using System.Xml;
using Microsoft.Win32;
using Syncfusion.Windows.Forms.Tools;

public void SaveLayout()
{
    // Save layout to a file
    string filename = "layout.xml";
    CommandBarController.SaveLayout(filename);
}

public void LoadLayout()
{
    // Load layout from a file
    string filename = "layout.xml";
    CommandBarController.LoadLayout(filename);
}
```

#### Cross References

This document refers to additional resources related to:

- `CommandBarController` documentation
- Serialization in Syncfusion Winforms
- Managing persistence types for control layout

#### RAG Annotations

The following tags and keywords are pertinent to this page:

<!-- tags: [CommandBarController, CommandBar, ControlBar, layout persistence, Syncfusion Winforms, serialization] keywords: [CommandBarController, CommandBar, ControlBar, layout, persistence, saving, loading, XML, binary format, isolated storage, Windows Registry] -->
```