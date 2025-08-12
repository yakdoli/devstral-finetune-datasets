```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_515.jpeg
document_name: tools
page_number: 515
page_id: tools#page_515
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:18:11Z
fidelity: lossless
--> 

## Essential Tools for Windows Forms

### Custom Color Panel

#### Figure 301: Custom Color Panel's Normal and Stretched View

![Figure 301: Custom Color Panel's Normal and Stretched View](https://i.imgur.com/figure/301_normal_and_stretched_view.png)

#### 3.5.4.1.5 Runtime Settings

At run time, a particular `color group` tab should be focussed or selected. Use the `SelectedColorGroup` property of the `ColorUI` property for this purpose.

The options are as follows:

- CustomColors
- StandardColors
- SystemColors
- UserColors
- None (Default)

Use the `SelectedColor` property to specify the initially selected color.

#### Example Code

**[C#]**

```csharp
this.colorUIControl1.SelectedColorGroup = 
    Syncfusion.Windows.Forms.ColorUISelectedGroup.StandardColors;
this.colorUIControl1.SelectedColor = System.Drawing.Color.OrangeRed;
```

**[VB.NET]**

```vb
Me.colorUIControl1.SelectedColorGroup = 
    Syncfusion.Windows.Forms.ColorUISelectedGroup.StandardColors
Me.colorUIControl1.SelectedColor = System.Drawing.Color.OrangeRed
```

---

### References

- **Figure 301**: Custom Color Panel’s Normal and Stretched View

### Notes

- The `SelectedColorGroup` property allows you to specify which tab in the Color Panel should be selected at runtime.
- The `SelectedColor` property sets the initial color that is highlighted when the Color Panel is first displayed.

---

<!-- tags: [Syncfusion, Winforms, ColorUI, selectedcolorgroup, runtime, C#, VB.NET] keywords: [custom color panel, runtime settings, selected color group, selected color, standard colors, system colors, user colors, none, orange red,以色や色パレツト、OSやバ빌ジョン- Qual sẽ cất dữ à kết và giữa nhiều liê,故 cẩn địa về các giốn ổ tag và性质きिध Banking]] RAG Annotations Section', color selection, tab focus, selectedcolor, figure 301] -->
```