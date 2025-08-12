```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_034.jpeg
document_name: schedule
page_number: 034
page_id: schedule#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:09:44Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview
- **Date Selection and Event Scheduling**: Users can navigate and select dates to view schedules.
- **Time-based Event Entry**: Double-clicking on time slots opens a new screen for entering schedule items.

## Content

### Day View Interface
Figure 23 illustrates the Day view resulting from the ContextMenu. The interface displays dates and individual time slots for scheduling appointments.

#### Key Components
1. **Calendar Navigation**: Allows switching between months and selecting dates.
2. **ScheduleGrid**: Shows time slots throughout the day where new appointments can be added.
3. **ScheduleControl Interaction**: Double-clicking a time slot opens a new appointment screen.

#### Steps for Adding a New Schedule Item
11. Double-click one of the time slots on the ScheduleGrid in the ScheduleControl. This action will display a new appointment screen where you can enter a new schedule item as shown below.

## API Reference

### Example Usage
```csharp
// Example: Adding a new event to the ScheduleControl
scheduleControl.InitialUIUpdate += (s, e) =>
{
    // Customize or initialize the schedule control as needed
    scheduleControl.AddEvent(new ScheduleEvent
    {
        Start = DateTime.Now,
        End = DateTime.Now.AddHours(1),
        Subject = "New Event",
        Description = "Description of the new event"
    });
    scheduleControl.UpdateUI();
};
```

### Related Sections
- See also: [Complete API Documentation for ScheduleControl](#schedulecontrol-api-documentation)

## Code Examples

### C#
```csharp
// Example: Setting up the ScheduleControl for Day View
scheduler.DayViewSettings.ShowAllDayPanel = true;
scheduler.DayViewSettings.TimeRulerSettings.IsVisible = true;
```

### VB
```vb
' Example: Configuring the ScheduleControl for Day View
scheduler.DayViewSettings.ShowAllDayPanel = True
scheduler.DayViewSettings.TimeRulerSettings.IsVisible = True
```

## Page-level Navigation/TOC (if applicable)

- **Day View Interface**
- **Key Components**
- **Steps for Adding a New Schedule Item**
- **API Reference**
- **Code Examples**

## RAG Annotations
<!-- tags: syncfusion-winforms, schedulecontrol, dayview, event-scheduling keywords: date-navigation, time-slots, new-appointment-screen, schedulegrid -->
```