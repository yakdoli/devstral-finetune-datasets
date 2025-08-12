```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_885.jpeg
document_name: grid
page_number: 885
page_id: grid#page_885
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:46:14Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Grid Skins

GridSkins, an extension of GridVisualStyles, is built on the idea of providing more advanced themes for your grid, along with the basic themes defined by GridVisualStyles. It is available as an add-on feature in the GridHelperClasses library.

GridSkins depicts the custom skin of GridVisualStyles. Currently, it comes with a new Vista skin that makes your grid components appear in a Vista-like look and feel.

Grid Skins can be set by invoking the static method `ApplySkin` of the GridSkins helper class. This method accepts two parameters: a grid that needs to be styled and a `Skins` enumeration value that specifies the desired skin, and applies this desired skin to all the grid components.

### Code Examples

#### C#

```csharp
GridSkins.ApplySkin(this.gridControl1.Model, Skins.Vista);
```

#### VB.NET

```vb
GridSkins.ApplySkin(Me.gridControl1.Model, Skins.Vista)
```

Below image illustrates a sample output.

![](attachment:image.png)
*Figure 350: Grid Grouping Control with Vista Skin*

## 4.3.4.5.9 Table Options

<!-- tags: [GRID SKINS, EXTENSIONS, GRIDVISUALSTYLES, GRIDHELPERCLASSES, APPLYSKIN, VISTA SKIN, GRID COMPONENTS] keywords: [gridskins, gridvisualstyles, gridhelperclasses, applyskin, vista, vista skin, grid components, skin] -->
```