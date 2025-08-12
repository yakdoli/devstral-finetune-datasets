```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_446.jpeg
document_name: tools
page_number: 446
page_id: tools#page_446
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:14:16Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Globalization

#### Overview
- The `MonthCalendarAdv` control supports globalization through the `MonthCalendarAdv.Culture` property.
- This property allows the control to display dates and text in a specified culture, enabling localization for different regions and languages.
- The process can be configured both through the PropertyGrid and programmatically.

#### Content
MonthCalendarAdv supports globalization through the `MonthCalendarAdv.Culture` property.

##### Selecting Culture Through PropertyGrid
The following figure demonstrates how to set the culture for the `MonthCalendarAdv` control using the PropertyGrid. This allows the control to display dates and text in the chosen language and format:

![Selecting Culture Through PropertyGrid](https://i.imgur.com/1LwLwLw.png)
*Figure 245: Selecting Culture Through PropertyGrid*

```csharp
[this.monthCalendarAdv1.Culture = new
 System.Globalization.CultureInfo("fr-FR");](https://i.imgur.com/1LwLwLw.png)
```

```vb
[Me.monthCalendarAdv1.Culture = New
 System.Globalization.CultureInfo("fr-FR")](https://i.imgur.com/1LwLwLw.png)
```

##### Code Examples
The following code examples show how to programmatically set the culture for the `MonthCalendarAdv` control to French (France) using both C# and VB.NET.

**C#**
```csharp
this.monthCalendarAdv1.Culture = new System.Globalization.CultureInfo("fr-FR");
```

**VB.NET**
```vb
Me.monthCalendarAdv1.Culture = New System.Globalization.CultureInfo("fr-FR")
```

![Calendar with French Culture](https://i.imgur.com/1LwLwLw.png)
*Example Image (Optional): Calendar Set to French (France) Culture*

### API Reference
For detailed information on `MonthCalendarAdv` and its properties, refer to the Syncfusion WinForms documentation.

#### See also:
- [Month Calendar Adv Documentation](https://www.syncfusion.com/documentation/windowsforms/monthcalendaradv)

<!-- tags: MonthCalendarAdv, Globalization, CultureInfo, PropertyGrid, C#, VB.NET, Windows Forms, WinForms -->
```