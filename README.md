# FormAutoChecker
**ParticipantChecker** is a Python-based automation script designed to verify participant information on a web-based announcement system. This script uses Selenium to interact with the web form, automating the process of inputting participant IDs and retrieving corresponding results.

## Features
- Automates participant verification on the [Tanoto Foundation Scholarship](https://form.jotform.com/242969188886482) announcement page (powered by JotForm).
- Retrieves and displays participant names and their university of origin.
- Handles iterative input of multiple participant IDs from a text file.
- Saves results and errors to an output file for later review.
- Automatically navigates back to the input page after each query.

## Requirements
To run this script, you need the following installed on your system:

1. Python 3.7 or above
2. Google Chrome
3. ChromeDriver (compatible with your Chrome version)
4. Required Python packages:
   - `selenium`

## Setup Instructions

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/ParticipantChecker.git
   cd ParticipantChecker
   ```

2. Install the required Python packages:
   ```bash
   pip install selenium
   ```

3. Download ChromeDriver and ensure it matches your installed Chrome version. Place it in a known directory and update the `Service` path in the script accordingly:
   ```python
   service = Service(r'path-to-your-chromedriver')
   ```

4. Prepare your input file (`pesertalolos.txt`) containing participant IDs, one ID per line.

5. Run the script:
   ```bash
   python participant_checker.py
   ```

## How It Works
1. The script navigates to the Tanoto Foundation Scholarship JotForm page.
2. For the first iteration, it initializes the form interaction by:
   - Clicking "Start"
   - Navigating to the participant ID input section.
3. It inputs each participant ID from the text file, retrieves the participant's name and university, and saves the results.
4. After each iteration, it navigates back to the input section using the "Previous" button.
5. A summary of the results, including the total number of successful verifications, is saved to `hasil_peserta.txt`.

## Example Output
After running the script, the `hasil_peserta.txt` file will look like this:

```
Peserta 12345 lolos! Nama: John Doe, Asal Universitas: Universitas Indonesia
Peserta 67890 lolos! Nama: Jane Smith, Asal Universitas: Universitas Gadjah Mada
...
Total peserta yang lolos adalah: 10
```

## Notes
- This script was built and tested using the Tanoto Foundation Scholarship announcement form as an example.
- Ensure your internet connection is stable for smooth execution.

## Disclaimer
This project is for educational purposes only. Unauthorized or improper use of automation scripts on web services may violate their terms of use. Ensure you have proper permissions before running this script on any web service.

---

Feel free to contribute or raise issues for further improvements!

Credits to GPT.
