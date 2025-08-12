```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_058.jpeg
document_name: ProjIO
page_number: 058
page_id: ProjIO#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:21Z
fidelity: lossless
-->

## Essential ProjIO

### 4.5.1.3 Methods

#### Table 18: Calendar Methods

| Method                           | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| Equals                           | Returns a value indicating whether this instance is equal to a specified object |
| GetHashCode                      | Serves as a hash function for Calendar type                                 |
| GetType                          | Gets the type of the current instance                                      |
| ToString                         | Returns a string that represents the current object                         |
| Calendar.StandardCalendar()      | Creates a standard calendar                                                |
| Calendar.StandardCalendar(string calendarName) | Creates a standard calendar                                               |

#### 4.5.2 Creating a Standard Calendar

The static method `StandardCalendar` is used to create a standard calendar and add it to the project.

This method contains two overloads namely:
- `StandardCalendar()` – Creates a standard calendar
- `StandardCalendar(string calendarName)` – Creates a standard calendar by passing the calendar name

The following code snippet shows how to make use of this method:

#### Code Examples

##### C#

```csharp
// Creating a standard calendar
Calendar calendar = Calendar.StandardCalendar();

// Creating a standard calendar by passing the calendar name
Calendar calendar1 = Calendar.StandardCalendar("Standard");
```

##### VB

```vb
' Creating a standard calendar
Dim calendar As Calendar = Calendar.StandardCalendar()
```

## Page-level Navigation/TOC (if applicable)
- 4.5.1.3 Methods
- 4.5.2 Creating a Standard Calendar

### RAG Annotations
<!-- tags: [Syncfusion, Winforms, Calendar, StandardCalendar, Creating Calendars] keywords: [calendar, StandardCalendar, methods, static method] -->
```