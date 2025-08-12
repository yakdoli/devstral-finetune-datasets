```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_167.jpeg
document_name: grid
page_number: 167
page_id: grid#page_167
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:59:34Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates setting up and styling a Progress Bar Control using VB.NET.
- Customizes the appearance of the Progress Bar by applying various background colors and gradients.

## Content

### Setup and Customization of Progress Bar Control

```vb
'[VB.NET]

' Set up a Progress Bar Control.
Dim style3 As GridStyleInfo = gridControl1(12, 2)
Dim progressBars3 As GridProgressBarInfo = style3.ProgressBar
style3.CellType = "ProgressBar"
style3.Themed = False

' Apply Styles.
progressBarEx3.BackColor = System.Drawing.Color.Empty
progressBarEx3.BackgroundGradientEndColor = System.Drawing.Color.RosyBrown
progressBarEx3.BackgroundGradientStartColor = System.Drawing.Color.DarkRed
progressBarEx3.BackgroundStyle = Syncfusion.Windows.Forms.Tools.ProgressBarBackgroundStyles.VerticalGradient
progressBarEx3.BackMultipleColors = New System.Drawing.Color(0) {}
progressBarEx3.BackSegments = False
progressBarEx3.BackTubeEndColor = System.Drawing.SystemColors.Control
progressBarEx3.BackTubeStartColor = System.Drawing.Color.LightGray
progressBarEx3.FontColor = System.Drawing.Color.Lime
progressBarEx3.ForeColor = Nothing
progressBarEx3.GradientEndColor = System.Drawing.Color.Lime
progressBarEx3.GradientStartColor = System.Drawing.Color.Red
progressBarEx3.MultipleColors = New System.Drawing.Color() {
  System.Drawing.SystemColors.ControlDarkDark,
  System.Drawing.SystemColors.ControlLight,
  System.Drawing.SystemColors.ControlDark,
  System.Drawing.SystemColors.Control}
progressBarEx3.ProgressStyle = Syncfusion.Windows.Forms.Tools.ProgressBarStyles.Tube
progressBarEx3.SegmentWidth = 12
progressBarEx3.TextVisible = False
progressBarEx3.TubeEndColor = System.Drawing.Color.Black
progressBarEx3.TubeStartColor = System.Drawing.Color.Red
progressBarEx3.ProgressValue = 75
```

## API Reference

### Members Used

- **GridStyleInfo**
  - `CellType`: Specifies the type of cell (in this case, "ProgressBar").
  - `Themed`: Indicates whether the control should use system themes.
  
- **GridProgressBarInfo**
  - `BackColor`: Sets the background color of the progress bar.
  - `BackgroundGradientEndColor`: Specifies the end color of the background gradient.
  - `BackgroundGradientStartColor`: Specifies the start color of the background gradient.
  - `BackgroundStyle`: Defines the style of the background gradient.
  - `BackMultipleColors`: Allows setting multiple background colors for the progress bar.
  - `BackSegments`: Enables segment styling for the progress bar.
  - `BackTubeEndColor`: Sets the end color of the tube-style gradient.
  - `BackTubeStartColor`: Sets the start color of the tube-style gradient.
  - `FontColor`: Specifies the color of the text displayed on the progress bar.
  - `ForeColor`: Specifies the foreground color of the progress bar.
  - `GradientEndColor`: Specifies the end color of the gradient in the progress bar.
  - `GradientStartColor`: Specifies the start color of the gradient in the progress bar.
  - `MultipleColors`: Allows setting multiple colors for the progress bar.
  - `ProgressStyle`: Defines the style of the progress bar (e.g., Tube).
  - `SegmentWidth`: Specifies the width of each segment in the progress bar.
  - `TextVisible`: Determines whether the text on the progress bar is visible.
  - `TubeEndColor`: Sets the end color for the tube-like appearance.
  - `TubeStartColor`: Sets the start color for the tube-like appearance.
  - `ProgressValue`: Specifies the current progress value (out of 100).

## Cross References
- For more information on setting up and styling controls in the Syncfusion Grid, see the official documentation on Grid Controls.
- **See also:** GridControl, ProgressBar, Theme Customization, Gradient Styles.

<!-- tags: [Windows Forms, Progress Bar, Themed Controls, Gradient Style, Progress Bar Styles, Multiple Colors, ProgressBarEx] keywords: [progress bar, themed controls, gradient end, gradient start, background style, segment width, text visible, tube end color, tube start color, progress value, multiple colors, cell type, progress style, syncfusion windows forms, vb.net] -->
```
