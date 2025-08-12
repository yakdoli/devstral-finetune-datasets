```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_047.jpeg
document_name: schedule
page_number: 047
page_id: schedule#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:10:25Z
fidelity: lossless
-->

## Overview

- Provides methods and properties for managing and setting lists of options for various scheduling data, including `MarkerValue`, `LocationValue`, and `Owner` options.  
- Highlights the use of derived classes implementing `IListObject` for dynamic drop-down list data.  

## Essential Schedule for Windows Forms

```csharp
/// <summary>
/// Gets or sets the list for the MarkerValue options.
/// </summary>
protected ListObjectList MarkerList
{
    get { return markerList; }
    set { markerList = value; }
}

/// <summary>
/// Returns the list for the LocationValue options.
/// </summary>
public virtual ILookUpObjectList GetLocations()
{
    return LocationList;
}

/// <summary>
/// Gets or sets the list for the LocationValue options.
/// </summary>
protected ListObjectList LocationList
{
    get { return locationList; }
    set { locationList = value; }
}

/// <summary>
/// Returns the list for the Owner options.
/// </summary>
public virtual ILookUpObjectList GetOwners()
{
    return OwnerList;
}

/// <summary>
/// Gets or sets the list for the Owner options.
/// </summary>
protected ListObjectList OwnerList
{
    get { return ownerList; }
    set { ownerList = value; }
}
```

### 3.4.1.2 The DropLists

The second type of data required of the `ScheduleControl` is the `DropList` data. You have seen a concrete implementation of providing this `DropList` data in the **The Appointments Data** discussion. Two classes that can provide such data are listed below.

- **ListObjectClass**

  The `ListObject` is a wrapper class for list choices that can have a `ValueMember`, `DisplayMember`, and `ColorMember` associated with them. The class is an implementation of the `IListObject` that exposes the `IListObject` functionality as virtual members. This allows you to implement the `IListObject` by deriving the `ListObject` and overriding virtual properties. Here are the properties exposed by this class.

## API Reference

### ListObjectClass

- **Properties**:
  - `ValueMember`: The value to be associated with the list item.
  - `DisplayMember`: The text displayed to the user for the list item.
  - `ColorMember`: The color or style associated with the list item.

### Methods

- **GetLocations**
  ```csharp
  public virtual ILookUpObjectList GetLocations();
  ```
  - **Returns**: The list of `LocationValue` options.

- **GetOwners**
  ```csharp
  public virtual ILookUpObjectList GetOwners();
  ```
  - **Returns**: The list of `Owner` options.

## Code Examples

Here's an example of how `ListObject` can be used to populate a `DropList`:

```csharp
// Creating a ListObject list for MarkerValues
ListObjectList markerList = new ListObjectList();
markerList.Add(new ListObject("Marker1", "Red", "Value1"));
markerList.Add(new ListObject("Marker2", "Blue", "Value2"));

// Populating the GetLocations method
ILookUpObjectList locations = new LocationObjectList();
locations.Add(new LocationObject("Location1", "USA", "Code1"));
locations.Add(new LocationObject("Location2", "UK", "Code2"));
```

## Page-level Navigation/TOC (if applicable)
- **3.4.1.2 The DropLists**
  - Overview of the DropLists in ScheduleControl
  - Details of the ListObjectClass

## Cross References
- Refer to **The Appointments Data** section for more concrete implementation examples of `DropList` usage.
<!-- tags: [Syncfusion Winforms, ScheduleControl, DropList, IListObject, ListObjectClass] keywords: [MarkerValue, LocationValue, Owner, ScheduleControl, DropLists, IListObject, ListObject, ILookUpObjectList] -->
```