```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_424.jpeg
document_name: tools
page_number: 424
page_id: tools#page_424
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:12:10Z
fidelity: lossless
-->

### Essential Tools for Windows Forms

#### Header Gradient

[VB.NET]

```vb
Me.monthCalendarAdv1.HeaderGradient = True
Me.monthCalendarAdv1.HeaderVerticalGradient = True
Me.monthCalendarAdv1.HeaderEndColor = System.Drawing.Color.SteelBlue
Me.monthCalendarAdv1.HeaderStartColor = System.Drawing.Color.AliceBlue
```

![Figure 222: HeaderStartColor = "AliceBlue"; HeaderEndColor = "SteelBlue"](assets/image.png "Figure 222: HeaderStartColor = \"AliceBlue\"; HeaderEndColor = \"SteelBlue\"")

---

### Foreground Settings

The font style and fore color of the header text can be specified through `HeaderFont` and `HeadForeColor` properties.

| MonthCalendarAdv Properties    | Description                                         |
|---------------------------------|-----------------------------------------------------|
| HeaderFont                     | Specifies the font of the header.                   |
| HeaderForeColor                | Specifies the fore color of the header.             |

[C#]

```csharp
this.monthCalendarAdv1.HeaderFont = new System.Drawing.Font("Arial", 9F, System.Drawing.FontStyle.Bold);
this.monthCalendarAdv1.HeaderForeColor = System.Drawing.Color.Navy;
```

[VB.NET]

```vb
Me.monthCalendarAdv1.HeaderFont = New System.Drawing.Font("Arial", 9F,
```

---

**© 2013 Syncfusion. All rights reserved.** |  ____1____ 424
```