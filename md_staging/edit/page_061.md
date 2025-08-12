```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_061.jpeg
document_name: edit
page_number: 061
page_id: edit#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:57:41Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

The coordinates associated with the above properties are referred to as **Virtual (or Visible)**, because their values vary depending on factors that affect the state of the collapsible blocks, font size of the text, and so on.

**Note:** The Virtual coordinates of the top-left corner in the Edit Control is (1,1), and it is not a zero-based coordinates system.

## Overview
- Coordinates in Edit Control are classified as Virtual/Visible due to dynamic factors such as text state.
- Special consideration is given to the non-zero-based coordinate system starting at (1,1).
- APIs are available for inter-conversion between virtual/actual positions and offsets.

## Content

The following APIs are used for inter-conversion between virtual / actual positions and offsets.

### Edit Control APIs for Coordinate Conversion

| Edit Control Method                    | Description                                                                                   |
|-----------------------------------------|-----------------------------------------------------------------------------------------------|
| `PointToVirtualPosition`               | Converts point in client coordinates to the virtual position in text.                          |
| `PointToPhysicalPosition`              | Converts point in client coordinates to the physical position in text.                         |
| `ConvertVirtualPositionToPhysical`     | Converts virtual coordinates to physical coordinates.                                         |
| `ConvertVirtualPositionToOffset`       | Converts virtual position in text to the offset in stream.                                   |
| `ConvertOffsetToVirtualPosition`       | Converts in-stream offset to virtual coordinates.                                            |
| `ConvertVirtualPointToCoordinatePoint` | Converts point in virtual coordinates to coordinate point.                                    |

### Code Examples for Coordinate Conversion

[C#]

```csharp
// Convert coordinates associated with mouse position to virtual coordinates.
Point virtualPosition = this.editControl1.PointToVirtualPosition(Control.MousePosition);

// Converts coordinates associated with mouse position to physical coordinates.
Point physicalPosition = this.editControl1.PointToPhysicalPosition(Control.MousePosition);

// Converts virtual coordinates to physical coordinates.
Point physicalPosition = this.editControl1.ConvertVirtualPositionToPhysical(virtualPosition);

// Converts virtual coordinates to offset value.
long offset = this.editControl1.ConvertVirtualPositionToOffset(virtualPosition);

// Converts the offset value to virtual coordinates.
```

### Explanation of Methods

- **PointToVirtualPosition**: Converts a client coordinate point to its corresponding virtual position in the text content.
- **PointToPhysicalPosition**: Translates a client point to a physical position within the text layout.
- **ConvertVirtualPositionToPhysical**: Converts virtual coordinates to their physical counterparts, useful for rendering purposes.
- **ConvertVirtualPositionToOffset**: Maps a virtual position to an offset within the text stream.
- **ConvertOffsetToVirtualPosition**: Converts an offset back to a virtual position, aiding in interactive functionalities.
- **ConvertVirtualPointToCoordinatePoint**: Translates a point in virtual coordinates to a physical coordinate point for precise user interaction.

## API Reference

### Methods in Edit Control

#### `PointToVirtualPosition`
- **Description**: Converts client coordinates to the virtual position in text.
- **Parameters**: `Point` representing the client coordinates.
- **Returns**: `Point` in virtual coordinates.

#### `PointToPhysicalPosition`
- **Description**: Converts client coordinates to the physical position in text.
- **Parameters**: `Point` representing the client coordinates.
- **Returns**: `Point` in physical coordinates.

#### `ConvertVirtualPositionToPhysical`
- **Description**: Converts virtual coordinates to physical coordinates.
- **Parameters**: `Point` in virtual coordinates.
- **Returns**: `Point` in physical coordinates.

#### `ConvertVirtualPositionToOffset`
- **Description**: Translates a virtual position in text to an offset in the stream.
- **Parameters**: `Point` in virtual coordinates.
- **Returns**: `long` representing the offset.

#### `ConvertOffsetToVirtualPosition`
- **Description**: Converts an offset in the stream to a virtual position.
- **Parameters**: `long` representing the offset.
- **Returns**: `Point` in virtual coordinates.

#### `ConvertVirtualPointToCoordinatePoint`
- **Description**: Maps a point in virtual coordinates to a physical coordinate point.
- **Parameters**: `Point` in virtual coordinates.
- **Returns**: `Point` in physical coordinates.

## Code Examples (Extended)

### Full Example Integration

```csharp
using Syncfusion.Windows.Forms.Edit;

public class CoordinateConversionExample
{
    private SfEditControl editControl1;

    public void InitializeEditControl()
    {
        editControl1 = new SfEditControl();
        // Additional initialization and configuration can be added here.
    }

    public void ConvertMousePositionToVirtual()
    {
        Point virtualPosition = editControl1.PointToVirtualPosition(Control.MousePosition);
        Console.WriteLine($"Virtual Position: {virtualPosition}");
    }

    public void ConvertOffsetToPosition()
    {
        long offset = 50; // Example offset value
        Point virtualPosition = editControl1.ConvertOffsetToVirtualPosition(offset);
        Console.WriteLine($"Position from Offset: {virtualPosition}");
    }

    // Additional methods for converting coordinates in various scenarios can be added here.
}
```

### Usage in Windows Forms Application

The above methods can be integrated into a Windows Forms application for features such as text selection, cursor positioning, and visual adjustments based on user interaction or design requirements.

## Summary

This section outlines the use of virtual and physical coordinates within the WinForms `EditControl`, focusing on APIs that allow conversion between these coordinate systems. These functionalities are essential for developing interactive and dynamic text editing experiences in Windows Forms applications.

## Cross References
- Refer to the documentation on `EditControl` properties and events for a more comprehensive understanding of its capabilities.

<!-- tags: [EditControl, Windows Forms, Coordinate Conversion, Virtual Coordinates, Physical Coordinates, Control.MousePosition, offset, SfEditControl] keywords: [EditControl, coordinate conversion, virtual coordinates, physical coordinates, text offset, mouse position, Windows Forms] -->
```