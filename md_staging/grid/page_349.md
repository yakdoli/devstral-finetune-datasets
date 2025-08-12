```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_349.jpeg
document_name: grid
page_number: 349
page_id: grid#page_349
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:11:25Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains error handling in grid functions.
- Provides details on hyperbolic functions like SECH.
- Describes time extraction functions like SECOND.
- Explains the SIGN function to determine number signs.

## Content

### 4.1.4.6.6.210 SECH
**Description:**  
The SECH function returns the hyperbolic secant of an angle.

**Syntax:**  
SECH(number) where:
- **number:** angle in radians for which you want the secant.

**Remarks:**  
- **#NUM!:** Occurs if the number is outside its constraints.
- **#VALUE!:** Occurs if the number is a non-numeric value.

---

### 4.1.4.6.6.211 SECOND
**Description:**  
Returns the seconds of a time value. The second is given as an integer in the range 0 (zero) to 59.

**Syntax:**  
SECOND(serial_number), where:
- **serial_number:** is the time that contains the seconds you want to find.

**Remarks:**  
- Time values are a portion of a date value and are represented by a decimal number (for example, 12:00 PM is represented as 0.5 because it is half of a day).

---

### 4.1.4.6.6.212 SIGN
**Description:**  
Determines the sign of a number. Returns 1 if the number is positive, zero (0) if the number is 0, and -1 if the number is negative.

**Syntax:**  
None provided in the text.

---

### Additional Information
- **Copyright:** © 2013 Syncfusion. All rights reserved.

## API Reference

### Methods
- **SECH(number):** Returns the hyperbolic secant of the specified angle.
- **SECOND(serial_number):** Extracts the seconds from a time value.
- **SIGN(number):** Determines the sign of a number.

### Parameters
- **number:** For SECH and SIGN, represents the angle in radians or the number to evaluate.
- **serial_number:** For SECOND, represents the time that contains the seconds.

### Exceptions
- **#NUM!:** Emitted when a number is outside its constraints.
- **#VALUE!:** Emitted when the input is a non-numeric value.

## Code Examples

### C#
```csharp
// Example for SECH function
using System;

double angle = Math.PI / 4; // 45 degrees in radians
double secant = Math.Round(1 / Math.Cosh(angle), 2); // Equivalent to SECH
Console.WriteLine("Hyperbolic Secant: " + secant);

// Example for SECOND function
TimeSpan time = new TimeSpan(0, 0, 30); // 30 seconds
int seconds = TimeSpan.FromSeconds(time.TotalSeconds).Seconds;
Console.WriteLine("Seconds: " + seconds);

// Example for SIGN function
double number = -5;
int sign = Math.Sign(number); // Returns -1
Console.WriteLine("Sign: " + sign);
```

---

<!-- tags: [Essential Grid, Windows Forms, SECH, SECOND, SIGN, error handling, hyperbolic functions, time extraction, number sign, Grid, WinForms] keywords: [SECH, SECOND, SIGN, error handling, hyperbolic secant, time, date, number sign, functions, syntax, remarks] -->
```