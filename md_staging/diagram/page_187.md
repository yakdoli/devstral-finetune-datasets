```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_187.jpeg
document_name: diagram
page_number: 187
page_id: diagram#page_187
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:18:43Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This section discusses the essential diagram components and scroll settings for Windows Forms.
- Detailed explanation of properties like ScrollGranularity and SmoothMouseWheelScrolling in the diagram.
- Includes a sample diagram illustrating the process flow with scroll functionalities.

## Content

### Sample Diagram
![Diagram With Scroll Settings](#)

**Figure 116: Diagram With Scroll Settings**

#### ScrollGranularity
- *ScrollGranularity* determines the level of granularity for scrolling. The value of this property must be greater than 0.
- This value is multiplied by the virtual size of the view to determine the scroll range.
- Example: If the virtual size of the view is 100x50 and ScrollGranularity is set to 0.5f, the horizontal scroll range is set to 0.50 and the vertical scroll range is set to 0.25.

#### SmoothMouseWheelScrolling
- *SmoothMouseWheelScrolling* specifies whether the control should perform one scroll command (faster) or multiple scroll commands with smaller increments (smoother) when the user rolls the mouse wheel.

### Properties and Their Descriptions

| Property           | Description                                                                                              |
|--------------------|----------------------------------------------------------------------------------------------------------|
| EnableIntelliMouse | Toggles support for Intelli-Mouse panning. When the user presses the middle-mouse button and drags the mouse, the window will scroll. |

## API Reference

### Namespace: Syncfusion.Windows.Forms

#### Property: EnableIntelliMouse
- **Description**: Toggles support for Intelli-Mouse panning.
- **Usage**: Enables or disables Intelli-Mouse panning functionality.

#### Property: ScrollGranularity
- **Description**: Determines the level of granularity for scrolling.
- **Usage**: Controls the scroll range based on virtual view size and multiplier value.

#### Property: SmoothMouseWheelScrolling
- **Description**: Specifies whether to perform one or multiple scroll commands during mouse wheel scrolling.
- **Usage**: Controls the smoothness of scrolling based on user preference for speed and increment size.

## Code Examples

### C# Example: Configuring Scroll Settings

```csharp
// Configure Scroll Settings
diagram.ScrollGranularity = 0.5f;
diagram.SmoothMouseWheelScrolling = true;
diagram.EnableIntelliMouse = true;
```

## Page-level Navigation/TOC
- [Section 1: Scroll Settings](#scroll-settings)
- [Section 2: Intelli-Mouse Support](#intelli-mouse-support)
- [Section 3: Scroll Granularity Details](#scroll-granularity-details)
- [Section 4: Smooth Scroll Implementation](#smooth-scroll-implementation)

## Cross References
- See also: [Syncfusion WinForms Documentation](#Syncfusion-WinForms-Documentation)
- Additional resources: [Scrolling Behavior in Diagrams](#scrolling-behavior-in-diagrams)

<!-- tags: [Syncfusion WinForms, Diagram, Scroll Settings, Intelli-Mouse Support, Smooth Scrolling, Scroll Granularity] keywords: [ScrollGranularity, SmoothMouseWheelScrolling, EnableIntelliMouse, WinForms, diagram, scroll, IntelliMouse, panning] -->
```