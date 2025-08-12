```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_233.jpeg
document_name: calculate
page_number: 233
page_id: calculate#page_233
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:34Z
fidelity: lossless
-->  

## Timevalue Function

### Syntax

```markdown
TIMEVALUE(time_text)
```

**Where:**

- `time_text` is a text string that represents a time as a formatted string; for example, "6:45 PM" and "18:45" text strings within quotation marks that represent time.

### Remarks

- Date information in `time_text` is ignored.

---

## 4.7.171 TODAY Function

**Returns the serial number of the current date. The serial number is the number of days since Jan 1, 1900.**

### Syntax

```markdown
TODAY()
```

### Remarks

- Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900, is serial number 1, and January 1, 2008, is serial number **39448** because it is 39,448 days after January 1, 1900.

---

## 4.7.172 Trim Function

**The Trim function returns a text value with the leading and trailing spaces removed.**

### Syntax

```markdown
Trim( text )
```

**Where:**

- `text` is the text value for which you want to remove the leading and the trailing spaces.
```