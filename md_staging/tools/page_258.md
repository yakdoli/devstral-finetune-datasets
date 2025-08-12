```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_258.jpeg
document_name: tools
page_number: 258
page_id: tools#page_258
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:03:11Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Introduces the use of three listboxes, a button, and a docking manager in WinForms applications.
- Demonstrates adding the namespace `Syncfusion.Windows.Forms.Tools` to enable advanced docking functionalities.
- Explains the process of tabbing controls in a docking group to achieve a specific layout.

## Content

### Steps for Implementation
1. **Add Controls to the Form**:
   - Add three listboxes, a button, and a docking manager to the form.
   
2. **Enable Docking Property**:
   - Set the `EnableDocking` property on the Docking Manager to `true`.

3. **Add the Namespace**:
   - Include the namespace `Syncfusion.Windows.Forms.Tools` in your application.

   #### Code for Adding the Namespace
   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```
   ```vb.net
   Imports Syncfusion.Windows.Forms.Tools
   ```

4. **Tab the Controls**:
   - Tab the controls as shown in the figure below.

   #### Docking Group Layout
   ![Docking Group Dialog Box](https://via.placeholder.com/600x400?text=Docking+Group)
   
   **Figure 108: Docking Group dialog box to get the Docking Group Details**

### Button Click Event Code
Add the following code in the button click event to interact with the docking group details.

#### C# Code
```csharp
Syncfusion.Windows.Forms.Tools.DockHost dhost = this.listBox1.Parent as Syncfusion.Windows.Forms.Tools.DockHost;
Syncfusion.Windows.Forms.Tools.DockHostController dhc = dhost.InternalController as Syncfusion.Windows.Forms.Tools.DockHostController;
```

## Page-level Navigation/TOC (if applicable)
<!-- None -->

## Cross References
- Refer to related topics on [Docking Group](#docking-group).

## RAG Annotations
<!-- tags: [winforms, docking, tool, listbox, button, namespace, syncfusion, enableDocking] keywords: [dockhost, dockhostcontroller, tab controls, layout, namespace addition, button click event] -->
```
