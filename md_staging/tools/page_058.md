```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_058.jpeg
document_name: tools
page_number: 058
page_id: tools#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:18:40Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

It allows the user to save and load the state of the CommandBar objects using different storage techniques.

### See Also

- Concepts and Features

### 3.3.2 Creating CommandBar

This section will give a step-by-step procedure to design a CommandBar control through designer, through programmatical approach and also through the XP Menus framework.

#### 3.3.2.1 Through Designer

The CommandBar framework makes it an effortless process to add, remove, and design the CommandBars in an application. With the WYSIWYG designer that it provides, all that is involved in setting up the CommandBar layout is to drag and drop the various CommandBars to the target location. The layout state is then serialized by the designer along with the form's resources and is used when the form is loaded at run time.

The following steps are involved in creating and setting up a simple CommandBar layout.

- Drag the **CommandBarController** component from the toolbox onto the form. The CommandBarController will be created in the components area of the form.

![CommandBarController in Toolbox](https://i.imgur.com/6r8IQBB.png)
**Figure 9: CommandBarController in Toolbox**

To add a CommandBar using the properties window, follow the procedure given below.

1. In the properties window, select the **CommandBars** property. The **CommandBar Collection Editor** will be opened. Click **Add**, a CommandBar will be added to the form.

---

<!-- tags: [syncfusion, winforms, commandbar, how-to, designer] keywords: [commandbar, designer, WYSIWYG, layout, properties window, CommandBarController, CommandBar Collection Editor, toolbox, visual studio] -->
```