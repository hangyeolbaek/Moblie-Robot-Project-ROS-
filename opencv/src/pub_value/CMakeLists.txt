cmake_minimum_required(VERSION 3.0.2)
project(pub_value)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  rospy
  sensor_msgs
  std_msgs
)

add_message_files(FILES StringArray.msg) 
generate_messages(DEPENDENCIES std_msgs sensor_msgs)
catkin_package(CATKIN_DEPENDS std_msgs roscpp rospy message_runtime) 

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
