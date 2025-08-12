```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_412.jpeg
document_name: tools
page_number: 412
page_id: tools#page_412
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:11:27Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
using Syncfusion.Windows.Forms.Tools;
```

```vb.net
Imports Syncfusion.Windows.Forms.Tools
```

## Using MonthCalendarAdv

1. **Create an instance of the MonthCalendarAdv control.**

### [C#]

```csharp
private Syncfusion.Windows.Forms.Tools.MonthCalendarAdv monthCalendarAdv1;
this.monthCalendarAdv1 = new MonthCalendarAdv();
```

### [VB.NET]

```vb.net
Private monthCalendarAdv1 As Syncfusion.Windows.Forms.Tools.MonthCalendarAdv
Me.monthCalendarAdv1 = New MonthCalendarAdv()
```

2. **Set the visual style for the control. Add that instance to the Form.**

### [C#]

```csharp
this.monthCalendarAdv1.Style = Syncfusion.Windows.Forms.VisualStyle.Office2007;
this.Controls.Add(this.monthCalendarAdv1);
```

### [VB.NET]

```vb.net
Me.monthCalendarAdv1.Style = Syncfusion.Windows.Forms.VisualStyle.Office2007
Me.Controls.Add(Me.monthCalendarAdv1)
```

3. **Run the application.**

## Conclusion

Set up the MonthCalendarAdv control to customize the visual style and integrate it seamlessly into a Windows Forms application using Syncfusion Tools.

``` 
```