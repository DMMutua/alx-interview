# UTF-8 Validation
Write a method that determines if a given data set represents a valid UTF-8 encoding.<br>

* Prototype: def validUTF8(data)<br>
* Return: True if data is a valid UTF-8 encoding, else return False<br>
* A character in UTF-8 can be 1 to 4 bytes long<br>
* The data set can contain multiple characters<br>
* The data will be represented by a list of integers<br>
* Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer<br>
