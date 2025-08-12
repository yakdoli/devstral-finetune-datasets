```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_288.jpeg
document_name: tools
page_number: 288
page_id: tools#page_288
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:03:23Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses the AutoComplete control and its components.
- Explains the appearance and behavior of the AutoComplete popup.
- Provides guidelines for using the AutoComplete control effectively.

## Content

### AutoCompletion of a TextBox Text

#### See also
- [Through Designer, Concepts and Features](Through Designer, Concepts and Features)

#### 3.5.1.1.3 Concepts and Features
The following topics will help you become more familiar in using the AutoComplete control.

#### 3.5.1.1.3.1 AutoComplete Popup
When a control is associated with an AutoComplete control, a popup will be displayed, based on the **source**. This section illustrates various components of the AutoComplete Popup with their properties which can control the appearance and behavior of the components.

#### Figure 121: AutoComplete Popup Components
This section will discuss various components in the AutoComplete popup.

#### Header, Close Button and Gripper
This section explains the settings for headers, close buttons, and grippers in the AutoComplete popup.

#### Header Settings
DropDown item can have a header which is enabled using the **AutoComplete.ShowColumnHeader** property. The **AutoAddItem** property should be set to **true**.

## API Reference (if applicable)

#### Namespace
- **Syncfusion.WinForms.Controls**

#### Class
- **AutoComplete**

#### Members
- **AutoComplete.ShowColumnHeader**
  - Type: Boolean
  - Description: Enables or disables the header display in the dropdown list.

- **AutoComplete.AutoAddItem**
  - Type: Boolean
  - Description: Determines whether the entered text should be automatically added to the dropdown list.

## Code Examples

### Example: Setting AutoComplete Header
```csharp
AutoComplete autoComplete = new AutoComplete();
autoComplete.ShowColumnHeader = true;
autoComplete.AutoAddItem = true;
```

## Cross References
- [Through Designer, Concepts and Features](Through Designer, Concepts and Features)
- [3.5.1.1.3 Concepts and Features](3.5.1.1.3 Concepts and Features)

## RAG Annotations
<!-- tags: [product, AutoComplete, WinForms, Control, API, version] keywords: [AutoComplete, DropDown, header, close button, gripper, properties, appearance, behavior, components] -->
```