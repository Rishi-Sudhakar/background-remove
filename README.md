# Background Removal Tool

This repository contains a simple tool for removing backgrounds from images using image processing techniques. It currently supports basic background removal using color-based segmentation.

## Features

- **Background Removal**: Uses OpenCV for simple color-based background removal.
- **Input/Output**: Processes JPEG images and outputs PNG images with removed backgrounds.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Rishi-Sudhakar/background-remove.git
   cd background-remove
   ```

2. **Install Dependencies:**
   ```bash
   pip3 install opencv-python
   ```
   Use "pip" instead of "pip3" if "pip3" doesn’t work.

3. **Run the Tool:**
   ```bash
   python remove_background.py input.jpg output.png
   ```
   Replace `input.jpg` with your input image and `output.png` with the desired output filename, or just run the tool without filename, just place the file "input.jpg" in the same directory.

## Future Development

- **Website Version**: A web-based version of the tool is currently in development, aiming to provide a user-friendly interface for background removal.
- **Improved Algorithms**: Plans to incorporate machine learning-based models for more accurate background segmentation.
- **Enhanced User Interaction**: Features like real-time preview, batch processing, and manual adjustment options.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or want to contribute code, feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
