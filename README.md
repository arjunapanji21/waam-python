# WAAM (WhatsApp Auto Messenger)

An automated WhatsApp messaging tool built with Python for sending bulk personalized messages using data from Excel files.

## Features

- Send personalized WhatsApp messages to multiple recipients
- Read contact data from Excel files
- Custom message templates with variable support
- Error logging and failed message tracking
- Progress bar visualization
- Automated browser configuration

## Prerequisites

- Python 3.7+
- Chrome Browser
- ChromeDriver (compatible with your Chrome version)
- WhatsApp Web access

## Installation

1. Clone this repository:
```bash
git clone https://github.com/arjunapanji21/waam-python.git
```
2. Install required packages:
```bash
pip install -r requirements.txt
```

## Project Structure

- `main.py` - Main program file
- `utils.py` - Utility functions
- `screen_config.py` - Browser window configuration
- `message_template.txt` - Template for WhatsApp messages
- `contacts.xlsx` - Input file containing contact information
- `log.txt` - Program execution logs
- `failed_messages.xlsx` - Report of failed message attempts

## Usage

1. Prepare your contacts file (`contacts.xlsx`) with columns:
   - NIM (Student ID)
   - Name
   - Phone Number

2. Create your message template in `message_template.txt`:
   - Use {nama} for recipient's name
   - Use {nim} for student ID

3. Run the program:
```bash
python main.py
```

4. Scan the WhatsApp QR code when prompted

## Error Handling

- Invalid phone numbers are automatically logged
- Failed messages are recorded in `failed_messages.xlsx`
- Detailed logs are saved in `log.txt`

## Notes

- The program uses WhatsApp Web
- Make sure you have a stable internet connection
- Keep your WhatsApp session active during execution
- Phone numbers should be in international format

## Author

**Arjuna Panji Prakarsa**
- GitHub: [@arjunapanji21](https://github.com/arjunapanji21)
- LinkedIn: [Arjuna Panji Prakarsa](https://www.linkedin.com/in/arjunapanji)
- Website: [arjunaprakarsa.com](https://arjunaprakarsa.com)

A Software Engineer who loves to learn and explore new technologies.

## Contributing

Feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
