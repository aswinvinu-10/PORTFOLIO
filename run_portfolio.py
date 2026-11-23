# Starts the portfolio and prints a local link and a public link.
# Stop it with Ctrl+C.
import os
import re
import subprocess
import sys
import time
import urllib.request
import webbrowser
from pathlib import Path

HERE = Path(__file__).resolve().parent
PORT = 8501
LOCAL_URL = f"http://localhost:{PORT}"
CLOUDFLARED = HERE / "cloudflared.exe"
CLOUDFLARED_URL = (
    "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe"
)


def check_files():
    needed = ["app.py", "ui.py", "data.py", "style.css", "views/home.py", "assets/dp.webp", "assets/Aswin_Vinu_Resume.pdf", "assets/Aswin_Vinu_CV.pdf"]
    missing = [n for n in needed if not (HERE / n).exists()]
    if missing:
        sys.exit("Missing files: " + ", ".join(missing) + "\nExtract the whole zip first, then run this file again.")


def ensure_streamlit():
    try:
        import streamlit  # noqa: F401
    except ImportError:
        print("Installing Streamlit (first time only)...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])


def ensure_cloudflared():
    if CLOUDFLARED.exists():
        return True
    if sys.platform != "win32":
        print("Public link: automatic download is for Windows only.")
        return False
    print("Downloading the free tunnel tool (first time only)...")
    try:
        urllib.request.urlretrieve(CLOUDFLARED_URL, CLOUDFLARED)
        return True
    except Exception as exc:
        print("Could not download the tunnel tool:", exc)
        return False


def main():
    os.chdir(HERE)
    check_files()
    ensure_streamlit()

    app = subprocess.Popen(
        [
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", str(PORT),
            "--server.headless", "true",
            "--browser.gatherUsageStats", "false",
        ]
    )
    time.sleep(6)
    print("\nLocal link (your computer only):", LOCAL_URL)
    webbrowser.open(LOCAL_URL)

    tunnel = None
    try:
        if ensure_cloudflared():
            tunnel = subprocess.Popen(
                [str(CLOUDFLARED), "tunnel", "--url", LOCAL_URL, "--protocol", "http2"],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            )
            shown = False
            for line in tunnel.stdout:
                match = re.search(r"https://[a-z0-9-]+\.trycloudflare\.com", line)
                if match and not shown:
                    shown = True
                    print("\n" + "=" * 60)
                    print("PUBLIC LINK (share this):", match.group(0))
                    print("Works only while this window is running.")
                    print("=" * 60 + "\n")
        else:
            app.wait()
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        if tunnel:
            tunnel.terminate()
        app.terminate()


if __name__ == "__main__":
    main()
