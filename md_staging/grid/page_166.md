```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_166.jpeg
document_name: grid
page_number: 166
page_id: grid#page_166
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:58:24Z
fidelity: lossless
-->

## Progress Bar

There are several formatting options that can be applied to an ProgressBar cell type embedded into the grid control. The following code example illustrates this.

### Code Example

```csharp
[C#]

// Set up a ProgressBar Control.
GridStyleInfo style3 = gridControl1[12, 2];
GridProgressBarInfo progressBarex3 = style3.ProgressBar;
style3.CellType = "ProgressBar";
style3.Themed = false;

// Apply Styles.
progressBarex3.BackGradientEndColor = System.Drawing.Color.RosyBrown;
progressBarex3.BackGradientStartColor = System.Drawing.Color.DarkRed;
progressBarex3.BackgroundStyle =
    Syncfusion.Windows.Forms.Tools.ProgressBarBackgroundStyles.VerticalGradient;
progressBarex3.BackMultipleColors = new System.Drawing.Color[0];
progressBarex3.BackSegments = false;
progressBarex3.BackTubeEndColor = System.Drawing.SystemColors.Control;
progressBarex3.BackTubeStartColor = System.Drawing.Color.LightGray;
progressBarex3.FontColor = System.Drawing.Color.Lime;
progressBarex3.ForegroundImage = null;
progressBarex3.GradientEndColor = System.Drawing.Color.Lime;
progressBarex3.GradientStartColor = System.Drawing.Color.Red;
progressBarex3.MultipleColors = new System.Drawing.Color[]
{
    System.Drawing.SystemColors.ControlDarkDark,
    System.Drawing.SystemColors.ControlLight,
    System.Drawing.SystemColors.ControlDark,
    System.Drawing.SystemColors.Control
};
progressBarex3.ProgressStyle =
    Syncfusion.Windows.Forms.Tools.ProgressBarStyles.Tube;
progressBarex3.SegmentWidth = 12;
progressBarex3.TextVisible = false;
progressBarex3.TubeEndColor = System.Drawing.Color.Black;
progressBarex3.TubeStartColor = System.Drawing.Color.Red;
progressBarex3.ProgressValue = 75;
```

<!-- tags: [Syncfusion, WinForms, ProgressBar, Grid, control, formatting, styles, multiple colors, segment width, tube style, final segment colors, text visibility, progress value] keywords: [ProgressBar, GridStyleInfo, GridProgressBarInfo, CellType, Themed, BackGradientEndColor, BackGradientStartColor, BackgroundStyle, BackMultipleColors, BackSegments, BackTubeEndColor, BackTubeStartColor, FontColor, ForegroundImage, GradientEndColor, GradientStartColor, MultipleColors, ProgressStyle, SegmentWidth, TextVisible, TubeEndColor, TubeStartColor, ProgressValue, System.Drawing.Color] -->
```