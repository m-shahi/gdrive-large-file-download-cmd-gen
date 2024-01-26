import sys
import pyperclip

def generate_download_url(file_id, output_filename):
    try:
        url = f"curl -L 'https://drive.usercontent.google.com/download?export=download&id={file_id}&confirm=t&export=download' > {output_filename}"
        pyperclip.copy(url)
        print('Copied to your clipboard successfully!')
        print("Your Clipboard Content:\n", pyperclip.paste())
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python google_drive_downloader.py <file_id> <output_filename>")
        sys.exit(1)

    file_id = sys.argv[1]
    output_filename = sys.argv[2]
    generate_download_url(file_id, output_filename)

if __name__ == "__main__":
    main()
