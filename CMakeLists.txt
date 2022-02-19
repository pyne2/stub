# Defines the CMake commands/policies
cmake_minimum_required(VERSION 3.0.0)

SET(PYNE2_COMP_NAME "stub")

# Make the scripts available in the 'cmake' directory available for the
# 'include()' command, 'find_package()' command.
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/config")

include(Pyne2Macros)

pyne2_set_products()

# Setup the project 
project(${PYNE2_PROJECT_NAME})

pyne2_print_logo()  # Beware of dragons

# This makes all the libraries build as SHARED
set(BUILD_SHARED_LIBS true)

add_subdirectory(src)
