```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_425.jpeg
document_name: tools
page_number: 425
page_id: tools#page_425
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:11:35Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```csharp
System.Drawing.FontStyle.Bold)
Me.monthCalendarAdv1.HeaderForeColor = System.Drawing.Color.Navy
```

### Height and Image for Header

The height of the header can be increased or decreased using the `HeaderHeight` property. The header can also host an image in its background using the `HeaderImage` property.

| MonthCalendarAdv Properties | Description |
|-------------------------------|-------------|
| `HeaderHeight` | Specifies the height of the header. Default value is 32 for Default Style and for other styles it is 20. |
| `HeaderImage` | Specifies the image of the header. |

### C#

```csharp
this.monthCalendarAdv1.HeaderImage = 
    ((System.Drawing.Image) (resources.GetObject("monthCalendarAdv1.HeaderImage")));
this.monthCalendarAdv1.HeaderHeight = 30;
```

### VB.NET

```vb
Me.monthCalendarAdv1.HeaderImage = 
    DirectCast(resources.GetObject("monthCalendarAdv1.HeaderImage"), System.Drawing.Image)
Me.monthCalendarAdv1.HeaderHeight = 30
```

![HeaderHeight = "30"](https://i.imgur.com/1234567.png)

**Figure 224: `HeaderHeight = "30"`**

### 3.5.3.1.4.2.2 Week Numbers

The `MonthCalendarAdv` control can display unique **week numbers** for all the weeks in a year. This section discusses the properties which can customize the appearance of the week numbers.
```markdown
```