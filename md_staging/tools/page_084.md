```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_084.jpeg
document_name: tools
page_number: 084
page_id: tools#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:19:47Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

![](https://via.placeholder.com/150x100.png?text=Figure+29%3A+Popup+Menu+displayed+on+Right+Clicking+the+CommandBar+Control)

**Figure 29**: Popup Menu displayed on Right Clicking the CommandBar Control

## See Also

- [Popup Menu on Clicking the DropDown Button](#)

## 3.3.3.5 Hosting Child Controls

Child controls can be easily hosted by the CommandBar through designer as well as through code. This can be done by selecting the client controls from the toolbox and dropping it onto the particular CommandBar. The control will be resized to fit the CommandBar's client bounds.

A CommandBar can host a single control / multiple controls. This can be done as follows.

### Single Control

You can drag-and-drop the single client control onto the CommandBar.

### Multiple Controls

To accommodate multiple controls, place the controls within a Panel control and set it to be the CommandBar's client.

```csharp
this.commandBar1.Controls.Add(this.panel1);
```

```vb.NET
Me.commandBar1.Controls.Add(Me.panel1)
```

## API Reference

### Methods

- `Controls.Add(Control)`

### Parameters

- **Name** | **Type** | **Description** | **Default** | **Required**
- `Control` | `System.Windows.Forms.Control` | The control to be added to the CommandBar's client area. | `null` | Yes

### Returns

- Type: `void`
- Description: Adds the specified control to the CommandBar's client area.

### Exceptions

- `ArgumentNullException`: Thrown if the specified control is `null`.

## Cross References

- [Popup Menu on Clicking the DropDown Button](#)

<!-- tags: [syncfusion-winform, commandbar, hosting-child-controls, api-reference, sample-code] keywords: [child controls, commandbar, designer, developer, windows forms, hosting controls, Syncfusion] -->
```