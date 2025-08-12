```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_049.jpeg
document_name: schedule
page_number: 049
page_id: schedule#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:10:46Z
fidelity: lossless
--> 

# Essential Schedule for Windows Forms

You also have the option of deriving the ScheduleData base classes to provide custom data to the ScheduleControl. But, implementing the required interfaces directly will give you the most flexibility.

There are five interfaces that you can use to provide data for a ScheduleControl. There are two 'object' interfaces, IScheduleAppointment and ILookUpObject. These interfaces are primarily wrappers for a collection of properties.

- **IScheduleAppointment** wraps individual appointment data.
- **ILookUpObject** wraps the items you can see in drop-lists.

There are two 'list' interfaces, IScheduleAppointmentList and ILookUpObjectList. As their names suggest, these two interfaces are essentially lists of **IScheduleAppointments** and **ILookUpItems** respectively.

The last interface, **IScheduleDataProvider**, is a wrapper that holds multiple ILookUpObjectLists and one IScheduleAppointmentList. It is through this interface that the ScheduleControl interacts with the source of data, and in fact, ScheduleControl.DataSource is an IScheduleDataProvider object.

The IScheduleDataProvider object exposes methods of interacting with the data like retrieving lookup lists and providing appointments for specified time periods. The Essential Schedule source code file **ScheduleAppointment.cs** provides a base class implementation of these interfaces, exposing a partially abstract set of classes (the ScheduleData classes) that you can use to indirectly implement these interfaces.

The **SimpleScheduleDataProvider** classes that were used in the Tutorial are derived from these base classes.

The following sections discuss these required data interfaces in more detail.

## 3.4.2.1 The Appointments Data

Three of the five data interfaces work directly with the Appointment data. Here are the three interfaces.

- **IScheduleAppointment Interface**
  
  IScheduleAppointment defines the objects that represent appointments in the ScheduleControl.
```