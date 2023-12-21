cmake_minimum_required(VERSION 3.12)
project(ImageProcessing)

find_package(OpenCV REQUIRED)

add_executable(image_processing backend/main.cpp)
target_link_libraries(image_processing PRIVATE ${OpenCV_LIBS})