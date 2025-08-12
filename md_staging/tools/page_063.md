```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_063.jpeg
document_name: tools
page_number: 063
page_id: tools#page_063
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:18:02Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

![Figure 13: CommandBar created Through Code](https://i.imgur.com/image.png)

## See Also

- Through Designer
- Through XP Menus Framework

## 3.3.2.3 Through XP Menus Framework

The XP Menus framework provides the flexibility to add detached toolbars that can host any .NET control. These toolbars are detached from the framework, i.e., they cannot participate in user customization. Otherwise, they are seamless in look and feel.

1. Right click on the **MainFrameBarManager** component and choose the **Add Detached CommandBar** option to add a detached toolbar.
2. Add that control by dragging and dropping to any .NET control. If you need to host multiple controls, you will need to first add a panel to the CommandBar and then add the controls to this panel.

```csharp
// Declare the controls.
private Syncfusion.Windows.Forms.Tools.XPMenus.MainFrameBarManager mainFrameBarManager2;
private Syncfusion.Windows.Forms.Tools.CommandBar commandBar2;

// Initialize the controls.
this.mainFrameBarManager2 = new Syncfusion.Windows.Forms.Tools.XPMenus.MainFrameBarManager(this);
this.commandBar2 = new Syncfusion.Windows.Forms.Tools.CommandBar();

// Set the properties.
this.mainFrameBarManager2.DetachedCommandBars.Add(this.commandBar2);
this.mainFrameBarManager2.Form = this;
```

### Submit the control to the form.

<!-- tags: [Syncfusion Winforms, XP Menus Framework, Detached Toolbars, Customization, .NET Control Hosting, Framework Detachment, User Guide, CommandBar, Designer Interface, Through Designer, Through XP Menus Framework] -->
```