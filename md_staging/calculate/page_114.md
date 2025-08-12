```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_114.jpeg
document_name: calculate
page_number: 114
page_id: calculate#page_114
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:58Z
fidelity: lossless
-->

## Date and Time

### Overview
- Lists the Date and Time functions included in `Essential calculate`.
- Provides descriptions for each function to assist in understanding their usage.

### Content

#### Date and Time Functions

The following table lists the Date and Time functions included with Essential calculate:

| Function Name    | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Date**         | Returns the sequential serial number that represents a particular date.     |
| **Datevalue**    | Returns the serial number of the date value.                              |
| **Day**          | Returns the day of the month.                                              |
| **Days360**      | Returns the number of days between two dates using a 360-day year.         |
| **Hour**         | Returns the hour from 0 to 23.                                             |
| **Minute**       | Returns the minute from 0 to 59.                                           |
| **Month**        | Returns the month from 1 to 12.                                            |
| **Now**          | Returns the current date and time.                                          |
| **Second**       | Returns the second from 0 to 59.                                           |
| **Time**         | Returns serial number time.                                                |
| **Timevalue**    | Returns the serial number time from a string.                             |
| **Today**        | Returns the current date.                                                  |

## Code Examples

Below are examples demonstrating the usage of some Date and Time functions:

- **Example 1: Using the `Now` Function**
  ```csharp
  var currentDateAndTime = Now();
  Console.WriteLine(currentDateAndTime);
  ```

- **Example 2: Using the `Date` Function**
  ```csharp
  var serialNumber = Date(2023, 8, 9);
  Console.WriteLine(serialNumber);
  ```

## Cross References

- See also: 
  - **String Functions** for more details on `Text`, `Value`, `Len`, and `MID`.
  - **Time and Date Formatting** for more complex formatting options.

<!-- tags: [date, time, datefunctions, essentialcalculate, syncfusionwinforms] keywords: [datevalue, days360, hour, minute, month, now, second, time, timevalue, today] -->
```