```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_695.jpeg
document_name: tools
page_number: 695
page_id: tools#page_695
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:29:51Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The FolderBrowser includes a TextBox control in the FolderBrowser Dialog that allows the user to type any text. The TextBox is capable of AutoCompleting the text entered.

## See Also

- [Concepts and Features](Concep)
- [[5.7.1.2 Creating FolderBrowser](5.7.1.2%20Creating%20)

### FolderBrowser control can be created in the following ways.

#### 3.5.7.1.2.1 Through Designer

The designer-based approach for creating and initializing the FolderBrowser component is shown below.

#### 1. Select the FolderBrowser control from the Visual Studio .NET toolbox window and drop it onto the design form. An instance of the FolderBrowser component will be added to the design form's component tray.

![](https://i.imgur.com/U8u8u8u.png)

**Figure 433: FolderBrowser in Toolbox**

#### 2. Select a suitable value for the `FolderBrowser.StartLocation` property from the enumerator list provided by the property grid. This specifies the location at which browsing should be started in the folder hierarchy. This property is the functional equivalent of the `Win32 PIDL`s.

#### 3. Specify an appropriate value for the `FolderBrowser.Style` property. The `FolderBrowserStyles` enumeration specifies various options for the FolderBrowser Dialog.

#### 4. To display the FolderBrowser window, simply invoke the `FolderBrowser.ShowDialog()` method from within your application's code.

---

© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [syncfusion, winforms, folderbrowser, toolbox, design, style, startlocation, showdialog, control, autocomplete] keywords: [folderbrowser, textbox, visual studio, .net toolbox, property grid, folder hierarchy] -->
```