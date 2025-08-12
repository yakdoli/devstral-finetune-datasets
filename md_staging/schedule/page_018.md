```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_018.jpeg
document_name: schedule
page_number: 018
page_id: schedule#page_018
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:08:46Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview
- The Essential Schedule control primarily consists of a `UserControl` derived class named `ScheduleControl`.
- Discusses the main properties of the `ScheduleControl`, which relies on data from any object implementing `IScheduleDataProvider`.
- Focuses on the concrete implementation of the `IScheduleDataProvider`, based on an `ArrayList`-derived object that serializes to a disk file.

## Content

### ScheduleControl Properties

**ScheduleControl Implementation**
The above screen shot shows a `ScheduleControl` displaying a Month view. The four marked areas are actually `Control`-derived objects (two Panels and two `GridControls`). These controls have been added to the `ScheduleControl.Controls` collection. Any of the four controls, except the `ScheduleGrid`, can be hidden through the property settings. Here is a short description of each of the 4 labeled areas:

#### CaptionPanel
- **Type**: Panel
- **Purpose**: Displays a caption at the top of the `ScheduleControl`.
- **Additional Controls**: Two button objects on this panel for navigating the Schedule forward and backward.
- **Hide Option**: Can be hidden using the `ScheduleControl.Appearance.ShowCaption` property.
- **Docking**: Docked at the top of the `ScheduleControl` client area.

#### NavigationPanel
- **Type**: Panel
- **Purpose**: Allows you to place additional controls and make them appear adjacent to the `ScheduleControl`.
- **Docking Options**: Can be optionally docked to the left or right side of the `ScheduleControl`.
- **Hide Option**: Can also be hidden.
- **Content**:
  - **NavigationCalendar**: A `GridControl`-derived object displaying multiple calendars.
  - **Splitter**: Allows displaying more or fewer calendars in the `NavigationCalendar`. The default setting displays three.
  - **Custom Controls**: You can easily add your own controls under the `NavigationCalendar` using code similar to the snippets provided.

#### Example of Adding a Custom Control to the NavigationPanel

```csharp
// Create a new Panel
Panel p = new Panel();
// Customize the Panel's properties
p.BackColor = Color.Blue;
p.Dock = DockStyle.Fill;
p.BackgroundImage = Image.FromFile(@"...\sync.png");
p.BackgroundImageLayout = ImageLayout.Tile;

// Add the Panel to the NavigationPanel
this.ScheduleControl.AddControlToNavigationPanel(p);
```

#### NavigationCalendar
- **Type**: GridControl-derived object
- **Purpose**: Displays multiple calendars, allowing you to select the dates displayed in the `ScheduleControl`.
- **Docking**: Docked at the top of the `NavigationPanel`.
- **Number of Calendars**: Determined by its client height. Enlarging the height of the `NavigationCalendar` will display more calendars.
- **Control Adjustment**: Facilitated by the Splitter docked under the `NavigationCalendar`.

### Conclusion
The `ScheduleControl` provides a flexible and customizable interface for managing and displaying scheduling data in a Windows Forms application. By leveraging the `IScheduleDataProvider` and the various properties and controls available within the `ScheduleControl`, developers can create highly personalized and functional scheduling solutions.

<!-- tags: [Syncfusion, WinForms, ScheduleControl, IScheduleDataProvider, GridControl, Calendar] keywords: [Schedule, UI controls, Windows Forms, User Interface, Data Serialization] -->
```