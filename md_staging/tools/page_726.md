```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_726.jpeg
document_name: tools
page_number: 726
page_id: tools#page_726
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:31:03Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Lists events related to property changes for the `ThemesEnabled`, `SpinOrientation`, `BorderSides`, `BorderColor`, and `Border3DStyle` properties.
- Describes the `KeyDown` event handling to add new items to a list when the user presses the Enter key.

## Content

| Event Name                     | Description                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|
| `ThemeChanged`                   | This event is handled when the `ThemesEnabled` property is changed.      |
| `SpinOrientationChanged`         | This event is handled when the orientation of the spin button is changed. |
| `BorderSidesChanged`             | This event is handled when the `BorderSides` property is changed.         |
| `BorderColorChanged`             | This event is handled when the `BorderColor` is changed.                 |
| `Border3DStyleChanged`           | This event is handled when the `Border3DStyle` is changed.               |

### 3.5.8.2.5 Frequently Asked Questions

#### 3.5.8.2.5.1 How to add new items to the List when enter key is pressed

To add the new items which are entered by the user at runtime after the user had pressed the enter key, we need to catch the `KeyDown` event.

##### C#

```csharp
private void domainUpDownExt1_KeyDown(object sender, System.Windows.Forms.KeyEventArgs e)
{
    // Add new items when user press the Enter key.
    if (e.KeyCode == Keys.Enter)
    {
        if (!domainUpDownExt1.Items.Contains(domainUpDownExt1.Text))
        {
            domainUpDownExt1.Items.Add(domainUpDownExt1.Text);
        }
    }
}
```

##### VB.NET

```vb
Private Sub domainUpDownExt1_KeyDown(ByVal sender As Object, ByVal e As System.Windows.Forms.KeyEventArgs)
    ' Add new items when user press the Enter key.
    If e.KeyCode = Keys.Enter Then
        If Not domainUpDownExt1.Items.Contains(domainUpDownExt1.Text) Then
            domainUpDownExt1.Items.Add(domainUpDownExt1.Text)
        End If
    End If
End Sub
```

### Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- Check for any cross-page references or section links present in the provided text and include them here. If not applicable, skip this section.

### RAG Annotations
The following tags and keywords are derived from the visible content:
<!-- tags: [syncfusion, windows forms, events, properties, control style, keydown] keywords: [ThemeChanged, SpinOrientationChanged, BorderSidesChanged, BorderColorChanged, Border3DStyleChanged, KeyDown, Enter key, domainUpDownExt] -->
```