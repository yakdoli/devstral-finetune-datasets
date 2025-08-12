```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_485.jpeg
document_name: tools
page_number: 485
page_id: tools#page_485
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:15:26Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Themes and Styles

#### Themes

We can apply themes for the DateTimePickerAdv and also the child controls using the below properties.

| DateTimePickerAdv Properties         | Description                                                                                                                                                                                                                                  |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ThemesEnabled                         | Specifies whether to enable themes for the DateTimePickerAdv control.                                                                                                                                                                      |
| ThemedChildControls                   | Setting ThemesEnabled to true will not enable themes for its child controls (CheckBox, DropDown, UpDown, and Calendar). To enable themes for the child controls of the DateTimePicker, set ThemedChildControls to true.                                      |

#### Code Examples

```csharp
this.dateTimePickerAdv1.ThemesEnabled = true;
this.dateTimePickerAdv1.ThemedChildControls = true;
```

```vb
Me.dateTimePickerAdv1.ThemesEnabled = True
Me.dateTimePickerAdv1.ThemedChildControls = True

' Setting backcolor for the control when it is ReadOnly
Me.dateTimePickerAdv1.ReadOnly = True
Me.dateTimePickerAdv1.IgnoreThemeBackground = True
```

<!-- tags: [product, module, control, api, version?] keywords: [DateTimePickerAdv, ThemesEnabled, ThemedChildControls, ReadOnly, IgnoreThemeBackground] -->
```