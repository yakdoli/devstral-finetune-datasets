```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_482.jpeg
document_name: tools
page_number: 482
page_id: tools#page_482
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:16:12Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- This section discusses the essential tools available in Syncfusion WinForms, focusing on the use of a DateTimePickerAdv control.
- Includes details on customizing the Popup Menu and Context Menu for DateTimePickerAdv controls.

### Content

#### 3.5.3.2.3.5.2 Context Menu

When you right-click on a DateTimePickerAdv control at run time, a context menu will be displayed like the below image.

##### Figure 278: Images for the Popup Menu

![Images for the Popup Menu](https://via.placeholder.com/300x200?text=Figure+278)

##### Figure 279: Default Context Menu

When you right-click on a DateTimePickerAdv control at run time, a context menu will be displayed like the below image.

![Default Context Menu](https://via.placeholder.com/300x200?text=Figure+279)

This default context menu can be replaced with Syncfusion XP Menu by setting the `UseEnhancedMenu` property to `true`. By default, it is set to `false`.

##### Code Examples

- **C#**

```csharp
this.dateTimePickerAdv1.UseEnhancedMenu = true;
```

- **VB.NET**

```vb
Me.dateTimePickerAdv1.UseEnhancedMenu = True
```

### API Reference
- **Property:** `UseEnhancedMenu`
  - Type: `bool`
  - Description: Determines whether the control uses the enhanced XP menu. When set to `true`, the default context menu is replaced with the Syncfusion XP menu.

### Cross References
- See also: DateTimePickerAdv control documentation, XP Menu customization details.

<!-- tags: Essentials, Context Menu, DateTimePickerAdv, XP Menu, Syncfusion WinForms, Windows Forms, version: 11.4.0.26 -->
```