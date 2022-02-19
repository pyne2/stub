# Generate version include file
execute_process(COMMAND python3 "${CMAKE_CURRENT_LIST_DIR}/../python/pyne2_${PYNE2_COMP_NAME}_version.py" WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})

# setup source files
set(PYNE2_SRCS
  ${PYNE2_VERSION_HEADER}
  )

# compile and link library
add_library(${PYNE2_LIB_NAME} ${PYNE2_SRCS})

#
# Install header files
#
FILE(GLOB h_files "${CMAKE_CURRENT_SOURCE_DIR}/*.h")
INSTALL(FILES ${h_files} DESTINATION include/pyne/${PYNE2_COMP_NAME} COMPONENT headers)

#
# Install libpyne_ground_state_data
#
INSTALL(TARGETS ${PYNE2_LIB_NAME} LIBRARY DESTINATION lib COMPONENT pyne)
