# Vision Volume Control [![License: MIT][License-Badge]](LICENSE.md)  [![Made with Python][Python-Badge]](https://www.python.org/)

This is a simple python script that uses OpenCV to detect the volume of a video stream and adjust the volume of the system accordingly. The script uses the `mediapipe` library to detect the hand landmarks and calculate the volume based on the distance between the thumb and the index finger.

## Installation

- Clone the repository

    ```bash
    git clone https://github.com/Polymath-Saksh/Vision-Volume-Control.git
    ```

- Install the required libraries

    ```bash
    pip install -r requirements.txt
    ```

## Usage

- Run the script

    ```bash
    python main.py
    ```

- Adjust the volume by moving your hand up and down. The volume will be adjusted based on the distance between the thumb and the index finger.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Mediapipe](https://google.github.io/mediapipe/)
- [OpenCV](https://opencv.org/)
- [Pycaw](https://github.com/AndreMiras/pycaw)

[License-Badge]: https://img.shields.io/badge/License-MIT-blue.svg
[Python-Badge]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff