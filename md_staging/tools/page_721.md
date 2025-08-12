```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_721.jpeg
document_name: tools
page_number: 721
page_id: tools#page_721
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:29:26Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```csharp
this.domainUpDownExt1.UpDownAlign = LeftRightAlignment.Left;
```

```vb
Me.domainUpDownExt1.UpDownAlign = LeftRightAlignment.Left
```

![UpDownAlign = "Left"](image.png)

**Figure 451: UpDownAlign = "Left"**

### 3.5.8.2.3.2.1 Keyboard SupportUsing Up and Down arrow keys we can increment and decrement the value of DomainUpDownExt control by setting InterceptArrowKeys to true.

| DomainUpDownExt Property      | Description                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------|
| InterceptArrowKeys            | Specifies whether the up-down control will increment and decrement when Up Arrow and Down Arrow keys are pressed. |

```csharp
this.domainUpDownExt1.InterceptArrowKeys = true;
```

```vb
Private Me.domainUpDownExt1.InterceptArrowKeys = True
```

### 3.5.8.2.3.3 Visual Styles DomainUpDownExt supports Office2007 visual style with all three color schemes.

```csharp
//sets the Office2007 Visual Style.
this.domainUpDownExt1.VisualStyle =
Syncfusion.Windows.Forms.VisualStyle.Office2007;
//To set Blue Color scheme.
this.domainUpDownExt1.ColorScheme =
Syncfusion.Windows.Forms.Office2007Theme.Blue;
//To set Silver Color scheme.
this.domainUpDownExt1.ColorScheme =
```

```markdown
© 2013 Syncfusion. All rights reserved.
```
```