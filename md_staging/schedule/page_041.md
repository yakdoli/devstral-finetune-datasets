```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_041.jpeg
document_name: schedule
page_number: 041
page_id: schedule#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:10:03Z
fidelity: lossless
--> 

## Overview

- **Key Concepts**:
  - ScheduleData Base Classes for data interaction.
  - Utilization of IServiceProvider interfaces for providing data to ScheduleControl.
  - Pre-determined droplist settings for simplified integration.
  - Overview of ScheduleAppointment Class for managing appointments.

## Content

### 3.4.1 ScheduleData Base Classes

The ScheduleControl gets its data through its **DataSource** property, an **IScheduleDataProvider** object. So, it is this **IScheduleDataProvider** interface (and several other associated interfaces) that gives you the ability and facility to provide data to the ScheduleControl. To simplify this process of providing data, Essential Schedule also exposes these interfaces as base classes that include some pre-determine droplist settings that allow you to use the ScheduleControl with less coding work. But, you do have the option of working directly through the interfaces to construct your own data provider for the ScheduleControl.

The Essential Schedule library contains several base classes that implement the various data interfaces required by the ScheduleControl. These base classes use virtual methods which, you can override to provide a concrete data implementation. The classes in the **SimpleScheduleDataProvider** file that is shipped with the samples and used in the Tutorial section of this User Guide are derived from the ScheduleData base classes. Check out the shipped sample that uses the SimpleScheduleDataProvider as a data source for ScheduleControl.

The following sections discuss these ScheduleData base classes in more detail.

### 3.4.1.1 The Appointments Data

Here are the ScheduleData base classes that provide the Appointments data used by ScheduleControl. For code details of deriving these ScheduleData base classes to implement a data provider for the ScheduleControl, please see the **SimpleScheduleDataProvider** code file that ships as part of the ScheduleSample sample.

#### ScheduleAppointment Class

ScheduleAppointment is the class that defines the objects that represent appointments in the Schedule Control. This class implements **IScheduleAppointment** to provide an object to hold the concrete data associated with appointments. You can either derive this class or implement **IScheduleAppointment** yourself to extend or modify the information managed by the ScheduleAppointment class. Here are the properties exposed in ScheduleAppointment.

- **UniqueID**: gets or sets a unique integer associated with this item.

## API Reference

### Properties
- **UniqueID**
  - Type: integer
  - Description: A unique identifier associated with the appointment item.
  - Default: Not specified.

## Code Examples

### C#
```csharp
public class CustomScheduleAppointment : ScheduleAppointment
{
    public override object UniqueID
    {
        get;
        set;
    }
}
```

## Cross References
- See also: `SimpleScheduleDataProvider` file for detailed code samples and implementation.

<!-- tags: [ScheduleControl, IScheduleDataProvider, ScheduleAppointment, Appointments, Data, Windows Forms, Csharp] keywords: [ScheduleAppointment, UniqueID, IScheduleDataProvider, Appointments Data, DataSource, ScheduleControl, ScheduleSample, SimpleScheduleDataProvider, base classes, pre-determine settings, virtual methods] -->
```