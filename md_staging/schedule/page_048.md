```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_048.jpeg
document_name: schedule
page_number: 048
page_id: schedule#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:11:30Z
fidelity: lossless
-->

## Essential Schedule for Windows Forms

### Code Example

```csharp
[C#]

/// An integer that is stored in the data objects to represent this object.
public virtual int ValueMember

/// A string that is used when this object is displayed.
public virtual string DisplayMember

/// A color associated with this object.
public virtual Color ColorMember
```

### ListObjectList

- **ListObjectList**
  The `ListObjectList` is a strongly-typed `ArrayList` that holds a collection of `ListObjects`. The class is derived from `ArrayList` and implements both `ITypedList` and `IList`. Here are the properties and methods exposed in this class:

```csharp
[C#]

/// Returns the property descriptors for each property in ListObject.</returns>
public PropertyDescriptorCollection GetItemProperties(PropertyDescriptor[] listAccessors)

/// Returns a list name</returns>
public string GetListName(PropertyDescriptor[] listAccessors)

/// Gets or sets the i-th item in the list.
public new ILookupObject this[int i]
```

### 3.4.2 IScheduleData Interfaces

The `ScheduleControl` gets its data through its `DataSource` property, an `IScheduleDataProvider` object.

So, it is this `IScheduleDataProvider` interface (and several other associated interfaces) that gives you the ability and facility to provide data to the `ScheduleControl`.

This section discusses the actual interfaces required to provide data to the `ScheduleControl`. If you need the access your own custom datastore, then you can create objects that implement these interfaces on which the `ScheduleControl` relies to provide data from your custom datastore.

If you just need a local disk file datastore, then using the implementation provided by the classes in the `SimpleScheduleDataProvider` file that is shipped with the samples, may serve your purpose.

---

```xml
© 2013 Syncfusion. All rights reserved. | Page 48
```

<!-- tags: [product, schedule, WinForms, listobjectlist, ischeduledata, interface, custom datastore, data provider] keywords: [schedulecontrol, datasource, listobjectlist, propertydescriptor, propertydescriptorcollection, ilookupobject, developers] -->
```