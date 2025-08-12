```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_146.jpeg
document_name: tools
page_number: 146
page_id: tools#page_146
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:52:51Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The page covers methods to set Caption icons and labels for docked controls in Syncfusion Windows Forms.
- Demonstrates how to configure dock icons and labels programmatically.

## Content

### Caption Label with Dock Icon

**Figure 62: Caption Image set for the Docked Control**

![](https://syncfusion.com/DocsImage/DocImages/DocImages/tools/DockedControlCaption.png)

Methods for setting Caption icons and labels are as follows.

| Methods                   | Description                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------|
| **SetDockIcon**           | Sets the icon or the image for the docking window by passing the image icon as a parameter for this method. <br> `Ctrl` - Represents the dock enabled control. <br> `image` - Icon representing the docking window. |
| **SetDockIcon(Overloaded)** | This overloaded method returns the index of the image associated with the docking window. <br> `Ctrl` - Indicates the docking window. <br> `int` - A zero-based index into the ImageList property value. |
| **SetDockLabel**          | Sets the text to be displayed in the docking window caption. <br> `Ctrl` - Indicates the docking window. <br> `strText` - A string value representing the text caption. |

### API Reference

#### Methods

- **SetDockIcon**  
  - **Description**: Sets the icon or the image for the docking window.  
  - **Parameters**:  
    - `Ctrl`: Represents the dock enabled control.  
    - `image`: Icon representing the docking window.  

- **SetDockIcon(Overloaded)**  
  - **Description**: Returns the index of the image associated with the docking window.  
  - **Parameters**:  
    - `Ctrl`: Indicates the docking window.  
    - `int`: A zero-based index into the ImageList property value.  

- **SetDockLabel**  
  - **Description**: Sets the text to be displayed in the docking window caption.  
  - **Parameters**:  
    - `Ctrl`: Indicates the docking window.  
    - `strText`: A string value representing the text caption.  

## Code Examples

```csharp
// Example: Setting a dock icon
yourDockableWindow.SetDockIcon(yourImage);

// Example: Setting a dock label
yourDockableWindow.SetDockLabel("Your Caption Text");
```

### Cross References
- For more details on using docking controls, refer to the main docking control documentation.

<!-- tags: windows forms, docked controls, caption icons, caption labels, SetDockIcon, SetDockLabel, version 11.4.0.26 -->
```