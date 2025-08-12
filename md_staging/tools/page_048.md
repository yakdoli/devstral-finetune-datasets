```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_048.jpeg
document_name: tools
page_number: 048
page_id: tools#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:17:42Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

Drag the component onto the form. The control in the form, for ex., ComboBoxBarItem, will get an extender provider property as in the image below.

## Figure 6: BannerText Provider Properties in ComboBoxBarItem PropertyGrid

![Figure 6: BannerText Provider Properties in ComboBoxBarItem PropertyGrid](https://screenshot-url-here/)

## Customizing the Banner Text

Extender properties which let you customize the Banner text are as follows.

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Visible</td>
      <td>Indicates whether the banner text should be visible or not.</td>
    </tr>
    <tr>
      <td>Text</td>
      <td>Sets the banner text.</td>
    </tr>
    <tr>
      <td>Color</td>
      <td>Sets the banner text color.</td>
    </tr>
    <tr>
      <td>Font</td>
      <td>Sets the font style for the banner text.</td>
    </tr>
    <tr>
      <td>Mode</td>
      <td>
        Specifies the rendering mode of the banner text. The modes are: <br>
        - FocusMode - The banner text disappears when the control gets
      </td>
    </tr>
  </tbody>
</table>

## API Reference

### Properties

- **Visible**
  - Type: Boolean
  - Description: Indicates whether the banner text should be visible or not.

- **Text**
  - Type: String
  - Description: Sets the banner text.

- **Color**
  - Type: Color
  - Description: Sets the banner text color.

- **Font**
  - Type: Font
  - Description: Sets the font style for the banner text.

- **Mode**
  - Type: Enum
  - Description: Specifies the rendering mode of the banner text.
    - FocusMode: The banner text disappears when the control gets focus.

## Code Examples

```csharp
comboBoxBarItem1.BannerTextProvider.Visible = true;
comboBoxBarItem1.BannerTextProvider.Text = "Enter Your Country";
comboBoxBarItem1.BannerTextProvider.Color = Color.RoyalBlue;
comboBoxBarItem1.BannerTextProvider.Font = new Font("Verdana", 8.25f, FontStyle.Regular);
comboBoxBarItem1.BannerTextProvider.Mode = BannerTextMode.FocusMode;
```

## Cross References

See also:
- ComBoxBarItem
- BannerTextProvider
- Windows Forms Controls

<!-- tags: [syncfusion, windowsforms, banner, extenderprovider, comboboxbaritem] keywords: [banner text, custom text, focus mode, propertygrid, windows forms] -->
```