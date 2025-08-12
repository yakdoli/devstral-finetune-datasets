```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_205.jpeg
document_name: edit
page_number: 205
page_id: edit#page_205
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:07:12Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

### Overview
- Demonstrates the Split Views feature in the Syncfusion WinForms Edit Control.
- Provides a sample installation path for the Split Views demo.
- Explains how to apply XP-style themes to the Edit Control.

### Content

#### Figure 63: Edit Control Split into Four Quadrants

A sample which demonstrates Split Views is available in the below sample installation path.

```
.. \My Documents \Syncfusion \EssentialStudio \VersionNumberWindows \Edit.Windows \Samples \2.0 \Appearance \SplitViewsDemo
```

#### See Also
- **Scrolling Support**

#### 4.9.1.3 Applying Themes

Edit Control has the ability to have Windows XP-like themed appearance. All its features like the scrollbars, splitters, control borders, outlining tooltip, intellisense popups - context tooltip, context choice, and context prompt appear themed. The XP themes support is independent of the underlying operating system, and hence the Edit Control appears themed even on Non-Windows XP systems.

The themed appearance can be provided for the Edit Control by setting the UseXPStyle property to `True`.

```csharp
this.editControl1.UseXPStyle = true;
```

```vb.net
Me.editControl1.UseXPStyle = True
```

### Page-level Navigation/TOC (if applicable)

- **Edit Control Split into Four Quadrants**
- **Split Views Demonstration**
- **Applying Themes for XP-like Appearance**
- **Scrolling Support**

### Cross References

- **Scrolling Support**: For additional details on managing scrolling in the Edit Control.

### API Reference (if applicable)
- `UseXPStyle`: Property of the Edit Control to enable XP-style theming.

### Code Examples (multi-language supported)
- **C#**
```csharp
this.editControl1.UseXPStyle = true;
```
- **VB.NET**
```vb.net
Me.editControl1.UseXPStyle = True
```

<!-- tags: [Syncfusion Winforms, Edit Control, XP Themes, Split Views, Appearance] keywords: [Edit Control, XP Style, Themes, Splitting Views, Scrolling Support, Split Control, WinForms, Appearance Settings] -->
```