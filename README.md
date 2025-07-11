
# 🧪 Selenium Multi-Browser Automation Suite

This project showcases **multi-browser web automation** using **Python**, **Selenium WebDriver**, and useful utilities like **dropdown handling**, **JavaScript alerts**, **broken image detection**, and **parallel test execution**. It is designed to simulate real-world scenarios across platforms like **Amazon** and **YouTube**.

It includes two primary workflows:

* 🛒 **Amazon Shopping Automation**
* 📺 **YouTube Video Interaction Automation**

---

## 📌 Features

### 🔹 Amazon Automation

* Launches Amazon in a browser
* Selects “Video Games” from the **dropdown menu**
* Searches for **"God of War"**
* Scrolls through the results and clicks on a relevant game
* Adds the game to the **cart**
* Handles exceptions and captures screenshots on errors

### 🔹 YouTube Automation

* Launches YouTube in a second browser
* Searches for **“Selenium FreeCodeCamp”**
* Plays the top matching video
* Performs browser actions: **refresh**, **back**, **forward**
* Uses `try-except` for **error debugging**

### 🧪 Additional Scripts

* ✅ **Checkbox Handling** – select and verify checkboxes
* 📉 **Broken Image Detection** – find non-loading images using `requests`
* 📤 **Dropdown Interaction** – select items by text, index, or value
* ⏳ **Explicit Waits** – wait until elements are ready
* 🧾 **Excel Data Handling** – read/write test data via `.xlsx` using `openpyxl`
* ⚠️ **JavaScript Alerts** – display browser pop-ups via automation
* 🔁 **Browser Navigation** – forward/backward button usage

---

## 🧰 Tech Stack

| Tool / Library      | Purpose                            |
| ------------------- | ---------------------------------- |
| Python              | Programming language               |
| Selenium WebDriver  | Web automation                     |
| ChromeDriver        | Chrome browser automation          |
| GeckoDriver         | Firefox browser automation         |
| OpenPyXL (optional) | Excel file interaction             |
| Requests            | HTTP requests (for image checking) |

---

## 📂 Project Structure

| File / Folder           | Purpose                                       |
| ----------------------- | --------------------------------------------- |
| `main.py`               | Runs Amazon and YouTube flows in parallel     |
| `amazon_automation.py`  | Contains Amazon shopping automation script    |
| `youtube_automation.py` | Contains YouTube video automation script      |
| `alert_box.py`          | Shows JavaScript alerts                       |
| `broken images.py`      | Detects broken image URLs                     |
| `checkbox.py`           | Interacts with checkboxes                     |
| `dropdown.py`           | Demonstrates dropdown selection               |
| `explicit.py`           | Uses explicit waits for slow-loading elements |
| `fwd & bgd.py`          | Demonstrates browser navigation               |
| `excel testing.py`      | Reads Excel files using openpyxl              |
| `data.xlsx`             | Excel file with input data                    |
| `amazon_error.png`      | Screenshot on Amazon error                    |
| `youtube_error.png`     | Screenshot on YouTube error (optional)        |
| `README.md`             | Documentation for the entire project          |

---

## 🚀 How to Run

1. Make sure you have **ChromeDriver** and/or **GeckoDriver** installed and accessible in your system path.
2. Install dependencies:

   ```bash
   pip install selenium requests openpyxl
   ```
3. Run the main automation:

   ```bash
   python main.py
   ```

---
