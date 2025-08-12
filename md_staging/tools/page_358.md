```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_358.jpeg
document_name: tools
page_number: 358
page_id: tools#page_358
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:08:49Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Adding Buttons using ButtonEditChildButton Collection Editor

**Figure 170: Adding Buttons using ButtonEditChildButton Collection Editor**

<figure>
 <img src="image.png" alt="ButtonEditChildButton Collection Editor" />
 <figcaption>Note: You can also add or remove buttons to the ButtonEdit.Buttons collection through the Add Button and Remove Button verbs provided.</figcaption>
</figure>

1. **Run the application.**
   
   You can specify handlers for these child buttons also.
   
   **Figure 171: ButtonEdit Control with Child Buttons at Run Time**
   
   <figure>
    <img src="button_edit_runtime.png" alt="ButtonEdit Control with Child Buttons at Run Time" />
    <figcaption>Figure 171: ButtonEdit Control with Child Buttons at Run Time</figcaption>
   </figure>

## See Also

- **Concepts and Features**
- **3.5.2.2.2 Through Code**

### Creating a ButtonEdit Control Programmatically

To create a ButtonEdit control programmatically, follow the below steps:

1. **Include the required namespace.**

   **C#**
   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```

   **VB.NET**
   ```vbnet
   Imports Syncfusion.Windows.Forms.Tools
   ```

2. **Create an instances of ButtonEdit, TextBox and three ButtonEditChildButtons.**

   **C#**
   ```csharp
   ```

---

**Page Footer:**
© 2013 Syncfusion. All rights reserved.  
Page 358 | Page

### Relevant API

- Namespace: `Syncfusion.Windows.Forms.Tools`
  - Class: `ButtonEdit`
  - Methods:
    - `AddButton`
    - `RemoveButton`

### Cross References

- **See also:**
  - **Concepts and Features**
  - **3.5.2.2.2 Through Code**

### RAG Annotations
<!-- tags: [Syncfusion Winforms, ButtonEdit, ButtonEditChildButton, Design-Time Editing] keywords: [design-time, run-time, buttons, control, api, version] -->
```