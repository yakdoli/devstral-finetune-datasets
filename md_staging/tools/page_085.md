```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_085.jpeg
document_name: tools
page_number: 085
page_id: tools#page_085
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:20:33Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Introduction to multiple controls hosted in CommandBar (Label and ComboBox).
- Description of methods related to client control bounds calculation.
- Explanation of appearance settings for enhancing CommandBar control appearance.

## Content

### Figure 30: CommandBar Hosting Multiple Controls (Label and ComboBox)

The method associated with the above property is given below.

| Method                   | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| CalcChildControlBounds   | Calculates the client control bounds for the specified CommandBar size and dock position. |

### 3.3.3.6 Appearance Settings

#### Description
The appearance settings that play a vital role in enhancing the appearance of the CommandBar control are listed below.

### 3.3.3.6.1 Background Settings

#### Description
The background settings of the CommandBar control are discussed below.

#### BackColor

##### CommandBarController
The back color of the CommandBarController can be set using the property given below.

| CommandBarController Property | Description             |
|--------------------------------|-------------------------|
| BackColor                      | The background color used to draw the host form's dockable regions. |

#### Code Examples
```csharp
this.commandBarController1.BackColor = System.Drawing.Color.RosyBrown;
```

```vb
Me.CommandBarController1.BackColor = System.Drawing.Color.RosyBrown
```

### CommandBar

---

<!-- tags: [syncfusion, winforms, commandbar, appearance settings, backcolor, commandbarcontroller] keywords: [calcchildcontrolbounds, clientcontrolbounds, commandbarController, backColor] -->
```