# 🎥 YouTube Downloader App (Python)

A simple yet powerful Python app to download YouTube videos directly to your machine.

---

## 🚀 Getting Started

### 1. **Clone the Repository**
```bash
git clone https://github.com/Ntwali14/YouTube_Downloader.git
cd YouTube_Downloader
```

### 2. **Set Up a Virtual Environment**
```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

- **Python 3.7+**  
  [Download Python](https://www.python.org/downloads/)

- **pytube**  
  For downloading YouTube videos.  
  [pytube documentation](https://pytube.io/en/latest/)

- **tkinter** (optional, for GUI)  
  For graphical user interface.  
  [tkinter documentation](https://docs.python.org/3/library/tkinter.html)

---

## 🔧 Features

- Download videos in high quality
- GUI support using `tkinter`
- Support for various resolutions
- Download progress indicator
- Handles video metadata

---

## 📝 Usage

### **Command Line**
1. Run the script:
    ```bash
    python downloader.py
    ```
2. Enter the YouTube video URL when prompted.

### **Graphical User Interface (GUI)**
1. Run the GUI script:
    ```bash
    python gui.py
    ```
2. Paste the YouTube URL and select download options.

---

## 🛠️ Implementation Details

- **Downloading Videos:**  
  Uses [`pytube.YouTube`](https://pytube.io/en/latest/user/quickstart.html) to fetch and download streams.

- **Progress Bar:**  
  Implemented using `tkinter.ttk.Progressbar`.  
  [Progressbar Example](https://realpython.com/python-gui-tkinter/#building-a-simple-gui-app-with-tkinter)

- **Error Handling:**  
  Handles invalid URLs, unavailable streams, and network errors.

- **Selecting Resolution:**  
  Lists available streams and lets the user choose.  
  [pytube Stream Selection](https://pytube.io/en/latest/user/streams.html)

---

## ❓ FAQ

- **How do I install `tkinter`?**  
  Usually comes with Python, but on some Linux systems:
  ```bash
  sudo apt-get install python3-tk
  ```

- **Where are videos saved?**  
  By default, in the current working directory. You can change the path in the script.

---

## 📚 Resources

- [pytube Documentation](https://pytube.io/en/latest/)
- [tkinter GUI Programming](https://realpython.com/python-gui-tkinter/)
- [Python Official Docs](https://docs.python.org/3/)

---

## 📝 License

MIT License

---

## 👨‍💻 Author

[Ntwali14](https://github.com/Ntwali14)