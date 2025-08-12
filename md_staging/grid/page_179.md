```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_179.jpeg
document_name: grid
page_number: 179
page_id: grid#page_179
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:00:36Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## GridFontInfo

### Overview
- The `GridFontInfo` class is an Essential Grid wrapper class for the standard `Systems.Drawing.Font` class.
- The `Font` property of the `GridStyleInfo` class specifies the font for the text displayed in the cell.
- The `GridFontInfo` class has special static members to easily modify font property members.

### Content

#### GridFontInfo Class

The `GridFontInfo` class is explained through its usage and properties:
- It wraps the standard `Systems.Drawing.Font` class, allowing easy modification of font properties.
- Static members are available in the `GridFontInfo` class to simplify changes to font properties.

**Example:**

```csharp
// Accessing and modifying font properties using GridFontInfo
GridFontInfo fontInfo = new GridFontInfo();
fontInfo.Bold = true;
fontInfo.Size = 14;
fontInfo.Italic = true;
fontInfo.Underline = true;
fontInfo.Strikeout = true;
fontInfo.Color = Color.Red;
fontInfo.Name = "Arial";

// Applying the modified font to a GridStyleInfo
GridStyleInfo style = new GridStyleInfo();
style.Font = fontInfo.Font;
```

### Description: GridFontInfo

The `GridFontInfo` class contains the following properties:
- **Font:** Specifies the system font used for the text.
- **Horizontal:** Alignment settings for the text (Left, Center, Right).
- **HotkeyPrefix:** Specifies how keyboard accelerators are displayed in operating systems (None, Underline, Hide).
- **ImageIndex:** Index of an image in the ImageList associated with the style.
- **ImageList:** An Imaging List that contains the images.
- **Interior:** Defines the cell's interior style (Solid, Wave, Dotted, etc.).
- **ShowButton:** Determines whether a button is displayed in the cell (Show or Hide).
- **TextAlign:** Specifies the alignment of the text within the cell (Top, Center, Bottom).
- **TextColor:** Defines the color of the text.
- **TextMargins:** Specifies the margin properties for aligning the text (Left, Top, Right, Bottom).
- **Trimming:** Sets how the text is trimmed to fit the cell (Character, Word, Ellipsis).
- **VerticalAlign:** Vertical alignment for the text (Top, Middle, Bottom).
- **AllowEnter:** Determines whether pressing the Enter key moves the focus to the next cell (True or False).

**Figure 97: GridFontInfo**

![Figure 97: GridFontInfo](image_of_grid_font_info.png)

### ImageList

#### ImageList Property

The `ImageList` property holds a `Systems.Windows.Forms.ImageList`. Generally, there is one `ImageList` stored in a parent `GridInfoStyle` such as the `standardstyle` or the `tablestyle`. This single `ImageList` is shared by all cells in the grid through the `ImageIndex` property, which is set on a cell-by-cell basis.

### Description: ImageList

The `ImageList` property in `GridInfoStyle`:
- Contains multiple images.
- Is shared across cells in the grid.
- Uses the `ImageIndex` property to specify which image to display in each cell.

#### Example Usage

```csharp
// Creating and assigning an ImageList to a Grid
ImageList myImages = new ImageList();
myImages.Images.Add(Properties.Resources.MyImage1);
myImages.Images.Add(Properties.Resources.MyImage2);

GridInfoStyle style = new GridInfoStyle();
style.ImageList = myImages;

// Different cells use the same ImageList but with different ImageIndexes
style["A1"].ImageIndex = 0;
style["A2"].ImageIndex = 1;
```

## Cross References
- **See also:** [Essential Grid Documentation](https://www.syncfusion.com/documentation/windowsforms/)

<!-- tags: [Essential Grid, GridFontInfo, ImageList, GridStyleInfo, Windows Forms, Syncfusion] keywords: [GridFontInfo, GridStyleInfo, Font, ImageList, ImageIndex, TextColor, ImageList, properties, methods, Grid] -->
```