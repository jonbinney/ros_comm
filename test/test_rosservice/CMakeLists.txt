cmake_minimum_required(VERSION 2.8.3)

project(test_rosservice)
find_package(catkin REQUIRED COMPONENTS genmsg rosunit rostest)
catkin_project(${PROJECT_NAME})

add_service_files(DIRECTORY srv
  FILES
  HeaderEcho.srv
  )
generate_messages(DEPENDENCIES std_msgs)

catkin_add_nosetests(test)

add_rostest(test/rosservice.test)
