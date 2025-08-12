```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_087.jpeg
document_name: tools
page_number: 087
page_id: tools#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:19:41Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Advanced Customization of CommandBar

### Hiding the Gripper

The `HideGripper` property controls whether the gripper, a small rectangular handle typically found at the end of a CommandBar, is visible. Setting this property to `true` hides the gripper.

#### Code Examples

- **C#**
  ```csharp
  this.commandBar1.HideGripper = true;
  ```

- **VB.NET**
  ```vb
  Me.commandBar1.HideGripper = True
  ```

#### Visual Representation

![CommandBar with and without Gripper](example_image_url)

**Figure 32: "HideGripper" property of CommandBar**

### Font Customization

The font of the text displayed in the CommandBar can be customized using the `Font` property provided below.

#### CommandBar Property Description

| CommandBar Property | Description                  |
|---------------------|-------------------------------|
| Font                | The font used to display text in the control. |

#### Code Examples

- **C#**
  ```csharp
  this.commandBar3.Font = new System.Drawing.Font("Comic Sans MS", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
  ```

- **VB.NET**
  ```vb
  Me.commandBar3.Font = New System.Drawing.Font("Comic Sans MS", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CByte((0)))
  ```

#### Visual Representation

![CommandBar with custom font](example_image_url)

**Figure 33: "Font" property of CommandBar Set**

```html

<!-- tags: [Syncfusion Winforms, CommandBar, Gripper, Font customization] keywords: [CommandBar, HideGripper, Font property, Windows Forms, custom font, C#, VB.NET, Syncfusion] -->
```