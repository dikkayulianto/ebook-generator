import os
import glob

FAVICON_TAGS = """  <!-- Favicon & Touch Icons -->
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
  <link rel="shortcut icon" href="/favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
"""

def inject():
    html_files = glob.glob("public/*.html")
    for fpath in html_files:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        if "favicon.svg" in content:
            continue

        if "<head>" in content:
            new_content = content.replace("<head>\n", f"<head>\n{FAVICON_TAGS}")
            if new_content == content:
                new_content = content.replace("<head>", f"<head>\n{FAVICON_TAGS}")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Injected favicon into: {fpath}")

if __name__ == "__main__":
    inject()
