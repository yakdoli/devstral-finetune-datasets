```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_570.jpeg
document_name: tools
page_number: 570
page_id: tools#page_570
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:21:29Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Figure 350: Banner Text set for ComboBoxAdv

#### See Also

- DropDown Settings
- Data Settings

#### 3.5.5.2.3.1.2 DropoutDown Settings

**DropoutDown for the ComboBoxAdv control can be customized using the below properties.**

| ComboBoxAdv Properties     | Description                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| DropDownWidth              | Specifies the width of the dropdown. Default value is 100.                                              |
| IntegralHeight             | Indicates whether the list portion will have only complete items. i.e when this property is set to true, it will display only those items that are fully visible in terms of height. |
| MaxDropDownItems           | Maximum number of entries that can be displayed in the dropdown. Set image for the dropdown items. Refer Image Settings topic. |
| Sorted                     | When set to true, will sort the dropdown items in the alphabetical order.                                 |

#### C#

```csharp
this.comboBoxAdv1.DropDownWidth = 150;
this.comboBoxAdv1.IntegralHeight = true;
this.comboBoxAdv1.MaxDropDownItems = 5;
this.comboBoxAdv1.Sorted = true;
```

#### VB.NET

```vb
Me.comboBoxAdv1.DropDownWidth = 150
Me.comboBoxAdv1.IntegralHeight = True
Me.comboBoxAdv1.MaxDropDownItems = 5
Me.comboBoxAdv1.Sorted = True
```

## Page-level Navigation/TOC (if applicable)

<!-- tags: [comboboxadv, dropdown, integralheight, maxdropdownitems, sorted] keywords: [comboboxadv properties, dropdown customization, integral height, max dropdown items, sorting] -->
```