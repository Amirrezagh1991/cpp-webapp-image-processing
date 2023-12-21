#include <iostream>
#include <opencv2/opencv.hpp>

int main(int argc, char* argv[]) {
    if (argc != 4) {
        std::cerr << "Usage: " << argv[0] << " input_image output_image processing_option" << std::endl;
        return 1;
    }

    // Load the input image
    cv::Mat image = cv::imread(argv[1]);

    if (image.empty()) {
        std::cerr << "Error: Unable to load input image." << std::endl;
        return 1;
    }

    // Perform image processing based on the selected option
    std::string processingOption = argv[3];
    if (processingOption == "grayscale") {
        // Convert the image to grayscale
        cv::cvtColor(image, image, cv::COLOR_BGR2GRAY);
    } else if (processingOption == "canny") {
        // Perform Canny edge detection
        cv::Mat edges;
        cv::cvtColor(image, edges, cv::COLOR_BGR2GRAY);
        cv::GaussianBlur(edges, edges, cv::Size(5, 5), 1.4, 1.4);
        cv::Canny(edges, edges, 50, 150);
        image = edges;
    } else {
        std::cerr << "Error: Invalid processing option." << std::endl;
        return 1;
    }

    // Save the processed image
    cv::imwrite(argv[2], image);

    return 0;
}
