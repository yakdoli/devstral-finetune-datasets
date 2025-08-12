```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_040.jpeg
document_name: schedule
page_number: 040
page_id: schedule#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:11:03Z
fidelity: lossless
-->

## Essential Schedule for Windows Forms

The ScheduleControl does all its data access through interfaces. To support custom data objects, you would have your data objects implement these particular interfaces that are discussed in the following sections. In addition, included in the Essential Schedule library are base classes that implement these required interfaces. So, you can also create data sources for the ScheduleControl by deriving these base classes. The SimpleScheduleDataProvider classes that were used in the Tutorial are derived from these base classes.

### Base Classes

- **ScheduleDataProvider Class**: provides an empty implementation of the IScheduleDataProvider.  
  The implementation is done through virtual methods. You can then derive this class and through its overrides, set up an IScheduleDataProvider. See the SimpleScheduleDataProvider class in the ScheduleSample sample.

- **ScheduleAppointmentList Class**: provides an implementation of IScheduleAppointmentList and is essentially a wrapper class for an ArrayList that holds ScheduleAppointments.

- **ScheduleAppointment Class**: provides an implementation of IScheduleAppointment and defines the objects that represent appointments in the ScheduleControl.

- **LookUpObjectList Class**: strongly typed ArrayList that holds list option values that are used in the new appointment form.

- **LookUpObject Class**: wrapper class for list choices that can have a valueMember, displayMember, and colorMember associated with them.

The lists for the ShowTime and Label options on the Appointment forms use these objects.

### Interfaces

- **IScheduleDataProvider Interface**: provides the framework for providing schedule item data to the ScheduleControl.

- **IScheduleAppointmentList Interface**: serves as a collection of ISchedule objects.

- **IScheduleAppointment Interface**: defines individual schedule items.

- **ILookUpObjectList Interface**: serves as a collection of ILookUpObjects.

- **ILookUpObject Interface**: enables Choice lists within the ScheduleControl, that are used to provide possible schedule item information (like location or a reminder).

<!-- tags: [schedule, interface, windows forms, data access, winforms] keywords: [ScheduleControl, IScheduleDataProvider, ScheduleAppointmentList, ScheduleAppointment, LookUpObjectList, LookUpObject, ScheduleDataProvier, ScheduleAppointmentList, ScheduleAppointment, ILookUpObjectList, ILookUpObject, Essential Schedule library, base classes, virtual methods, data sources, SimpleScheduleDataProvider, ScheduleSample sample] -->
```