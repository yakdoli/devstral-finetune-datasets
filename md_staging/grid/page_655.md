```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_655.jpeg
document_name: grid
page_number: 655
page_id: grid#page_655
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:31:30Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates handling of blink states in the grid.
- Explains setting custom base styles for newly added records and handling cell changes based onblink states.

## Content
The base styles for various blink states are defined. ThePrepareViewStyleInfo event handler is used to set the custom base style for a newly added record. A cell change is highlighted by checking its BlinkState. The BlinkState indicates whether the cell's value is increased or reduced, or if the record has been recently added. If the state is eitherIncreased` orReduced`, the back color and text colors of the cell are changed.

### Code Example: C#

```csharp
// Allow Blinking for all the columns.
// Highlight up and down ticks.
gridGroupingControl1.BlinkTime = 700;
for (int i = 1; i <= 20; i++)
    gridGroupingControl1.TableDescriptor.Columns[i.ToString()].AllowBlink = true;
gridGroupingControl1.Engine.AddBaseStylesForBlinking();
gridGroupingControl1.BaseStyles[GridEngine.BlinkIncreased].StyleInfo.TextColor = Color.White;
gridGroupingControl1.BaseStyles[GridEngine.BlinkReduced].StyleInfo.TextColor = Color.White;

gridGroupingControl1.Engine.BaseStyles.Add("CustomStyle");
gridGroupingControl1.BaseStyles["CustomStyle"].StyleInfo.TextColor = Color.Black;
gridGroupingControl1.BaseStyles["CustomStyle"].StyleInfo.BackColor = Color.White;

// PrepareViewStyleInfo
void gridGroupingControl1_TableControlPrepareViewStyleInfo(object sender, GridTableControlPrepareViewStyleInfoEventArgs e)
{
    GridTableCellStyleInfo style = (GridTableCellStyleInfo)e.Inner.Style;
    BlinkState bs = gridGroupingControl1.GetBlinkState(style.TableCellIdentity);
    if (bs != BlinkState.None)
    {
        if (bs == BlinkState.NewRecord)
        {
            e.Inner.Style.BaseStyle = "CustomStyle";
        }
    }
}
```

### Code Example: VB.NET

```vb.net
' Allow Blinking for all the columns.
' Highlight up and downticks.
```

## API Reference

### Events
- **PrepareViewStyleInfo**: Raised when the grid is preparing the style information for viewing.

### Methods
- **GetBlinkState**: Returns the blink state of the specified table cell.
- **AddBaseStylesForBlinking**: Adds base styles for blinking states to the grid.

### Enums
- **BlinkState**:
  - `None`: Indicates no specific blink state.
  - `NewRecord`: Indicates a newly added record.
  - `Increased`: Indicates an increase in value.
  - `Reduced`: Indicates a reduction in value.

## Code Examples

### C# Example
The provided C# code demonstrates how to enable blinking for all columns, highlight changes (up or down ticks), and configure custom styles for specific blink states. It also shows how to handle thePrepareViewStyleInfo event to apply a custom base style to newly added records.

### VB.NET Example
The VB.NET code shows the initial setup for enabling blinking and highlights for up and down ticks.

## Page-level Navigation/TOC (if applicable)
- Blink States Overview
- Configuring Blink Styles
  - C# Example
  - VB.NET Example
- Handling New Records
- Modifying Text and Back Colors

## Cross References
- See also: [Working with Base Styles in Grid](#working-with-base-styles-in-grid)
- [Handling Events in Grid](#handling-events-in-grid)

<!-- tags: [winforms, grid, blinkstates, customstyles, prepareviewstyleinfo, newrecord] keywords: [blinktime, upanddownticks, customstyle, getblinkstate, addbasestylesforblinking] -->
```