```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_086.jpeg
document_name: tools
page_number: 086
page_id: tools#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:20:31Z
fidelity: lossless
-->

### Essential Tools for Windows Forms

#### Overview
- Explains how to set the background color of the CommandBar in a Windows Forms application.
- Describes properties and code examples for adjusting the CommandBar's background and foreground settings.
- Highlights the role of the gripper in the CommandBar package for docking and floating functionality.

#### Content

- The back color of the CommandBar can be set using the property given below:

| CommandBar Property | Description |
|---------------------|-------------|
| BackColor           | The background color used to draw the component. |

**[C#]**
```csharp
this.commandBar1.BackColor = System.Drawing.Color.Wheat;
```

**[VB.NET]**
```vb
Me.commandBar1.BackColor = System.Drawing.Color.Wheat
```

![BackColor of CommandBarController and CommandBar Set](https://github.com/syncfusion/documentation/blob/main/images/CommandBar_BackColor.png)

*Figure 31: BackColor of CommandBarController and CommandBar Set*

**Note:** The `ResetBackColor()` method of the CommandBarController can be used to reset its `BackColor` property to the default value. Similarly, the `ResetBackColor()` method of the CommandBar can be used to reset its `BackColor` property to the default value.

### 3.3.3.6.2 Foreground Settings

The foreground settings of the CommandBar control are discussed below.

#### Gripper

The gripper plays a major role in the CommandBar package. It allows the user to dock / float the CommandBar at runtime.

| CommandBar Property | Description |
|---------------------|-------------|
| HideGripper        | Draws the CommandBar with / without the drag gripper. |

**[C#]**

---

© 2013 Syncfusion. All rights reserved.

<!-- tags: [Syncfusion Winforms, CommandBar, background color, foreground settings, gripper] keywords: [CommandBarBackColor, CommandBarController, HideGripper, docking, floating, runtime settings] -->
```