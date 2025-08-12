```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_511.jpeg
document_name: tools
page_number: 511
page_id: tools#page_511
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:18:00Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## User Groups

The `ColorGroups` property allows you to add user groups in addition to the standard groups. The color palette for the UserGroups will be `CustomColors`, by default.

### Code Examples

#### C#

```csharp
this.colorUIControl1.ColorGroups =
    (Syncfusion.Windows.Forms.ColorUIGroups.CustomColors |
     Syncfusion.Windows.Forms.ColorUIGroups.StandardColors |
     Syncfusion.Windows.Forms.ColorUIGroups.UserColors);
```

#### VB.NET

```vbnet
Me.colorUIControl1.ColorGroups =
    DirectCast((((Syncfusion.Windows.Forms.ColorUIGroups.CustomColors Or
                 Syncfusion.Windows.Forms.ColorUIGroups.StandardColors) Or
                 Syncfusion.Windows.Forms.ColorUIGroups.UserColors)),
                 Syncfusion.Windows.Forms.ColorUIGroups)
```

### Figure

![Figure 298: User Group added to ColorUIControl](https://via.placeholder.com/300x200?text=Figure%20298:%20User%20Group%20added%20to%20ColorUIControl)

#### Notes

- **Custom Text for Tabs:** You can add custom text for the tabs of the Color groups. See [Tab Text](#tab-text) for details.
- **Stretchability of Panels:** The Custom Color Panels and User Color Panels can be stretched according to the size of the control. Refer to [ColorUIControl Appearance](#coloruicontrol-appearace) for details.

## See Also

- Runtime Settings
```